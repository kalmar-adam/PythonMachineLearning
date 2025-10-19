import numpy
from scipy import stats

# SOURCE: w3schools

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
print("speed", speed)


# mean of speed = SUM(speed) / len(speed)
mean_of_speed = numpy.mean(speed)
print("mean_of_speed", mean_of_speed)

# median of speed = middle element (or middle 2 element's mean) of sorted ASC speed
median_of_speed = numpy.median(speed)
print("median_of_speed", median_of_speed)

# mode of speeds = element/value that appears most times in speeds
mode_of_speed = stats.mode(speed)
print("mode_of_speed mode and count", mode_of_speed.mode, mode_of_speed.count)
