######################################################
# AB Testing
######################################################

# AB Testing
# - Independent Two-Sample T-Test
#       - Parametric Comparison
#       - Nonarametric Comparison
# - Two Sample Ratio Test
# - Mean Comparison of More than Two Groups. (ANOVA)


# ############## Business Problem ###########
# Facebook recently made an offer called maximum bidding.
# a new bid type, average bidding, as an alternative to the bidding type introduced.
# One of our customers, bombabomba.com is testing this new feature.
# He decided to try and find that averagebidding is better than maximumbidding.
# do an A/B test to see if it converts too much
# wants.
#############################################

# ############## Dataset Story ##############
# In this dataset, which contains the website information of bombabomba.com,
# information of user are number of ads they saw and clicked on, purchase frequency.
# There are two separate data sets, the control and test groups.
#############################################

# ############## Variables #################
# Impression – Ad views
# Click – Clicks >> Indicates the number of clicks on the displayed ad.
# Purchase  >> Indicates the number of products purchased after the ads clicked.
# Earning – Earning  >> Earnings after purchased products

############################################
# Data Preprocessing
############################################

import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, pearsonr, spearmanr, kendalltau, \
    f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

############################
# Hypothesis
############################
# Is there any statistically significant difference between Maximum Bidding and Average Bidding ?

# H0: There is no statistically significant difference between Maximum Bidding and Average Bidding
# H1: There is a statistically significant difference between Maximum Bidding and Average Bidding

############################
# Let's get the dataset
############################

# Maximum Bidding
control = pd.read_excel("hafta_5/ab_testing.xlsx", sheet_name="Control Group")
control.head()
control.isnull().sum()
control.info()

# Average Bidding
test = pd.read_excel("hafta_5/ab_testing.xlsx", sheet_name="Test Group")
test.head()
test.isnull().sum()
test.info()

# quick look at the mean and median values of datasets
control["Click"].describe().T
test["Click"].describe().T

############################
# Assumption Control
############################

# 1. Normality Assumption
# 2. Variance Homogeneity Assumption

############################
# Normality Assumption (Shapiro Test)
############################

# H0: Normal distribution assumption is provided.
# H1: .... not provided.
# p-value < 0.05 >> HO provided.
# not p-value < 0.05  >> H0 not provided.

test_stat, pvalue = shapiro(control["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# H0 hypothesis could not be rejected because pvalue = 0.5891 > 0.05.
# We see that the data in the control group has a normal distribution.
# Because 0.05 is not greater than p value.

test_stat, pvalue = shapiro(control["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# H0 hypothesis could not be rejected because pvalue = 0.1541 > 0.05.
# We see that the data in the test group has a normal distribution.
# Because 0.05 is not greater than p value.

############################
# Variance Homogeneity Assumption (Levene Test)
############################

# H0: Variances are homogeneous.
# H1: Variances are not homogeneous.
# p-value < 0.05 >> HO provided.
# not p-value < 0.05  >> H0 not provided.

test_stat, pvalue = levene(final_["control"], final_["test"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# H0 hypothesis could be rejected because pvalue = 0.1083 > 0.05.
# We see that the data in the test and control group have variances homogeneous.
# Because 0.05 is not greater than p value.

############################
# Parametric Independent Two-Sample T Test ()
############################

# H0: There is no statistically significant difference between Maximum Bidding and Average Bidding
# H1: There is a statistically significant difference between Maximum Bidding and Average Bidding

# p-value < 0.05 >> HO provided.
# not p-value < 0.05  >> H0 not provided.

test_stat, pvalue = ttest_ind(control["Purchase"], test["Purchase"], equal_var=True)
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# H0 hypothesis could be rejected because pvalue = 0.3493 > 0.05.
# There is no statistically significant difference between Maximum Bidding and Average Bidding
# Because 0.05 is not greater than p value.

############################
# for task questions
############################

# 1. Define the hypothesis of the A/B test.
"""
    Is there any statistically significant difference between Maximum Bidding and Average Bidding ?
        # H0: There is no statistically significant difference between Maximum Bidding and Average Bidding
        # H1: There is a statistically significant difference between Maximum Bidding and Average Bidding
"""

# 2. Statistically, the test results, it is statistically significant or not.
"""
    After calculating the normality and homogeneity of variance, I decided to perform the 
    Parametric Independent Two-Sample T-Test. Since the pvalue is greater than 0.05 in the last test, 
    I observed that there is no statistically significant difference between the purchases made with 
    the Maximum Bidding and Average Bidding methods.
"""
# 3. Which tests did you use? Specify your reasons.
"""
     AB Testing
 - Independent Two-Sample T-Test
       - Parametric Comparison
       - Nonarametric Comparison
 - Two Sample Ratio Test
 - Mean Comparison of More than Two Groups. (ANOVA)
 
    Based on the information above; Previously, I observed the results of the hypotheses regarding
    homogeneity of variance and normality assumptions. After that; Since the p value was greater than 0.05,
     h0 could not be rejected and an independent two-sample parametric t test was applied.
"""
# 4. Based on your answer in Task 2, what is your advice for customer?
"""
    Considering the costs, they may abandon the relevant situation. As another suggestion, 
    when the investment in development is taken into account, the outputs of the analysis can be checked by waiting 
    for a certain period of time and thanks to the new data.    
"""
