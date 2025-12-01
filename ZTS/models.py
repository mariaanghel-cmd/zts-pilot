import json
import random
from otree.api import *
c = cu
from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

author = 'Jason Friedman, Student Helper COG, ETHZ'

doc = """
Trading App of the Zurich Trading Simulator (ZTS).
A web-based behaviour experiment in the form of a trading game, 
designed by the Chair of Cognitive Science - ETH Zurich.
"""

class Constants(BaseConstants):
    name_in_url = 'zts'
    players_per_group = None
    num_rounds = 20 # Actual num_rounds is specified in session config, by the length of the list 'timeseries_filename'!

class Subsession(BaseSubsession):

    def creating_session(self):
        """
        Called when each ZTS subsession is created.

        - Sets the effective number of rounds based on the timeseries_filename list.
        - If training_round is True, the first round is a training (unpaid) round.
        - Draws a random payoff round from the set of payoff-eligible rounds.
        - Stores the treatment flag ('control' or 'FE') for each participant.
        """

        if self.round_number == 1:

            # effective number of rounds = number of timeseries files
            self.session.num_rounds = len(json.loads(self.session.config['timeseries_filename']))

            # which treatment are we in? (set in settings.py)
            treatment = self.session.config.get('treatment', 'control')

            for player in self.get_players():

                # first payoff-eligible round
                first_round = 1
                if self.session.config['training_round']:
                    first_round = 2

                # sanity check
                if first_round > self.session.num_rounds:
                    raise ValueError(
                        'Num rounds cannot be smaller than 1 (or 2 if there is a training session)!'
                    )

                # random payoff round among eligible rounds (original ZTS logic)
                player.participant.vars['round_to_pay'] = random.randint(
                    first_round, self.session.num_rounds
                )

                # store treatment flag for later use
                player.participant.vars['treatment'] = treatment

    def get_config_multivalue(self, value_name):
        """
        Some config values can contain either a list of values (for each round)
        or a single value. This function gives a unified accessor for both
        formats: for lists it picks the value for the current round.
        """
        parsed_value = json.loads(self.session.config[value_name])
        if isinstance(parsed_value, list):
            assert len(parsed_value) >= self.session.num_rounds, (
                value_name + ' contains less entries than effective rounds!'
            )
            return parsed_value[self.round_number - 1]
        else:
            return parsed_value

    def get_timeseries_values(self):
        """
        Read this round's timeseries file and return:
        - asset name
        - list of prices
        - list of news strings (showing news only in the FE treatment)

        News text comes from the 3rd column ('news') of the CSV.
        """
        filename = self.get_config_multivalue('timeseries_filename')
        asset = filename.strip('.csv')
        path = self.session.config['timeseries_filepath'] + filename
        rows = read_csv(path, TimeSeriesFile)

        # prices are always used
        prices = [dic['price'] for dic in rows]

        # raw news from CSV (3rd column)
        if 'news' in rows[0].keys():
            news_raw = [dic['news'] if dic['news'] else '' for dic in rows]
        else:
            news_raw = [''] * len(prices)

        # treatment: FE sees news, control does not
        treatment = self.session.config.get('treatment', 'control')
        if treatment == 'FE':
            news = news_raw
        else:
            news = [''] * len(prices)

        return asset, prices, news
                
class Group(BaseGroup):
    pass

class Player(BasePlayer):
    cash = models.FloatField(initial=1000000)
    shares = models.FloatField(initial=0)
    share_value = models.FloatField(initial=0)
    portfolio_value = models.FloatField(initial=0)
    pandl = models.FloatField(initial=0)    

    def live_trading_report(self, payload):
        # Ignore websocket messages that don't contain proper data
        if not payload:
            return
        if payload.get('cash') is None:
            return
        """
        Accepts the "daily" trading Reports from the front end and
        further processes them to store them in the database
        :param payload: trading report
        """
        #print('received a report from', self.id_in_group, ':', payload)
        self.cash = float(payload['cash'])
        self.shares = int(payload['owned_shares'])
        self.share_value = float(payload['share_value'])
        self.portfolio_value = float(payload['portfolio_value'])
        self.pandl = float(payload['pandl'])

        TradingAction.create(
            player=self,
            action=payload['action'],
            quantity = payload['quantity'],
            time = payload['time'],
            price_per_share = payload['price_per_share'],
            cash = payload['cash'],
            owned_shares = payload['owned_shares'],
            share_value = payload['share_value'],
            portfolio_value = payload['portfolio_value'],
            cur_day = payload['cur_day'],
            asset = payload['asset'],
            roi = payload['roi_percent']
        )

        # Set payoff if end of round
        if(payload['action'] == 'End'):
            self.set_payoff()

    def set_payoff(self):
        """
        Set the players payoff for the current round to the total portfolio value.
        If we want participants final payoff to be chosen randomly
        from all rounds instead of accumulatee standard) subtract current payoff
        from participants.payoff if we are not in round_to_pay. Also payoff should not 
        count if we are in a training round.
        """
        self.payoff = 0
        self.payoff = self.portfolio_value
        random_payoff = self.session.config['random_round_payoff']
        training_round = self.session.config['training_round']
        if(random_payoff and self.round_number != self.participant.vars['round_to_pay']):
            self.participant.payoff -= self.payoff
        elif(training_round and self.round_number == 1):
            self.participant.payoff -= self.payoff

class TradingAction(ExtraModel):
    """
    An extra database model that is used to store all the transactions. Each transaction is
    linked to the player that executed it. 
    """
    ACTIONS = [
        ('Buy', 'Buy'),
        ('Sell', 'Sell'),
        ('Start', 'Start'),
        ('End', 'End'),
    ]

    player = models.Link(Player)
    action = models.CharField(choices=ACTIONS, max_length=10)
    quantity = models.FloatField(initial=0.0)
    time = models.StringField()
    price_per_share = models.FloatField()
    cash = models.FloatField()
    owned_shares = models.FloatField()
    share_value = models.FloatField()
    portfolio_value = models.FloatField()
    cur_day = models.IntegerField()
    asset = models.CharField(blank=True, max_length=100)
    roi = models.FloatField()

class TimeSeriesFile(ExtraModel):
    date = models.StringField()
    price = models.FloatField()
    news = models.StringField()

def custom_export(players):
    """
    Create a custom export, that allows us to download more 
    detailed trading reports as csv or excel files. 

    NOTE: the custom export will output all Trading actions that are found in the database,
    i.e. also of earlier sessions --> if you do not want this you migth need to implement a filter
    here.

    :param players: queryset of all players in the database
    :yield: a titel row and then the corresponding values one after the other
    """
    # header row
    yield ['session', 'round_nr', 'participant', 'action', 'quantity', 'price_per_share', 'cash', 'owned_shares', 'share_value', 'portfolio_value', 'cur_day',
           'asset', 'roi']
    # data content
    for p in players:
        for ta in TradingAction.filter(player=p):
            yield [p.session.code, p.subsession.round_number, p.participant.code, ta.action, ta.quantity, ta.price_per_share, ta.cash, ta.owned_shares, ta.share_value,
                   ta.portfolio_value, ta.cur_day, ta.asset, ta.roi]
    