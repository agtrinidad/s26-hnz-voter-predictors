full_features = [
    # Copy from naive
    'VoterAge',         # Age (derived: 2024 - birthyr)
    'gender4',          # Gender
    'educ',             # Education
    'race',             # Race
    'hispanic',         # Hispanic
    'pid3',             # 3 point party ID
    'inputstate',       # State of Residence
    'region',           # Region
    'student',          # Student Full or Part-time

    # Multiracial categories
    "multrace_1",       # Multiracial - White
    "multrace_2",       # Multiracial - Black
    "multrace_3",       # Multiracial - Hispanic
    "multrace_4",       # Multiracial - Asian
    "multrace_5",       # Multiracial - Native American
    "multrace_8",       # Multiracial - Middle Eastern
    "multrace_97",      # Multiracial - Other
    "multrace_98",      # Multiracial - Don't know

    # Device & Registration
    'votereg',          # Voter Registration Status

    # Other
    'pid7',             # 7 point Party ID
    'immstat',          # Immigration background

    # Media consumption (past 24 hrs) -- FE
    "CC24_300_1",       # Media use past 24 hrs - Used social media
    "CC24_300_2",       # Media use past 24 hrs - Watched TV news
    "CC24_300_3",       # Media use past 24 hrs - Read a newspaper
    "CC24_300_4",       # Media use past 24 hrs - Listened to radio news
    "CC24_300_5",       # Media use past 24 hrs - None of these

    # Social media use in relation to politics
    "CC24_300d_1",      # Recent social media use - Posted a story, photo, video or link about politics
    "CC24_300d_2",      # Recent social media use - Posted a comment about politics
    "CC24_300d_3",      # Recent social media use - Read a story or watched a video about politics
    "CC24_300d_4",      # Recent social media use - Followed a political event
    "CC24_300d_5",      # Recent social media use - Forwarded a story, photo, video or link about politics to friends
    "CC24_300d_6",      # Recent social media use - None of the above

    # Economic perceptions
    "CC24_301",         # National Economics
    "CC24_302",         # Household income change
    "CC24_303",         # Price change in past year

    # Life changes
    "CC24_305_1",       # Life Changes - Married
    "CC24_305_2",       # Life Changes - Lost a job
    "CC24_305_3",       # Life Changes - Finished school
    "CC24_305_4",       # Life Changes - Retired
    "CC24_305_5",       # Life Changes - Divorced
    "CC24_305_6",       # Life Changes - Had a child
    "CC24_305_7",       # Life Changes - Taken a new job
    "CC24_305_9",       # Life Changes - Been a victim of a crime
    "CC24_305_10",      # Life Changes - Visited an emergency room
    "CC24_305_11",      # Life Changes - Visited a doctor for a regular examination
    "CC24_305_12",      # Life Changes - Received a raise at work
    "CC24_305_13",      # Life Changes - Had a pay cut at work
    "CC24_305_14",      # Life Changes - None of the above

    # Health status
    "CC24_309e",        # General health

    # Emergency expenses
    "CC24_309d_1",      # Emergency expense - Put it on credit card, pay off in full
    "CC24_309d_2",      # Emergency expense - Put it on credit card, pay off over time
    "CC24_309d_3",      # Emergency expense - With checking/savings or cash
    "CC24_309d_4",      # Emergency expense - Bank loan or line of credit
    "CC24_309d_5",      # Emergency expense - Borrowing from friend or family
    "CC24_309d_6",      # Emergency expense - Payday loan, deposit advance, or overdraft
    "CC24_309d_7",      # Emergency expense - By selling something
    "CC24_309d_8",      # Emergency expense - Wouldn't be able to pay right now

    # Knowledge of current politicians
    "CC24_310a",        # Know Party in Government - U.S. House of Representatives
    "CC24_310b",        # Know Party in Government - U.S. Senate

    # Voting habits
    "CC24_363",         # Vote Intention

    # Miscellaneous
    "urbancity",        # Type of Area Living In
    "ideo5",            # Ideology
    "parent",           # Parent of child younger or older than 18
    "employ",           # Employment Status
    "stock",            # Stock ownership
    "newsint",          # Political Interest
    "faminc_new",       # Family income
    "marstat",          # Marital Status
    "union",            # Labor union member
    "ownhome",          # Home ownership
    "industry",         # Industry of employment
    "jobnum",           # Number of jobs
    "sexuality",        # Sexual Orientation
    "transgender",      # Transgender

    # Religious habit
    "pew_religimp",     # Importance of religion (Pew version)
    "religpew",         # Religion

    # Election habits
    "CC24_421_1",       # Election fair - Elections in the U.S. are fair
    "CC24_421_2",       # Election fair - State/local government conducted fair and accurate election in 2024
    "CC24_423",         # Trust in federal government
    "CC24_424",         # Trust in state government

    # Past year political engagement
    "CC24_430a_1",      # Past year - Attend local political meetings
    "CC24_430a_2",      # Past year - Put up a political sign
    "CC24_430a_3",      # Past year - Work for a candidate or campaign
    "CC24_430a_4",      # Past year - Attend a political protest, march or demonstration
    "CC24_430a_5",      # Past year - Contact a public official
    "CC24_430a_6",      # Past year - Donate money to a candidate, campaign, or political organization
    "CC24_430a_7",      # Past year - Donate blood
    "CC24_430a_8",      # Past year - None of these

    # Money donation
    "CC24_430b_1",      # Donate money - Candidate for President
    "CC24_430b_2",      # Donate money - Candidate for U.S. Senate in my state
    "CC24_430b_3",      # Donate money - Candidate for U.S. Senate in another state
    "CC24_430b_4",      # Donate money - Candidate for U.S. House in my state
    "CC24_430b_5",      # Donate money - Candidate for U.S. House in another state
    "CC24_430b_6",      # Donate money - Candidate for state office
    "CC24_430b_7",      # Donate money - Political party committee
    "CC24_430b_8",      # Donate money - Political action committee at work
    "CC24_430b_9",      # Donate money - Political group
    "CC24_430b_10",     # Donate money - Other
    "CC24_430c",        # Donate money - total amount

    # Campaign contact
    "CC24_431a",        # Contacted by candidate or political campaign

    # Other post-election
    "gunown",           # Personal gun ownership
    "numchildren",      # Number of children
    "gigwork",          # Gig work
    "edloan",           # Student debtor

    # Voting history
    "presvote20post",   # 2020 President Vote Post Election
    "presvote16post",   # 2016 President Vote Post Election
]