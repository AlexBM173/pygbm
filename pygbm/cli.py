#!/usr/bin/env python3
import argparse

# Use a package-relative import so the module can be executed with
# `python -m pygbm.cli` or when the package is installed.
from .gbm_simulation import GBMSimulator

def main():
    """
    Main function to parse command-line arguments and run the GBM simulation.

    Args:
        None
    Returns:
        None
    """
    parser = argparse.ArgumentParser(description="Simulate Geometric Brownian Motion")
    parser.add_argument("--y0", type=float, required=True, help="Initial value Y(0)")
    parser.add_argument("--mu", type=float, required=True, help="Drift coefficient")
    parser.add_argument("--sigma", type=float, required=True, help="Diffusion coefficient")
    parser.add_argument("--T", type=float, required=True, help="Total time for simulation")
    parser.add_argument("--N", type=int, required=True, help="Number of time steps")
    parser.add_argument("--solver", type=str, required=True, help="Analytical or numerical solver")
    parser.add_argument("--output", type=str, help="Output file for the plot")

    args = parser.parse_args()

    simulator = GBMSimulator(args.y0, args.mu, args.sigma)
    t_values, y_values = simulator.simulate_path(args.T, args.N, args.solver)
    simulator.plot_path(t_values, y_values, output=args.output)

if __name__ == "__main__":
    main()