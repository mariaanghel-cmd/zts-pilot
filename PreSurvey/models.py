from otree.api import *


doc = """
Pre-treatment survey:
- Sociodemographic variables (SD1–SD8)
- Financial literacy (Big Five + 9 advanced items)
- Financial risk tolerance (13 Grable & Lytton items)
"""


class C(BaseConstants):
    NAME_IN_URL = 'PreSurvey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # ----------------------------
    # Part I: Sociodemographic (SD1–SD8)
    # ----------------------------

    sd1_residential_status = models.IntegerField(
        label="Please indicate your residential status:",
        choices=[
            [1, "Urban area, with over 100,000 people"],
            [2, "Urban area, with 30,000 to about 100,000 people"],
            [3, "Urban area, with fewer than 30,000 people"],
            [4, "Rural area"],
        ],
    )

    sd2_gender = models.IntegerField(
        label="Gender:",
        choices=[
            [1, "Male"],
            [2, "Female"],
        ],
    )

    sd3_age = models.IntegerField(
        label="What is your age (completed years)?",
        min=18,
        max=100,
    )

    sd4_education = models.IntegerField(
        label="What is your highest educational attainment?",
        choices=[
            [1, "Primary school (4 grades)"],
            [2, "Middle school (8 grades)"],
            [3, "High school (12 grades)"],
            [4, "Bachelor and/or Master education"],
            [5, "Post-graduate education"],
        ],
    )

    sd5_employment_status = models.IntegerField(
        label="What is your current employment status?",
        choices=[
            [1, "Student / pupil"],
            [2, "Employee"],
            [3, "Self-employed"],
            [4, "Retired"],
            [5, "Not working"],
        ],
    )

    sd6_household_size = models.IntegerField(
        label="How many persons, including yourself, live permanently in your household?",
        choices=[
            [1, "1 person"],
            [2, "2 persons"],
            [3, "3 persons"],
            [4, "4 or more persons"],
        ],
    )

    sd7_income = models.IntegerField(
        label="What is your monthly income after taxes?",
        choices=[
            [1, "< LEI 1,500 (approx. < EUR 300)"],
            [2, "LEI 1,501 – 3,500 (approx. EUR 301–700)"],
            [3, "LEI 3,501 – 5,500 (approx. EUR 701–1,100)"],
            [4, "LEI 5,501 – 9,000 (approx. EUR 1,101–1,800)"],
            [5, "> LEI 9,001 (approx. > EUR 1,801)"],
        ],
    )

    sd8_marital_status = models.IntegerField(
        label="Please indicate your marital status:",
        choices=[
            [1, "Single"],
            [2, "Married"],
            [3, "Divorced"],
            [4, "Consensual union"],
            [5, "Widowed"],
        ],
    )

    # ----------------------------
    # Part II: Self-assessment
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
    # Part III: Financial literacy
    # Big Five (based on C2–C6) + 9 advanced
    # ----------------------------

    # Big Five core items (Romanian questionnaire C2–C6) :contentReference[oaicite:0]{index=0}

    # GFLEC “Big Five” financial literacy questions (Lusardi & Mitchell)
    # Source: https://gflec.org/education/questions-that-indicate-financial-literacy/ 

    big5_interest = models.IntegerField(
        label=(
            "Suppose you had $100 in a savings account and the interest rate was 2% per year. "
            "After 5 years, how much do you think you would have in the account if you left the money to grow?"
        ),
        choices=[
            [1, "More than $102"],
            [2, "Exactly $102"],
            [3, "Less than $102"],
            [0, "Don't know"],
        ],
    )

    big5_inflation = models.IntegerField(
        label=(
            "Imagine that the interest rate on your savings account was 1% per year and inflation was 2% per year. "
            "After 1 year, with the money in this account, would you be able to buy..."
        ),
        choices=[
            [1, "More than today"],
            [2, "Exactly the same as today"],
            [3, "Less than today"],
            [0, "Don't know"],
        ],
    )

    big5_diversification = models.IntegerField(
        label="Buying a single company’s stock usually provides a safer return than a stock mutual fund.",
        choices=[
            [1, "True"],
            [2, "False"],
            [0, "Don't know"],
        ],
    )

    big5_mortgage = models.IntegerField(
        label=(
            "A 15-year mortgage typically requires higher monthly payments than a 30-year mortgage, "
            "but the total interest paid over the life of the loan will be less."
        ),
        choices=[
            [1, "True"],
            [2, "False"],
            [0, "Don't know"],
        ],
    )

    big5_bonds = models.IntegerField(
        label="If interest rates rise, what will typically happen to bond prices?",
        choices=[
            [1, "They will rise"],
            [2, "They will fall"],
            [3, "They will stay the same"],
            [4, "There is no relationship between bond prices and the interest rate"],
            [0, "Don't know"],
        ],
    )


    # 8 advanced literacy items (you can tweak wording later if needed)

    # --- Advanced financial literacy questions (A-1 to D-2), multiple choice ---

    adv_a1_beta = models.IntegerField(
        label="A portfolio with a beta of 1.5 is best described as:",
        choices=[
            [1, "Less volatile than the market in all situations"],
            [2, "More sensitive to market movements than the market"],
            [3, "Guaranteed to earn 1.5× the market return"],
            [4, "Unrelated to market risk"],
            [0, "Don’t know"]
        ],
    )

    adv_a2_sharpe = models.IntegerField(
        label=(
            "If a fund has had high returns with even higher volatility, "
            "the metric most directly designed to compare “return per unit of risk” is:"
        ),
        choices=[
            [1, "Sharpe ratio"],
            [2, "Price-to-earnings ratio"],
            [3, "Dividend yield"],
            [4, "Book value"],
            [0, "Don’t know"]
        ],
    )

    adv_b1_spread = models.IntegerField(
        label="The bid–ask spread is best interpreted as:",
        choices=[
            [1, "A tax paid to the government"],
            [2, "A measure of inflation"],
            [3, "A trading cost related to liquidity and market-making"],
            [4, "The dividend a stock pays"],
            [0, "Don’t know"]
        ],
    )

    adv_b2_market_order = models.IntegerField(
        label="A market order (vs a limit order) mainly increases the risk of:",
        choices=[
            [1, "Not executing at all"],
            [2, "Executing at an unexpectedly bad price in fast markets"],
            [3, "Paying any commission"],
            [4, "Being forced to hold the asset for years"],
            [0, "Don’t know"]
        ],
    )

    adv_c2_turnover_tax = models.IntegerField(
        label=(
            "Compared with long-term investing, high turnover in a taxable account tends to:"
        ),
        choices=[
            [1, "Increase after-tax returns by default"],
            [2, "Reduce after-tax returns due to taxes and costs"],
            [3, "Eliminate risk"],
            [4, "Make performance easier to predict"],
            [0, "Don’t know"]
        ],
    )

    adv_d1_credit_score_payments = models.IntegerField(
        label="The factor most consistently associated with stronger credit scores is:",
        choices=[
            [1, "Applying for many new loans quickly"],
            [2, "Making payments on time"],
            [3, "Closing old credit accounts"],
            [4, "Having the highest possible credit limit and using it fully"],
            [0, "Don’t know"]
        ],
    )


    # ----------------------------
    # Part IV: CRT
    # Self-assessment of financial knowledge (1–7 scale)
    # ----------------------------

    # --- CRT rephrasings (selected) — all multiple choice ---

    crt_coffee_muffin_mc = models.IntegerField(
        label=(
            "A coffee and a muffin cost $6.30 in total. "
            "The coffee costs $5.50 more than the muffin. "
            "How much does the muffin cost?"
        ),
        choices=[
            [1, "$0.40"],
            [2, "$0.80"],
            [3, "$1.30"],
            [4, "$1.10"],
            [5, "$0.55"],
            [0, "Don’t know"]
        ],
    )

    crt_bakers_loaves_mc = models.IntegerField(
        label=(
            "If 4 bakers make 4 trays of rolls in 10 minutes, "
            "how long would it take 40 bakers to make 40 trays?"
        ),
        choices=[
            [1, "1 minute"],
            [2, "10 minutes"],
            [3, "40 minutes"],
            [4, "100 minutes"],
            [5, "25 minutes"],
            [0, "Don’t know"]
        ],
    )

    crt_online_rumor_mc = models.IntegerField(
        label=(
            "The number of people who have seen a video doubles each hour. "
            "It takes 20 hours to reach everyone in the target group. "
            "After how many hours had half the group seen it?"
        ),
        choices=[
            [1, "10 hours"],
            [2, "19 hours"], 
            [3, "18 hours"],
            [4, "20 hours"],
            [5, "15 hours"],
            [0, "Don’t know"]
        ],
    )

    crt_discount_then_tax_mc = models.IntegerField(
        label=(
            "A jacket is discounted by 20%, then a 20% sales tax is applied "
            "to the discounted price. Is the final price lower than, equal to, "
            "or higher than the original price?"
        ),
        choices=[
            [1, "Lower than the original price"],  # correct
            [2, "Equal to the original price"],
            [3, "Higher than the original price"],
            [4, "Cannot be determined without the original price"],
            [0, "Don’t know"]
        ],
    )

    # ----------------------------
    # Part IV: Risk tolerance
    # 13 items from Grable & Lytton (1999) 
    # We implement the commonly used 13-item short form.
    # ----------------------------

    # 13-item Financial Risk Tolerance instrument (Grable & Lytton, 1999)
    # Items retained after factor analysis: 1,2,3,5,6,8,12,14,16,17,18,19,20. :contentReference[oaicite:0]{index=0}
    # Response scoring weights are shown in the paper’s Table 1 “Scoring” section. :contentReference[oaicite:1]{index=1}

    frt_1_risk_taker = models.IntegerField(
        label="In general, how would your best friend describe you as a risk taker?",
        choices=[
            [1, "A real gambler"],  # scored 4 :contentReference[oaicite:2]{index=2}
            [2, "Willing to take risks after completing adequate research"],  # scored 3
            [3, "Cautious"],  # scored 2
            [4, "A real risk avoider"],  # scored 1
        ],
    )

    frt_2_game_show = models.IntegerField(
        label="You are on a TV game show and can choose one of the following. Which would you take?",
        choices=[
            [1, "$1,000 in cash"],  # scored 1 :contentReference[oaicite:3]{index=3}
            [2, "A 50% chance at winning $5,000"],  # scored 2
            [3, "A 25% chance at winning $10,000"],  # scored 3
            [4, "A 5% chance at winning $100,000"],  # scored 4
        ],
    )

    frt_3_job_loss_vacation = models.IntegerField(
        label=(
            "You have just finished saving for a “once-in-a-lifetime” vacation. "
            "Three weeks before you plan to leave, you lose your job. You would:"
        ),
        choices=[
            [1, "Cancel the vacation"],  # scored 1 :contentReference[oaicite:4]{index=4}
            [2, "Take a much more modest vacation"],  # scored 2
            [3, "Go as scheduled, reasoning that you need the time to prepare for a job search"],  # scored 3
            [4, "Extend your vacation, because this might be your last chance to go first-class"],  # scored 4
        ],
    )

    frt_5_unexpected_20000 = models.IntegerField(
        label="If you unexpectedly received $20,000 to invest, what would you do?",
        choices=[
            [1, "Deposit it in a bank account, money market account, or an insured CD"],  # scored 1 :contentReference[oaicite:5]{index=5}
            [2, "Invest it in safe high quality bonds or bond mutual funds"],  # scored 2
            [3, "Invest it in stocks or stock mutual funds"],  # scored 3
        ],
    )

    frt_6_comfort_stocks = models.IntegerField(
        label="In terms of experience, how comfortable are you investing in stocks or stock mutual funds?",
        choices=[
            [1, "Not at all comfortable"],  # scored 1 :contentReference[oaicite:6]{index=6}
            [2, "Somewhat comfortable"],  # scored 2
            [3, "Very comfortable"],  # scored 3
        ],
    )

    frt_8_word_risk = models.IntegerField(
        label="When you think of the word “risk” which of the following words comes to mind first?",
        choices=[
            [1, "Loss"],  # scored 1 :contentReference[oaicite:7]{index=7}
            [2, "Uncertainty"],  # scored 2
            [3, "Opportunity"],  # scored 3
            [4, "Thrill"],  # scored 4
        ],
    )

    frt_12_hard_assets = models.IntegerField(
        label=(
            "Some experts are predicting prices of assets such as gold, jewels, collectibles, and real estate "
            "(hard assets) to increase in value; bond prices may fall, however, experts tend to agree that "
            "government bonds are relatively safe. Most of your investment assets are now in high interest "
            "government bonds. What would you do?"
        ),
        choices=[
            [1, "Hold the bonds"],  # scored 1 :contentReference[oaicite:8]{index=8}
            [2, "Sell the bonds, put half the proceeds into money market accounts, and the other half into hard assets"],  # scored 2
            [3, "Sell the bonds and put the total proceeds into hard assets"],  # scored 3
            [4, "Sell the bonds, put all the money into hard assets, and borrow additional money to buy more"],  # scored 4
        ],
    )

    frt_14_best_worst_case = models.IntegerField(
        label=(
            "Given the best and worst case returns of the four investment choices below, which would you prefer?"
        ),
        choices=[
            [1, "$200 gain best case; $0 gain/loss worst case"],  # scored 1 :contentReference[oaicite:9]{index=9}
            [2, "$800 gain best case; $200 loss worst case"],  # scored 2
            [3, "$2,600 gain best case; $800 loss worst case"],  # scored 3
            [4, "$4,800 gain best case; $2,400 loss worst case"],  # scored 4
        ],
    )

    frt_16_sure_gain_vs_gamble = models.IntegerField(
        label=(
            "In addition to whatever you own, you have been given $1,000. You are now asked to choose between:"
        ),
        choices=[
            [1, "A sure gain of $500"],  # scored 1 :contentReference[oaicite:10]{index=10}
            [2, "A 50% chance to gain $1,000 and a 50% chance to gain nothing"],  # scored 3
        ],
    )

    frt_17_sure_loss_vs_gamble = models.IntegerField(
        label=(
            "In addition to whatever you own, you have been given $2,000. You are now asked to choose between:"
        ),
        choices=[
            [1, "A sure loss of $500"],  # scored 1 :contentReference[oaicite:11]{index=11}
            [2, "A 50% chance to lose $1,000 and a 50% chance to lose nothing"],  # scored 3
        ],
    )

    frt_18_inheritance_100k = models.IntegerField(
        label=(
            "Suppose a relative left you an inheritance of $100,000, stipulating in the will that you invest ALL "
            "the money in ONE of the following choices. Which one would you select?"
        ),
        choices=[
            [1, "A savings account or money market mutual fund"],  # scored 1 :contentReference[oaicite:12]{index=12}
            [2, "A mutual fund that owns stocks and bonds"],  # scored 2
            [3, "A portfolio of 15 common stocks"],  # scored 3
            [4, "Commodities like gold, silver, and oil"],  # scored 4
        ],
    )

    frt_19_allocate_20000 = models.IntegerField(
        label="If you had to invest $20,000, which of the following investment choices would you find most appealing?",
        choices=[
            [1, "60% in low-risk investments, 30% in medium-risk investments, 10% in high-risk investments"],  # scored 1 :contentReference[oaicite:13]{index=13}
            [2, "30% in low-risk investments, 40% in medium-risk investments, 30% in high-risk investments"],  # scored 2
            [3, "10% in low-risk investments, 40% in medium-risk investments, 50% in high-risk investments"],  # scored 3
        ],
    )

    frt_20_gold_venture = models.IntegerField(
        label=(
            "Your trusted friend and neighbor, an experienced geologist, is putting together a group of investors "
            "to fund an exploratory gold mining venture. The venture could pay back 50 to 100 times the investment "
            "if successful. If the mine is a bust, the entire investment is worthless. Your friend estimates the chance "
            "of success is only 20%. If you had the money, how much would you invest?"
        ),
        choices=[
            [1, "Nothing"],  # scored 1 :contentReference[oaicite:14]{index=14}
            [2, "One month’s salary"],  # scored 2
            [3, "Three month’s salary"],  # scored 3
            [4, "Six month’s salary"],  # scored 4
        ],
    )


