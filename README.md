# A/B Testing with Python

- What is A/B Testing?

A/B testing (also known as bucket testing or split-run testing) is a user experience research methodology.A/B tests consist of a randomized experiment with two variants, A and B. It includes application of statistical hypothesis testing or "two-sample hypothesis testing" as used in the field of statistics. A/B testing is a way to compare two versions of a single variable, typically by testing a subject's response to variant A against variant B, and determining which of the two variants is more effective.

- A/B Testing Methods
> Independent Two-Sample T-Test (Comparing Means of Two Group)
> 
> Parametric Comparison (if Normality Assumption and Variance Homogeneity Assumption are provided)
> 
> Nonarametric Comparison (if Normality Assumption or Variance Homogeneity Assumption are NOT provided)
> 
> Two Sample Ratio Test (Comparing Ratio of Two Group)
>
> Anova (Mean Comparison of More than Two Groups)

# Business Problem
- 
......... company recently made an offer called maximum bidding a new bid type, average bidding, as an alternative to the bidding type introduced. One of their customers, ....., is testing this new feature. Company decided to try and find that averagebidding is better than maximumbidding. Do an A/B test to see if it converts too much wants.

# Dataset Story

In this dataset, which contains the website information of ........ ,information of user are number of ads they saw and clicked on, purchase frequency.
There are two separate data sets, the control and test groups.

# Variables

Impression – Ad views
Click – Clicks >> Indicates the number of clicks on the displayed ad.
Purchase >> Indicates the number of products purchased after the ads clicked.
Earning – Earning >> Earnings after purchased products
