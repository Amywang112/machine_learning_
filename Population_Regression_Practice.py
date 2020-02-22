'''
This program plots Chinese population growth over the past 2000 years with simple linear regression.
Data source: https://www.wikiwand.com/en/Demographics_of_China

n = sample size
m = (n(sigma(xy)) - sigma(x)*sigma(y)) /
'''

import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x, y):
   #number of observations
    n = np.size(x);

    #finding the mean of x and y vector
    mean_x, mean_y = np.mean(x), np.mean(y)

    #calculating the least squares
    #SS_xy = n * np.sum(y*x) - np.sum(x) * np.sum(y)
    #SS_xx = n * np.sum(x*x) - np.sum(x) * np.sum(x)

    SS_xy = np.sum(y*x) - n * mean_y * mean_x
    SS_xx = np.sum(x*x) - n * mean_x * mean_x

    #SS_top = np.sum((x-mean_x)*(y-mean_y))
    #SS_bottom = np.sum(x-mean_x) * np.sum(x-mean_x)


    #regression coefficents
    slope = SS_xy/SS_xx
    yintercept = mean_y - slope * mean_x

    #return m and b
    return(slope, yintercept)

def plot_regression_line(x, y, b):
    #plotting the actual points as a scatter plot
    plt.scatter(x, y, color = "m", marker = "o", s = 30)

    #predicted response vector
    y_pred = b[0] + b[1] + x

    #plotting the regression plot_regression_line
    plt.plot(x, y_pred, color = "y")
    #plt.pyplot.plot(x, y_pred, color = "g")

    #putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    #function to show plotting
    plt.show()

def main():
    #observations
    #Year
    x = np.array([1, 156, 280, 600, 700, 755, 1290, 1351, 1393, 1400, 1500, 1550, 1650, 1700, 1750, 1800, 1850, 1928, 1950, 1975, 1982, 2000, 2005, 2010, 2015])
    #Population
    y = np.array([59594979, 50068856, 8200000, 44500000, 37140001, 52919309, 58834711, 87587000, 58323934, 66598339, 60105835, 60692856, 123000000, 126110000, 181810000, 332181400, 430000000, 474780000, 546815000, 916395000, 	1008180000, 1262645000, 1303720000, 1337825000, 1374620000])

    # estimated coefficients
    b = estimate_coef(x, y)
    print("Estimated coefficients: \n b = {} \ \n m = {}".format(b[0], b[1]))

    #plotting regression line
    plot_regression_line(x, y, b)

#make script importable and executables
if __name__ == "__main__":
    main()
