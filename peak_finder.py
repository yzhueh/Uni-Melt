import pandas as pd
from scipy.interpolate import CubicSpline
from scipy.signal import find_peaks
from sa_algorithm import SA

def process_channel(temp, intensity, temp_new):
    """
    Process channel data to find peaks and optimal temperature
    
    Parameters:
    temp: Temperature data points
    intensity: Intensity values corresponding to temperatures
    temp_new: New temperature range for interpolation
    
    Returns:
    spline: Cubic spline interpolation function
    peaks: Detected peak positions
    best_sol: Optimal temperature solution
    """
    # Create DataFrame with temperature and intensity data
    data1 = pd.DataFrame({'temp': temp, 'intensity': intensity})
    
    # Create cubic spline interpolation
    spline = CubicSpline(data1.temp, data1.intensity)
    
    # Find peaks in negative spline (valleys in original data)
    peaks, _ = find_peaks(-spline(temp_new), distance=10, prominence=20)
    
    # Initialize best solution tracking
    best_sol = None
    best_value = float('inf')
    
    # Run simulated annealing twice to find global minimum
    for _ in range(2):
        sa = SA([20.5, 85, 0.5], spline, 'min')
        current_sol = sa.solve()
        current_value = spline(current_sol)
        
        # Update best solution if current is better
        if current_value < best_value:
            best_value = current_value
            best_sol = current_sol
    
    return spline, peaks, best_sol