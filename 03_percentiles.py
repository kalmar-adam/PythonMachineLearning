import numpy


# SOURCE: w3schools

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

# PERCENTILES (1-99) = describes the value that a given percent of the values are lower than.
# like median percentiles requires sorting values ASC order
age_perc_75 = numpy.percentile(ages, 75)
print("age_perc_75", age_perc_75)


age_perc_90 = numpy.percentile(ages, 90)
print("age_perc_90", age_perc_90)

