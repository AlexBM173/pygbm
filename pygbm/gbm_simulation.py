import numpy as np
import matplotlib.pyplot as plt
from .base import BaseGBM

class GBMSimulator(BaseGBM):
    """
    Simulator for Geometric Brownian Motion (GBM) paths.

    Inherits from:
        BaseGBM: Base class for GBM models.
    
    Methods:
        __init__(y0, mu, sigma): Initializes the GBM simulator with given parameters.
        simulate_path(T, N): Simulates a GBM path over time T with N steps.
        plot_path(t_values, y_values, output=None): Plots the simulated GBM path.

    Args:
        y0 (float): Initial value of the process.
        mu (float): Drift coefficient.
        sigma (float): Diffusion coefficient.
    """
    def __init__(self, y0, mu, sigma):
        """
        Initializes the GBM simulator with given parameters.

        Args:
            y0 (float): Initial value of the process.
            mu (float): Drift coefficient.
            sigma (float): Diffusion coefficient.
        """
        super().__init__(y0, mu, sigma)
    
    def simulate_path(self, T, N, solver):
        """
        Simulates a GBM path over time T with N steps using an analytical or specified numerical solver, either the Euler-Maruyama or Milstein method.

        Args:
            T (float): Total time for simulation.
            N (int): Number of time steps.
            solver (str): Solver type, either 'analytical', 'Euler-Maruyama', or 'Milstein'.

        Returns:
            t_values (numpy.ndarray): Array of time values.
            y_values (list): List of simulated GBM values at each time step.
        """

        dt = T/N

        t_values = np.linspace(0, T, N + 1)
        y_values = [self.y0]

        if solver == 'analytical':
            for i in range(1, N + 1):
                t = t_values[i]
                W_t = np.random.normal(0, np.sqrt(t))
                y_t = self.y0 * np.exp((self.mu - 0.5 * self.sigma ** 2) * t + self.sigma * W_t)
                y_values.append(y_t)
            return(t_values, y_values)
        
        elif solver == 'Euler-Maruyama':
            for i in range(1, N + 1):
                W_inc = np.random.normal(0, np.sqrt(dt))
                y_prev = y_values[-1]
                y_t = y_prev + self.mu * y_prev * dt + self.sigma * y_prev * W_inc
                y_values.append(y_t)
            return(t_values, y_values)
        
        elif solver == 'Milstein':
            for i in range(1, N + 1):
                W_inc = np.random.normal(0, np.sqrt(dt))
                y_prev = y_values[-1]
                y_t = (y_prev + self.mu * y_prev * dt + self.sigma * y_prev * W_inc +
                        0.5 * self.sigma**2 * y_prev * (W_inc**2 - dt))
                y_values.append(y_t)
            return(t_values, y_values)

    def plot_path(self, t_values, y_values, output=None):
        """
        Plots the simulated GBM path.

        Args:
            t_values (numpy.ndarray): Array of time values.
            y_values (list): List of simulated GBM values at each time step.
            output (str, optional): If provided, saves the plot to the specified file.
        
        Returns:
            None
        """

        self.t_values = t_values
        self.y_values = y_values

        plt.plot(t_values, y_values, label="GBM Path")
        plt.xlabel("Time")
        plt.ylabel("Y(t)")
        plt.title("Simulated Geometric Brownian Motion Path")
        plt.legend()
        if output:
            plt.savefig(output)
        else:
            plt.show()