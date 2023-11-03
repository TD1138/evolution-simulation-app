import numpy as np
from random import uniform

class organism():
    def __init__(self, settings, wih=None, who=None, name=None):

        self.x = uniform(settings['x_min'], settings['x_max'])  # position (x)
        self.y = uniform(settings['y_min'], settings['y_max'])  # position (y)

        self.r = uniform(0,360)                 # orientation   [0, 360]
        self.v = uniform(0,settings['v_max'])   # velocity      [0, v_max]
        self.dv = uniform(-settings['dv_max'], settings['dv_max'])   # dv

        self.d_food = 100   # distance to nearest food
        self.r_food = 0     # orientation to nearest food
        self.fitness = 0    # fitness (food count)

        self.wih = wih
        self.who = who

        self.name = name

    def next_action(self):

        # SIMPLE MLP
        activation = lambda x: np.tanh(x)
        hidden_layer = activation(np.dot(self.wih, self.r_food))
        output = activation(np.dot(self.who, hidden_layer))

        # UPDATE dv AND dr WITH MLP RESPONSE
        self.nn_dv = float(output[0])   # [-1, 1]  (accelerate=1, deaccelerate=-1)
        self.nn_dr = float(output[1])   # [-1, 1]  (left=1, right=-1)