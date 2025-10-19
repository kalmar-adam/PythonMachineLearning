import numpy

# SOURCE: w3schools

# STD
speed = [86,87,88,86,87,85,86]
print("speed", speed)

# standard dev = how values are close or far from mean value
# std = (avg(v-u)^2 FOR v in speeds)^(1/2) WHERE v = value of speed, u = mean vale of speeds
standard_deviation_of_speed = numpy.std(speed)
print("standard_deviation_of_speed", standard_deviation_of_speed)

# non-numpy way calc
mean = sum(speed)/len(speed)
speed_mean_diffs = [s-mean for s in speed]
speed_mean_diff_square = [s**2 for s in speed_mean_diffs]
std = (sum(speed_mean_diff_square) / len(speed_mean_diff_square))**0.5 # if you want to get variance, just omit **0.5
print(std)



# wider range of values (not so close to mean)
speed2 = [32,111,138,28,59,77,97]
standard_deviation_of_speed2 = numpy.std(speed2)
print("standard_deviation_of_speed2", standard_deviation_of_speed2)

# VARIANCE
# 1. find mean
# 2. calc difference for all elements from the mean
# 3. find squares for all "difference from the mean" (=> squares difference)
# 4. get mean of these squares => VARIANCE
variance_of_speed2 = numpy.var(speed2)
print("variance_of_speed2", variance_of_speed2)

# VARIANCE = STD * STD = STD**2
std_of_speed2 = variance_of_speed2**0.5 # / SQRT operation
print("std_of_speed2", std_of_speed2)
