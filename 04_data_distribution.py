import numpy
import matplotlib.pyplot as plt

# generate 250 random float value between 0 and 5
data_set = numpy.random.uniform(0, 5, 250)
print(data_set) # continous data because these are floats

# HISTOGRAM
# show value between 0-1, 1-2, 2-3, 3-4 and 4-5 with 5 bars counting them

plt.hist(data_set, 5)
plt.show()

