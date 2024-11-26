import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from peak_finder import process_channel
from plotting import plot_channel, setup_axes
from peak_analysis import analyze_both_channels, format_result

def main(file_path):
    if not os.path.exists('result'):
        os.makedirs('result')
    
    temp_new = np.arange(20.5, 85, 0.5)
    
    df_fam = pd.read_excel(file_path, sheet_name='FAM', engine='openpyxl', header=1)
    df_hex = pd.read_excel(file_path, sheet_name='HEX', engine='openpyxl', header=1)
    
    # Collect all results
    all_results = []
    
    for col_idx, column in enumerate(df_fam.columns[1:], 1):
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 8))
        
        # Process FAM data
        spline_fam, peaks_fam, temp_sol_fam = process_channel(
            df_fam.iloc[:, 0], df_fam.iloc[:, col_idx], temp_new)
        
        # Process HEX data
        spline_hex, peaks_hex, temp_sol_hex = process_channel(
            df_hex.iloc[:, 0], df_hex.iloc[:, col_idx], temp_new)
        
        # Plot data
        plot_channel(ax1, ax2, temp_new, spline_fam, peaks_fam, temp_sol_fam, 'FAM')
        plot_channel(ax3, ax4, temp_new, spline_hex, peaks_hex, temp_sol_hex, 'HEX')
        
        # Analyze peaks
        result = analyze_both_channels(spline_fam, peaks_fam, temp_sol_fam,
                                     spline_hex, peaks_hex, temp_sol_hex)
        
        # Format current result
        current_result = format_result(result, col_idx)
        
        # Print current result immediately
        print(current_result)
        
        # Add to results list for final summary
        all_results.append(current_result)
        
        setup_axes([ax1, ax2, ax3, ax4])
        
        plt.suptitle(f'Column {column} Analysis', fontsize=16, y=1.02)
        plt.tight_layout()
        plt.savefig(os.path.join('result', f'{col_idx}.png'), dpi=300, bbox_inches='tight')
        plt.close()
    
    # Print and save summary after all processing is complete
    print("\nSummary of All Results:")
    
    # Save results to file
    with open(os.path.join('result', 'sample-result.txt'), 'w', encoding='utf-8') as f:
        f.write("Summary of All Results:\n")
        for result in all_results:
            print(result)  # Print to console
            f.write(f"{result}\n")  # Write to file

if __name__ == "__main__":
    file_path = "test.xlsx"
    main(file_path)