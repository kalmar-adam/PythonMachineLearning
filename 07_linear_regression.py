import matplotlib.pyplot as plt
from scipy import stats

#source: w3schools


# LINEAR REGREESSION - relationships between data-points -> draw straight line -> predict future
def linearreg():
    x = [5,7,8,7,2,17,2,9,4,11,12,9,6] # ages
    y = [99,86,87,88,111,86,103,87,94,78,77,85,86] # speeds

    slope, intercept, r, p, se = stats.linregress(x, y)
    """
        slope: line goes up/down if you increasing X value
        intercept: where the line is crossing Y line in x=0
    """
    def  myfunc(x):
        return slope * x + intercept

    mymodel = list(map(myfunc, x))
    print(mymodel)


    # calc a + bx (a, b values with no scipy)
    sum_y = sum(y)
    sum_x = sum(x)
    sum_xsqare = sum([_x**2 for _x in x])
    sum_xy = sum([x[idx]*y[idx] for idx, _ in enumerate(x)])
    sum_x_square = sum(x)**2
    a = ((sum_y*sum_xsqare) - (sum_x * sum_xy)) / ((len(x)*sum_xsqare) - sum_x_square)
    b = ((len(x)*sum_xy) - (sum_x*sum_y)) / ((len(x)*sum_xsqare)-(sum_x_square))
    print("a and intercept shold be equal", a, intercept)
    print("b and slope shold be equal", b, slope)
    


    plt.scatter(x, y)
    plt.plot(x, mymodel)
    plt.show()

def relationship():
    pass
    # r - coefficient of correlation
    # ranges -1 to 1, where 0 is no relationship and 1 or -1 means 100% relation
    x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
    y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

    """
        r stands for relation ship between -1 and 1
    """

    slope, intercept, r, p, std_err = stats.linregress(x, y)

    print(r) # ~ -0.76

def predict_future():
    x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
    y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

    slope, intercept, r, p, std_err = stats.linregress(x, y)

    def myfunc(x):
        return slope * x + intercept

    speed = myfunc(10)

    print(speed)

def bad_fit():
    x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
    y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

    slope, intercept, r, p, std_err = stats.linregress(x, y)

    def myfunc(x):
        return slope * x + intercept

    mymodel = list(map(myfunc, x))

    print("relation - r ->", r) # 0.013 bad relationship -> not suitablefor linear-regression

    plt.scatter(x, y)
    plt.plot(x, mymodel)
    plt.show()


linearreg()