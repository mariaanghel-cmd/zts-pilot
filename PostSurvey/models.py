from otree.api import *


doc = """
Post-treatment survey:
"""


class C(BaseConstants):
    NAME_IN_URL = 'PostSurvey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # ----------------------------
    # Part I: Post-game perceptions & feedback
    # ----------------------------

    news_valence = models.IntegerField(
        label="The news felt:",
        choices=[[i, str(i)] for i in range(1, 8)],
        widget=widgets.RadioSelect,
        blank=True,
    )

    feedback_text = models.LongStringField(
        label="This was a pilot experiment. Any feedback about your experience to help us improve the real experiment? (Optional)",
        blank=True,
    )

