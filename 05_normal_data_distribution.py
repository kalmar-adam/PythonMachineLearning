import numpy
import matplotlib.pyplot as plt

# source: w3schools

# generate data, that are concentrated around a given value
# MEAN: 5, STD: 1, values count: 100000
normal_data_dist = numpy.random.normal(5, 1, 100000)

print(normal_data_dist)

plt.hist(normal_data_dist, 100)
plt.show()