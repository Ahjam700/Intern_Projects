import numpy as np
import unittest
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d
from matplotlib import cm

#generating random data for a simple linear regression problem

#X is a 100x1 matrix of random values between 0 and 4.
#y is a target variable generated as a noisy linear function of X with a slope of 2 and an intercept of 10.
X = 4 * np.random.rand(100, 1) 
y = 10 + 2 * X + np.random.randn(100, 1)

# 1. Linear Hypothesis Function
def h(x, theta):
    expectation = np.dot(x, theta.reshape(x.shape[1], 1))
    return expectation

# 2. Mean Squared Error Function
def mean_squared_error(y_predicted, y_label):
    return np.sqrt(((y_predicted - y_label) ** 2).mean())

# 3. LeastSquaresRegression Class
class LeastSquaresRegression():
    def __init__(self, ):
        self.theta_ = None

    def fit(self, X, y):
        # Calculates theta that minimizes the MSE and updates self.theta_
        self.theta_ = np.dot((np.dot(np.linalg.inv(np.dot(X.T, X)), X.T)), y)

    def predict(self, X):
        # Make predictions for data X, i.e output y = h(X) (See equation in Introduction)
        return h(X, self.theta_)

# 4. Bias Column Function
def bias_column(X):
    return np.c_[np.ones((X.shape[0], 1)), X]

x_recent = bias_column(X)

print(X[:5])
print(" ---- ")
print(x_recent[:5])
model = LeastSquaresRegression()
model.fit(x_recent, y)
print(model.theta_)
y_new = model.predict(x_recent)

# 5. My_Visualization
def my_visualization(X, y, y_new):
    plt.scatter(X, y, color="b", marker="o", s=30)

    # plotting the regression line
    plt.plot(X, y_new, color="r")

    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    # function to show plot
    plt.show()
    plt.savefig('my_linear_regression.png')

print(my_visualization(X, y, y_new))
# 6. GradientDescentOptimizer Class
# Define the GradientDescentOptimizer class based on your format
class GradientDescentOptimizer():

    def __init__(self, f, fprime, start, learning_rate=0.1):
        self.f_ = f  # Objective function
        self.fprime_ = fprime   # Gradient of the objective function
        self.current_ = start  # Current parameter values
        self.learning_rate_ = learning_rate  
        self.history_ = [start]    # Track parameter updates   

    def step(self):
        # Take a gradient descent steps, by Compute the new data and update selt.current_, to append the new data to history and it should return nothing
        new_data = self.current_ - (self.learning_rate_ * fprime(self.current_))
        self.current_ = new_data
        self.history_.append(self.current_)
        # print(self.current_)
        return

    def optimize(self, iterations=100):
        # Use the gradient descent to get closer to the minimum:
        # For each iteration, take a gradient step
        for i in range(iterations):
            self.step()
        return

    def getCurrentValue(self):
        # Return the current value of the optimizer
        return self.current_

    def print_result(self):
        print("Best theta found is " + str(self.current_))
        print("Value of f at this theta: f(theta) = " + str(self.f_(self.current_)))
        print("Value of f prime at this theta: f'(theta) = " + str(self.fprime_(self.current_)))


def f(x):
    return -np.exp(-(x - 0.7) ** 2)


def fprime(x):
    fp = 2 * x - np.array([4, 12])
    return fp

gradient = GradientDescentOptimizer(f, fprime, np.random.normal(size=(2,)), 0.1)
gradient.optimize(10)
gradient.print_result()

d = np.linspace(-10, 10, 20)
f = np.linspace(-10, 10, 20)
X, Y = np.meshgrid(d, f)

Z = X ** 2 + Y ** 2
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, color='b', alpha=0.1)

surface = ax.plot_surface(X, Y, Z,cmap=cm.coolwarm,rstride=2,cstride=2)

plt.show()
print(plt.savefig('function_f_in_3D_1.png'))

d = np.linspace(-10, 10, 20)
f = np.linspace(-10, 10, 20)
X, Y = np.meshgrid(d, f)

Z = X ** 2 + Y ** 2
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, color='b', alpha=0.1)
ax.plot([t[0] for t in gradient.history_], [t[1] for t in gradient.history_], markerfacecolor='b', markeredgecolor='b',
        marker='.', markersize=5)
plt.show()
print(plt.savefig('function_f_in_3D_2.png'))


# Running the unit tests

if __name__ == '__main__':
    unittest.main()