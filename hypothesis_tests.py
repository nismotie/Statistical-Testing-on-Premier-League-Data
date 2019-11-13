"""
This module is for your final hypothesis tests.
Each hypothesis test should tie to a specific analysis question.

Each test should print out the results in a legible sentence
return either "Reject the null hypothesis" or "Fail to reject the null hypothesis" depending on the specified alpha
"""

import pandas as pd
import numpy as np
from scipy import stats
import math

def make_t_dist(t, t_critical, dof, title):
    """
    makes a visualisation of a t-distribution, with lines for t-statistic and critical t-value
    :param t: t-statistic
    :param t_critical: the critical t value 
    :param dof: the welch's degress of freedom
    :title: the desired title of the graph
    """
    
    x= np.linspace(-5, 5, 200)
    
    y = stats.t.pdf(xs, df, 0, 1)
    
    fig = plt.figure(figsize=(8,5))
    
    ax = fig.gca()
    
    ax.plot(x, y, linewidth=3, color='darkblue')
    
    # plot a vertical line for our measured difference in rates t-statistic
    ax.axvline(t, color='yellow', linestyle='--', lw=2,label='t-statistic')
    ax.axvline(t_critical, color='purple', linestyle='--', lw=2, label='critical t-value')
    ax.fill_betweenx(y, x, t_critical, where = x>t_critical)
    ax.legend()
    plt.title(title)
    plt.show()

def welch_dof(a, b):
    """
    This module is for calculating the degrees of freedom that go into a welch's t-test
    :param a: first sample to compare
    :param b: second sample to compare
    """
    s1 = a.var(ddof=1)
    s2 = b.var(ddof=1)
    n1 = len(a)
    n2 = len(b)
    numerator = (s1/n1 + s2/n2)**2
    denominator = (s1/ n1)**2/(n1 - 1) + (s2/ n2)**2/(n2 - 1)
    return numerator/denominator

def cohen_d:
    nx = len(group1)
    ny = len(group2)
    dof = nx + ny - 2
    return (mean(x) - mean(y)) / sqrt(((nx-1)*std(x, ddof=1) ** 2 + (ny-1)*std(y, ddof=1) ** 2) / dof)

def create_sample_dists(cleaned_data, y_var=None, categories=[]):
    """
    Each hypothesis test will require you to create a sample distribution from your data
    Best make a repeatable function

    :param cleaned_data:
    :param y_var: The numeric variable you are comparing
    :param categories: the categories whose means you are comparing
    :return: a list of sample distributions to be used in subsequent t-tests

    """
    htest_dfs = []

    # Main chunk of code using t-tests or z-tests
    return htest_dfs

def compare_pval_alpha(p_val, alpha):       vb
    status = ''
    if p_val > alpha:
        status = "Fail to reject"
    else:
        status = 'Reject'
    return status


def hypothesis_test_one(alpha = None, cleaned_data):
    """
    Describe the purpose of your hypothesis test in the docstring
    These functions should be able to test different levels of alpha for the hypothesis test.
    If a value of alpha is entered that is outside of the acceptable range, an error should be raised.

    :param alpha: the critical value of choice
    :param cleaned_data: 
    :return:
    """
    # Get data for tests
    comparison_groups = create_sample_dists(cleaned_data=None, y_var=None, categories=[])

    ###
    # Main chunk of code using t-tests or z-tests, effect size, power, etc
    ###
    
    

    # starter code for return statement and printed results
    status = compare_pval_alpha(p_val, alpha)
    assertion = ''
    if status == 'Fail to reject':
        assertion = 'cannot'
    else:
        assertion = "can"
        # calculations for effect size, power, etc here as well

    print(f'Based on the p value of {p_val} and our aplha of {alpha} we {status.lower()}  the null hypothesis.'
          f'\n Due to these results, we  {assertion} state that there is a difference between NONE')

    if assertion == 'can':
        print(f"with an effect size, cohen's d, of {str(coh_d)} and power of {power}.")
    else:
        print(".")

    return status

def hypothesis_test_two():
        """
    Describe the purpose of your hypothesis test in the docstring
    These functions should be able to test different levels of alpha for the hypothesis test.
    If a value of alpha is entered that is outside of the acceptable range, an error should be raised.

    :param alpha: the critical value of choice
    :param cleaned_data: 
    :return:
    """
    # Get data for tests
    comparison_groups = create_sample_dists(cleaned_data=None, y_var=None, categories=[])
    
    ###
    # Main chunk of code using t-tests or z-tests, effect size, power, etc
    ###

    # starter code for return statement and printed results
    status = compare_pval_alpha(p_val, alpha)
    assertion = ''
    if status == 'Fail to reject':
        assertion = 'cannot'
    else:
        assertion = "can"
        # calculations for effect size, power, etc here as well

    print(f'Based on the p value of {p_val} and our aplha of {alpha} we {status.lower()}  the null hypothesis.'
          f'\n Due to these results, we  {assertion} state that there is a difference between NONE')

    if assertion == 'can':
        print(f"with an effect size, cohen's d, of {str(coh_d)} and power of {power}.")
    else:
        print(".")

    return status


def hypothesis_test_three(alpha=None, group1, group2):
        """
    Testing to see whether the 

    :param alpha: the critical value of choice
    :param cleaned_data: 
    :return:
    """
    
    ###
    # Main chunk of code using t-tests or z-tests, effect size, power, etc
    ###
    
    tt_results = stats.ttest_ind(group1, group2, equal_var = False)
    t_stat = tt_results[0]
    p_val = tt_results[1]
    

    # starter code for return statement and printed results
    status = compare_pval_alpha(p_val, alpha)
    assertion = ''
    if status == 'Fail to reject':
        assertion = 'cannot'
    else:
        assertion = "can"
        # calculations for effect size, power, etc here as well

    print(f'Based on the p value of {p_val} and our aplha of {alpha} we {status.lower()}  the null hypothesis.'
          f'\n Due to these results, we  {assertion} state that there is a difference between games with a red card and those without')

    if assertion == 'can':
        print(f"with an effect size, cohen's d, of {str(coh_d)} and power of {power}.")
    else:
        print(".")

    return status


def hypothesis_test_four():
    pass
