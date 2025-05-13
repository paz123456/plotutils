import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

def discrete_cmap(n, base_cmap='viridis'):
    """
    Returns a ListedColormap with n discrete colors sampled from the base_cmap.

    Parameters:
    - n (int): Number of discrete colors.
    - base_cmap (str): Name of the continuous colormap to sample from.

    Returns:
    - ListedColormap: A colormap with n discrete colors.
    """
    # Get the base colormap
    base = plt.get_cmap(base_cmap)
    # Sample n colors from the continuous colormap
    colors = base(np.linspace(0, 1, n))
    # Create and return a discrete colormap
    return mcolors.ListedColormap(colors)
