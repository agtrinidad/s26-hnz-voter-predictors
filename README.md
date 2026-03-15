# Who Voted?: *Applying Classification Methods to Voter Turnout*
### Contributors: Gavin Loyd, Cierra Oliviera, Avery Trinidad
### Originally Published: March 15, 2026
### Course: 90803-B: Machine Learning Foundations with Python
---
## Executive Summary
### Objective
Using 2024 data gathered by the Cooperative Election Study (CCES), this project aims to identify predictive attributes for United States nonparticipant eligible voters and participant voters.

### Background & Organizational Relevance
Since the turn of the millennium, less than 65% of eligible American adults have participated in each presidential election on average. Though voter participation has trended upwards over time (achieving an estimated 63.1% in 2024 compared to 54.3% in 2000), unengaged but eligible voters have long remained an object of concern for politicians, policy analysts, and social advocacy practitioners alike. Stakeholders commonly seek to increase this turnout.

If interested organizations were able to identify which individual factors were associated with historically lower voter turnout (or better yet, which factors led to nonparticipation), they would then be able to produce targeted campaigns to augment voter engagement. Rather than blanket calls for “civic responsibility,” stakeholders could strategically target their resources.

### Data Source & Profile
This project’s data originates from the Cooperative Election Study (CCES), “a 50,000+ person national stratified sample survey” administered by UK-headquartered research firm YouGov. Formerly referred to as the “Cooperative Congressional Election Study,” the study engages with an identical set of respondents at both pre-election and post-election stages each federal voting cycle. Though records from the study date back to 2006, we use data drawn from the most recent federal election in 2024, hosted by Harvard University within its “Harvard Dataverse.”

The original dataset provided in “CCES24_Common_OUTPUT_vv_topost_final.csv” contains 60000 records with a total of 694 attributes (not including their index). While many of these cells are blank, the set is still 175.2 MB in its CSV form. Because GitHub does not support hosting individual files of over 100 MB in size, this file was subdivided into 8 CSVs of approximately ~23 MB each in our repository. We recombine these parts as part of our cleaning process.

### Methodology
Records were cast as nonvoters (0) and voters (1), framing the objective as a binary classification problem. Focusing only on records capable of definite classification, the publicly available XGBoost, scikit-learn Naive Bayes Classifier, and CatBoost were trained in consideration of both nonvoter and voter classes. SHAP was then used as a model-agnostic method to identify which features were deemed most important as a matter of consensus between both models and their trained instantiations.

### Interpretation of Results
There was strong cross-model agreement on the most predictive signals for voter turnout. Five features appear across all three models: “newsint” (political interest), “pres20” (2020 election vote history), “CC24_421_2” (belief that elections in respondent municipality are fair), “investor” (stock market participation), and “marstat” (marital status). This level of agreement across the three different models provides high confidence that these are genuine predictors of turnout. Political and civic engagement formed another cluster of agreement. Specifically, political knowledge (“CC24_310a” and “CC24_310b”) and civic engagement (“past_year_civic”, “CC24_431a”) indicators are identified as important predictors in at least two of the three models. Overall, the presence of prior voting and measures of attentiveness to politics appear consistently important, suggesting that political interest plays a key role in distinguishing voters from non-voters. 

Additionally, there is some convergence on indicators of socioeconomic stability and civic integration, including marital status (“marstat”), home ownership (“ownhom”), and investment in the stock market (“investor”). These variables capture broader patterns of economic resources or social attachment that are associated with political participation. 


### Findings
Records were cast as nonvoters (0) and voters (1), framing the objective as a binary classification problem. Focusing only on records capable of definite classification, the publicly available XGBoost, scikit-learn Naive Bayes Classifier, and CatBoost were trained in consideration of both nonvoter and voter classes. SHAP was then used as a model-agnostic method to identify which features were deemed most important as a matter of consensus between both models and their trained instantiations.
