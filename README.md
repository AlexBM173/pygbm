# pygbm

Practice for the MPhil Data Intensive Science Research Computing and Software Development module. Getting experience developing Python packages with complete documentation and object-oriented programming.

## Python package for geometric Brownian motion simulations

## Running the script

There are seven arguments you can pass to the GBM simulator, six of which are required for it to function:

- y0: A float specifying the starting value of the GBM (required).
- mu: A float specifying the drift coefficient of the GBM (required).
- sigma: A float specifying the diffusion coefficient of the GBM (required).
- T: A float specifying the total time the GBM will run for (required).
- N: An integer specifying the number of timesteps used in the simulation (required).
- solver: A string specifying the method used to simulate the GBM. Possible options are 'analytical', 'Einstein-Maruyama', and 'Milstein' (required).
- output: A string specifying the name of the output image of the GBM path as a function of time.

Example usage:

```
python -m pygbm.cli --y0 1 --mu 0.05 --sigma 0.2 --T 1 --N 100 --solver analytical --output gbm_plot.png
```