from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    session_name='test_session',
    timeseries_filepath='_static/ZTS/timeseries_files/',
    timeseries_filename='["demo_1.csv", "AAPL.csv", "AMZN.csv", "CAT.csv", "JNJ.csv", "JPM.csv", "KO.csv", "MSFT.csv", "NVDA.csv", "UNH.csv", "XOM.csv"]',
    refresh_rate_ms='[800, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]',
    initial_cash='[5000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000]',
    initial_shares='[10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]',
    trading_button_values='[[1, 10, 20], [1, 10, 20], [1, 10, 20], [1, 10, 20], [1, 10, 20], [1, 10, 20], [1, 10, 20], [1, 10, 20], [1, 10, 20], [1, 10, 20], [1, 10, 20]]',
    random_round_payoff=True,
    training_round=True,
    graph_buffer=0.05,
    real_world_currency_per_point=1,
    participation_fee=1.00,
    num_rounds=11, 
    doc='',
)

SESSION_CONFIGS = [
    dict(
        name='ZTS_control_V1',
        display_name='ZTS Control (No news)',
        num_demo_participants=10,
        app_sequence=['PreSurvey', 'ZTS', 'PostSurvey'],
        news_condition='control',   
    ),
    dict(
        name='ZTS_pos_V1',
        display_name='ZTS Positive news frame',
        num_demo_participants=10,
        app_sequence=['PreSurvey', 'ZTS', 'PostSurvey'],
        news_condition='positive',  
    ),
    dict(
        name='ZTS_neg_V1',
        display_name='ZTS Negative news frame',
        num_demo_participants=10,
        app_sequence=['PreSurvey', 'ZTS', 'PostSurvey'],
        news_condition='negative',  
    ),
]

SESSION_FIELDS = ['num_rounds']
PARTICIPANT_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='zts_c',
        display_name='ZTS – group C',
        participant_label_file='_rooms/zts_control.txt',
    ),
    dict(
        name='zts_p',
        display_name='ZTS – group P',
        participant_label_file='_rooms/zts_treatment_pos.txt',
    ),
    dict(
        name='zts_n',
        display_name='ZTS – group N',
        participant_label_file='_rooms/zts_treatment_neg.txt',
    ),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
<b>Zurich Trading Simulator (ZTS)</b>
<p>A web-based behaviour experiment 
in the form of a trading game, designed by the Chair of Cognitive Science - ETH Zurich.</p>
"""

# Change this default secret key to a fully random one after forking.
SECRET_KEY = '1sjjosef4a7#)%cb3_us8%aa*l_d476lp&*hatrb6al*u*dude^'