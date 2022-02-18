import numpy as np
import matplotlib.pyplot as plt


class Sampels:
    N_m = 100
    N0 = 50
    P = 10

    def __init__(self):
        self.X = np.random.normal(0.0, 1.0, size=(self.N_m, self.P))
        self.X0 = self.X[:self.N0, :]

    def get_shape(self):
        return ('X.shape= ', self.X.shape), ('X0.shape= ', self.X0.shape)


class Teacher:
    N_0 = 50
    P = 10
    sig = 1

    def __init__(self, X):
        self.w0 = np.random.normal(0.0, 1.0, size=(1, self.N_0))
        self.z = np.random.normal(0.0, 1.0, size=(1, self.P))
        self.X0 = X.X0
        self.Y = np.add(np.dot(self.w0, self.X0), np.dot(self.sig, self.z))
        print(self.Y)
        print(self.Y.shape)

    def get_shape(self):
        return 'w0.shape= ', self.w0.shape


# Xt = np.random.normal(0.0, 1.0, size=(1, 10))
# print(Xt)
# res = np.dot(100, Xt)
# print(res)
X = Sampels()
X.get_shape()
teacher = Teacher(X)
teacher.get_shape()
