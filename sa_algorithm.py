import numpy as np
import random

class SA(object):
    def __init__(self, interval, spline_func, tab='min', T_max=50000, T_min=0.1, iterMax=2000, rate=0.97):
        self.interval = interval
        self.spline_func = spline_func
        self.T_max = T_max
        self.T_min = T_min
        self.iterMax = iterMax
        self.rate = rate
        self.x_seed = random.uniform(interval[0], interval[1])
        self.tab = tab.strip()
        self.best_solution = None
        self.best_value = float('inf') if tab == 'min' else float('-inf')
        self.solve()

    def func(self, x):
        return self.spline_func(x)

    def deal_min(self, x1, x2, delta_f, T):
        if delta_f < 0:
            return x2
        else:
            p = np.exp(-delta_f / T)
            return x2 if random.random() < p else x1

    def deal_max(self, x1, x2, delta_f, T):
        if delta_f > 0:
            return x2
        else:
            p = np.exp(delta_f / T)
            return x2 if random.random() < p else x1

    def solve(self):
        temp = 'deal_' + self.tab
        if hasattr(self, temp):
            deal = getattr(self, temp)
        else:
            exit('>>>Invalid tab parameter: must be "min" or "max"<<<')
        
        x1 = self.x_seed
        current_value = self.func(x1)
        
        if (self.tab == 'min' and current_value < self.best_value) or \
           (self.tab == 'max' and current_value > self.best_value):
            self.best_value = current_value
            self.best_solution = x1
        
        T = self.T_max
        while T >= self.T_min:
            for i in range(self.iterMax):
                f1 = self.func(x1)
                delta_x = (random.random() * 2 - 1) * (T / self.T_max) * 5
                if x1 + delta_x >= self.interval[0] and x1 + delta_x <= self.interval[1]:
                    x2 = x1 + delta_x
                else:
                    x2 = x1 - delta_x
                f2 = self.func(x2)
                delta_f = f2 - f1
                x1 = deal(x1, x2, delta_f, T)
                
                current_value = self.func(x1)
                if (self.tab == 'min' and current_value < self.best_value) or \
                   (self.tab == 'max' and current_value > self.best_value):
                    self.best_value = current_value 
                    self.best_solution = x1
                    
            T *= self.rate
        self.x_solu = self.best_solution
        return self.x_solu