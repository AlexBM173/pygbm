import numpy as np

class BaseGBM:
    """
    Base class for Geometric Brownian Motion (GBM) models.

    Attributes:
        y0 (float): Initial value of the process.
        mu (float): Drift coefficient.
        sigma (float): Diffusion coefficient.

    Methods:
        __init__(y0, mu, sigma): Initializes the GBM model with given parameters.
    """
    
    def __init__(self, y0, mu, sigma):
        self.y0 = y0  # Initial value
        self.mu = mu  # Drift coefficient
        self.sigma = sigma  # Diffusion coefficient