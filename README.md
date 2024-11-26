# Melting Curve Analysis Tool

A Python-based tool for analyzing DNA melting curves with peak detection and classification capabilities. This tool processes fluorescence data from FAM and HEX channels to identify and classify DNA samples.

## Features

- Processes melting curve data from FAM and HEX fluorescence channels
- Implements Simulated Annealing algorithm for optimal peak detection
- Generates visualizations of global and local peak analysis
- Provides automated classification of DNA samples
- Saves analysis results and plots to a designated output directory

## Requirements

- Python 3.10
- Required packages:
numpy>=1.24.0
pandas>=2.0.0
matplotlib>=3.7.0
scipy>=1.10.0
openpyxl>=3.1.0

## Installation

Clone the repository:
```bash
git clone https://github.com/yourusername/melting-curve-analysis.git
cd melting-curve-analysis
Install required packages:
bash

pip install -r requirements.txt
Usage
Prepare your input data in Excel format (.xlsx) with two sheets named 'FAM' and 'HEX'
Run the analysis:
bash

python main.py
The program will:

Process the melting curve data
Generate visualization plots
Save results in a 'result' directory
Create a summary of sample classifications
Output
The tool generates:

Individual plot files (.png) for each sample's analysis
A text file containing classification results
Console output showing real-time analysis progress
Project Structure
main.py: Main execution script
sa_algorithm.py: Simulated Annealing implementation
peak_finder.py: Peak detection and processing
peak_analysis.py: Sample classification logic
plotting.py: Visualization functions
