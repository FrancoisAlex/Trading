import math
import numpy as np

class OU_Drift_case:
    mu_rod : float 
    delta : float
    kappa : float
    sigma : float
    m1_0 : float
    v1_0 : float
    lambda_ : float
    
    def __init__(self, mu_rod : float, delta : float, kappa : float, sigma : float, m1_0 : float, v1_0 : float, lambda_ : float):
        self.mu_rod, self.delta, self.kappa, self.sigma = mu_rod, delta, kappa, sigma
        self.m1_0, self.v1_0, self.lambda_ = m1_0, v1_0, lambda_
        
    @property
    def M(self):
        M = [[] for _ in range(3)]
        M[1] = [self.mu_rod, self.m1_0 - self.mu_rod]
        M[2] = [(2 * self.mu_rod - self.sigma**2)]
        return M
        