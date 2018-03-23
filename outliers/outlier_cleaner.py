#!/usr/bin/python
import math
from copy import deepcopy

# function to clean outlier data of 10%
def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    # cleaned_data to store result
    cleaned_data = []

    # percent to clean
    percent = 0.1

    # get SSE_LIST
    sse_list = [ math.pow((net_worth - pre), 2) for pre, net_worth in zip(predictions, net_worths) ]

    # define a list to store the index of del value
    rindex_list = []

    # calculate the del value size
    rlen = len(sse_list) * percent

    # made a deepcopy
    tlist = deepcopy(sse_list)

    # get del index list(the max rlen values of sse_list), and never modify original sse_list
    while len(rindex_list) < rlen:
        max_sse = max(tlist)
        idmax = sse_list.index(max_sse)
        rindex_list.append(idmax)
        tlist.remove(max_sse)

    # get the clean dataset, if index is in del list, just continue
    for i in range(len(net_worths)):
        if i in rindex_list:
            continue

        cleaned_data.append((ages[i], net_worths[i], sse_list[i]))

    # return result
    return(cleaned_data)

