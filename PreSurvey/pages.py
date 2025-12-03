from otree.api import *
from .models import C, Subsession, Group, Player


class Demographics(Page):
    form_model = 'player'
    form_fields = [
        'sd1_residential_status',
        'sd2_gender',
        'sd3_age',
        'sd4_education',
        'sd5_employment_status',
        'sd6_household_size',
        'sd7_income',
        'sd8_marital_status',
    ]

class SelfAssessment(Page):
    form_model = 'player'
    form_fields = ['self_fl_knowledge']


class LiteracyBasic(Page):
    form_model = 'player'
    form_fields = [
        'big5_interest',
        'big5_inflation',
        'big5_diversification',
        'big5_mortgage',
        'big5_bonds',
    ]


class LiteracyAdvanced(Page):
    form_model = 'player'
    form_fields = [
        'adv_a1_beta',
        'adv_a2_sharpe',
        'adv_b1_spread',
        'adv_b2_market_order',
        'adv_c2_turnover_tax',
        'adv_d1_credit_score_payments',
    ]

class CRT(Page):
    form_model = 'player'
    form_fields = [
        'crt_coffee_muffin_mc',
        'crt_bakers_loaves_mc',
        'crt_online_rumor_mc',
        'crt_discount_then_tax_mc',
    ]

class RiskTolerance(Page):
    form_model = 'player'
    form_fields = [
        'frt_1_risk_taker',
        'frt_2_game_show',
        'frt_3_job_loss_vacation',
        'frt_5_unexpected_20000',
        'frt_6_comfort_stocks',
        'frt_8_word_risk',
        'frt_12_hard_assets',
        'frt_14_best_worst_case',
        'frt_16_sure_gain_vs_gamble',
        'frt_17_sure_loss_vs_gamble',
        'frt_18_inheritance_100k',
        'frt_19_allocate_20000',
        'frt_20_gold_venture',
    ]


page_sequence = [
    Demographics,
    SelfAssessment,
    LiteracyBasic,
    LiteracyAdvanced,
    CRT,
    RiskTolerance,
]
