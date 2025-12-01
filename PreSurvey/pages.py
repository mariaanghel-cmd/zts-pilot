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
        'fl_q1_c2_compound_interest',
        'fl_q2_c3_mortgage_term',
        'fl_q3_c4_time_value_inheritance',
        'fl_q4_c5_inflation_real_income',
        'fl_q5_c6_diversification',
    ]


class LiteracyAdvanced(Page):
    form_model = 'player'
    form_fields = [
        'adv_fl_q1_emergency_fund',
        'adv_fl_q2_inflation_bond',
        'adv_fl_q3_index_fund',
        'adv_fl_q4_diversification_correlation',
        'adv_fl_q5_leverage',
        'adv_fl_q6_real_vs_nominal',
        'adv_fl_q7_risk_return_tradeoff',
        'adv_fl_q8_loss_aversion',
        'adv_fl_q9_overtrading',
    ]


class RiskTolerance(Page):
    form_model = 'player'
    form_fields = [
        'rt_q1_best_friend',
        'rt_q2_game_show',
        'rt_q3_vacation',
        'rt_q4_invest_20000',
        'rt_q5_stock_experience',
        'rt_q6_risk_word',
        'rt_q7_keep_bonds_or_switch',
        'rt_q8_house_purchase',
        'rt_q9_invest_100k',
        'rt_q10_portfolio_mix_20000',
        'rt_q11_sure_gain',
        'rt_q12_sure_loss',
        'rt_q13_gold_venture',
    ]


page_sequence = [
    Demographics,
    SelfAssessment,
    LiteracyBasic,
    LiteracyAdvanced,
    RiskTolerance,
]
