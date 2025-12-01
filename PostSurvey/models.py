from otree.api import *


doc = """
Post-treatment survey:
- Financial literacy (Big Five + 9 advanced items)
- Financial risk tolerance (13 Grable & Lytton items)
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
    # Part I: Self-assessment
    # Self-assessment of financial knowledge (1–7 scale)
    # ----------------------------
    self_fl_knowledge = models.IntegerField(
        label=(
            "On a scale from 1 to 7, where 1 means very low and 7 means very high, "
            "how would you assess your overall financial knowledge?"
        ),
        choices=[[i, str(i)] for i in range(1, 8)],
        widget=widgets.RadioSelect,
    )

    # ----------------------------
    # Part II: Financial literacy
    # Big Five (based on C2–C6) + 9 advanced
    # ----------------------------

    # Big Five core items (Romanian questionnaire C2–C6) :contentReference[oaicite:0]{index=0}

    fl_q1_c2_compound_interest = models.IntegerField(
        label=(
            "Suppose you had LEI 100 in a savings account and the interest rate "
            "was 10 percent per year. After 5 years, how much would you have if "
            "you left the money to grow?"
        ),
        choices=[
            [1, "More than LEI 150"],
            [2, "Exactly LEI 150"],
            [3, "Less than LEI 150"],
            [0, "Don’t know"],
        ],
    )

    fl_q2_c3_mortgage_term = models.IntegerField(
        label=(
            "True or false: A 15-year mortgage typically requires higher monthly "
            "payments than a 30-year mortgage, but the total interest paid is less."
        ),
        choices=[
            [1, "True"],
            [2, "False"],
            [0, "Don’t know"],
        ],
    )

    fl_q3_c4_time_value_inheritance = models.IntegerField(
        label=(
            "Assume a friend inherits LEI 50,000 today and their sibling "
            "inherits LEI 50,000 three years from now. Who is richer because of the inheritance?"
        ),
        choices=[
            [1, "They are equally rich"],
            [2, "My friend"],
            [3, "The sibling"],
            [0, "Don’t know"],
        ],
    )

    fl_q4_c5_inflation_real_income = models.IntegerField(
        label=(
            "Suppose over the next 10 years the prices of things you buy double. "
            "If your income also doubles, will you be able to buy less, the same, "
            "or more than today?"
        ),
        choices=[
            [1, "More"],
            [2, "Less"],
            [3, "The same"],
            [0, "Don’t know"],
        ],
    )

    fl_q5_c6_diversification = models.IntegerField(
        label=(
            "Suppose you have some money. Is it safer to put your money into one "
            "business/investment or into multiple businesses/investments?"
        ),
        choices=[
            [1, "One business or investment"],
            [2, "Multiple businesses or investments"],
            [0, "Don’t know"],
        ],
    )

    # 9 advanced literacy items (you can tweak wording later if needed)

    adv_fl_q1_emergency_fund = models.IntegerField(
        label=(
            "A good rule of thumb for an emergency fund is to cover how many months "
            "of essential expenses?"
        ),
        choices=[
            [1, "1 month"],
            [2, "3–6 months"],
            [3, "12 months"],
            [4, "It is not necessary to have an emergency fund"],
            [0, "Don’t know"],
        ],
    )

    adv_fl_q2_inflation_bond = models.IntegerField(
        label=(
            "If inflation rises unexpectedly, what generally happens to the price "
            "of a fixed-rate bond you already hold?"
        ),
        choices=[
            [1, "It increases"],
            [2, "It stays exactly the same"],
            [3, "It decreases"],
            [4, "There is no systematic relation"],
            [0, "Don’t know"],
        ],
    )

    adv_fl_q3_index_fund = models.IntegerField(
        label=(
            "Compared to a low-cost index fund, an actively managed mutual fund "
            "with higher fees will, on average over the long run:"
        ),
        choices=[
            [1, "Deliver higher returns after fees"],
            [2, "Deliver similar or lower returns after fees"],
            [3, "Eliminate investment risk"],
            [4, "Guarantee positive returns"],
            [0, "Don’t know"],
        ],
    )

    adv_fl_q4_diversification_correlation = models.IntegerField(
        label=(
            "Diversification is most effective when the assets in the portfolio are:"
        ),
        choices=[
            [1, "Highly positively correlated"],
            [2, "Uncorrelated or weakly correlated"],
            [3, "Perfectly correlated"],
            [4, "Always from the same sector"],
            [0, "Don’t know"],
        ],
    )

    adv_fl_q5_leverage = models.IntegerField(
        label=(
            "Taking a loan to invest in risky assets (using leverage) generally:"
        ),
        choices=[
            [1, "Increases both potential gains and potential losses"],
            [2, "Increases gains and reduces losses"],
            [3, "Reduces both gains and losses"],
            [4, "Eliminates risk"],
            [0, "Don’t know"],
        ],
    )

    adv_fl_q6_real_vs_nominal = models.IntegerField(
        label=(
            "If your investment returns 5% and inflation is 3%, your approximate "
            "real (inflation-adjusted) return is:"
        ),
        choices=[
            [1, "2%"],
            [2, "5%"],
            [3, "8%"],
            [4, "−2%"],
            [0, "Don’t know"],
        ],
    )

    adv_fl_q7_risk_return_tradeoff = models.IntegerField(
        label="In financial markets, higher expected returns are usually associated with:",
        choices=[
            [1, "Higher risk"],
            [2, "Lower risk"],
            [3, "Exactly the same risk"],
            [4, "No relation between risk and return"],
            [0, "Don’t know"],
        ],
    )

    adv_fl_q8_loss_aversion = models.IntegerField(
        label=(
            "Loss aversion describes the tendency of investors to:"
        ),
        choices=[
            [1, "Prefer a sure gain over a risky gain with the same expected value"],
            [2, "Dislike losses more than they like equivalent gains"],
            [3, "Always choose the riskiest asset"],
            [4, "Ignore past outcomes when deciding"],
            [0, "Don’t know"],
        ],
    )

    adv_fl_q9_overtrading = models.IntegerField(
        label=(
            "Empirical evidence on individual investors’ trading suggests that very "
            "frequent trading tends to:"
        ),
        choices=[
            [1, "Improve risk-adjusted performance after costs"],
            [2, "Reduce risk-adjusted performance after costs"],
            [3, "Have no effect on performance"],
            [4, "Completely eliminate risk"],
            [0, "Don’t know"],
        ],
    )

    # ----------------------------
    # Part III: Risk tolerance
    # 13 items from Grable & Lytton (1999) 
    # We implement the commonly used 13-item short form.
    # ----------------------------

    rt_q1_best_friend = models.IntegerField(
        label="In general, how would your best friend describe you as a risk taker?",
        choices=[
            [1, "A real gambler"],
            [2, "Willing to take risks after doing research"],
            [3, "Cautious"],
            [4, "A real risk avoider"],
        ],
    )

    rt_q2_game_show = models.IntegerField(
        label="You are on a TV game show and can choose one of the following. Which would you take?",
        choices=[
            [1, "$1,000 in cash"],
            [2, "A 50% chance at winning $5,000"],
            [3, "A 25% chance at winning $10,000"],
            [4, "A 5% chance at winning $100,000"],
        ],
    )

    rt_q3_vacation = models.IntegerField(
        label=(
            "You have saved for a ‘once-in-a-lifetime’ vacation. Three weeks before "
            "you plan to leave, you lose your job. You would:"
        ),
        choices=[
            [1, "Cancel the vacation"],
            [2, "Take a much more modest vacation"],
            [3, "Go as scheduled"],
            [4, "Extend the vacation and go first-class"],
        ],
    )

    rt_q4_invest_20000 = models.IntegerField(
        label="If you unexpectedly received $20,000 to invest, what would you do?",
        choices=[
            [1, "Deposit it in a bank / money market / insured CD"],
            [2, "Invest in safe high-quality bonds or bond funds"],
            [3, "Invest in stocks or stock mutual funds"],
        ],
    )

    rt_q5_stock_experience = models.IntegerField(
        label="How comfortable are you investing in stocks or stock mutual funds?",
        choices=[
            [1, "Not at all comfortable"],
            [2, "Somewhat comfortable"],
            [3, "Very comfortable"],
        ],
    )

    rt_q6_risk_word = models.IntegerField(
        label="When you think of the word ‘risk’, which word comes to mind first?",
        choices=[
            [1, "Loss"],
            [2, "Uncertainty"],
            [3, "Opportunity"],
            [4, "Thrill"],
        ],
    )

    rt_q7_keep_bonds_or_switch = models.IntegerField(
        label=(
            "Most of your investments are in high-interest government bonds. "
            "Experts expect hard assets (e.g., gold, real estate) to rise in price. "
            "What would you do?"
        ),
        choices=[
            [1, "Hold the bonds"],
            [2, "Sell some bonds and put half into hard assets"],
            [3, "Sell the bonds and put all into hard assets"],
            [4, "Sell, put all into hard assets, and borrow to buy more"],
        ],
    )

    rt_q8_house_purchase = models.IntegerField(
        label="When buying a home in the next few weeks, your strategy would be to:",
        choices=[
            [1, "Buy an affordable house with comfortable payments"],
            [2, "Stretch a bit for the house you really want"],
            [3, "Buy the most expensive house you can qualify for"],
            [4, "Borrow from friends/relatives to afford an even bigger mortgage"],
        ],
    )

    rt_q9_invest_100k = models.IntegerField(
        label="A relative leaves you $100,000 to invest in ONE of the following. Which do you choose?",
        choices=[
            [1, "Savings account or money market fund"],
            [2, "Mutual fund with both stocks and bonds"],
            [3, "Portfolio of common stocks"],
            [4, "Commodities like gold, silver, oil"],
        ],
    )

    rt_q10_portfolio_mix_20000 = models.IntegerField(
        label="If you had to invest $20,000, which portfolio mix is most appealing?",
        choices=[
            [1, "60% low-risk, 30% medium-risk, 10% high-risk"],
            [2, "30% low-risk, 40% medium-risk, 30% high-risk"],
            [3, "10% low-risk, 40% medium-risk, 50% high-risk"],
        ],
    )

    rt_q11_sure_gain = models.IntegerField(
        label=(
            "In addition to what you own, you are given $1,000. "
            "You must choose between:"
        ),
        choices=[
            [1, "A sure gain of $500"],
            [2, "A 50% chance to gain $1,000 and a 50% chance to gain nothing"],
        ],
    )

    rt_q12_sure_loss = models.IntegerField(
        label=(
            "In addition to what you own, you are given $2,000. "
            "You must choose between:"
        ),
        choices=[
            [1, "A sure loss of $500"],
            [2, "A 50% chance to lose $1,000 and a 50% chance to lose nothing"],
        ],
    )

    rt_q13_gold_venture = models.IntegerField(
        label=(
            "A trusted friend (an experienced geologist) is raising money for a "
            "high-risk gold mining venture. The chance of success is about 20%. "
            "If you had the money, how much would you invest?"
        ),
        choices=[
            [1, "Nothing"],
            [2, "A small amount that you could afford to lose"],
            [3, "A significant amount but less than half of your savings"],
            [4, "A large amount, including borrowing to invest more"],
        ],
    )

