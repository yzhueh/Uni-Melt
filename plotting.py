import numpy as np
import matplotlib.pyplot as plt

def plot_channel(ax_global, ax_local, temp_new, spline, peaks, temp_sol, sheet):
    color = 'g' if sheet == 'FAM' else 'b'
    peak_color = 'pink' if sheet == 'FAM' else 'orange'
    local_peak_color = 'lightgreen' if sheet == 'FAM' else 'lightblue'
    
    # Global peak
    ax_global.plot(temp_new, spline(temp_new), f'{color}-', 
                  linewidth=2.0, label=f'{sheet} curve')
    ax_global.plot(temp_sol, spline(temp_sol), marker='*', 
                  color=peak_color, markersize=10, label=f'{sheet} global peak')
    ax_global.set_xlim(20, 85)
    ax_global.legend()
    ax_global.set_title(f'{sheet} Global Peak Analysis')
    
    # Local peaks
    ax_local.plot(temp_new, spline(temp_new), f'{color}-', 
                 linewidth=2.0, label=f'{sheet} curve')
    for i in temp_new[peaks]:
        ax_local.plot(i, spline(i), marker='*', 
                     color=local_peak_color, markersize=10)
    ax_local.plot([], [], marker='*', color=local_peak_color, 
                 markersize=10, label=f'{sheet} local peaks')
    ax_local.set_xlim(20, 85)
    ax_local.legend()
    ax_local.set_title(f'{sheet} Local Peaks Analysis')

def setup_axes(axes):
    """
    Configure the appearance of plot axes
    
    Parameters:
    axes: List of matplotlib axes to be configured
    """
    for ax in axes:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.set_xticks(np.arange(20, 90, 10))
        ax.tick_params(axis='both', which='major', labelsize=10)
        ax.set_xlabel('Temperature (°C)')
        ax.set_ylabel('Fluorescence')