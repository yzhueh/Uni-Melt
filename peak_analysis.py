def analyze_both_channels(spline_fam, peaks_fam, temp_sol_fam, spline_hex, peaks_hex, temp_sol_hex):
    """
    Analyze data from FAM and HEX channels and return final classification result
    
    Parameters:
    spline_fam: Spline function for FAM channel
    peaks_fam: Local peak positions for FAM channel
    temp_sol_fam: Global optimal temperature solution for FAM channel
    spline_hex: Spline function for HEX channel 
    peaks_hex: Local peak positions for HEX channel
    temp_sol_hex: Global optimal temperature solution for HEX channel
    
    Returns:
    dict: Dictionary containing classification results and detailed information
    """
    result = {
        'classification': '',
        'FAM_result': '',
        'HEX_result': '',
        'FAM_peaks_count': len(peaks_fam),
        'HEX_peaks_count': len(peaks_hex),
        'FAM_temperature': temp_sol_fam,
        'HEX_temperature': temp_sol_hex
    }
    
    # First check FAM channel
    if len(peaks_fam) <= 2:
        # Judge based on FAM global optimal temperature
        if 50 <= temp_sol_fam <= 55:
            result['classification'] = 'HPV-16'
        elif 58 <= temp_sol_fam <= 65:
            result['classification'] = 'HPV-18'
        elif 35 <= temp_sol_fam <= 45:
            result['classification'] = 'HPV-58'
        else:
            # If FAM temperature is out of range, check HEX channel
            if len(peaks_hex) <= 2:
                if 35 <= temp_sol_hex <= 45:
                    result['classification'] = 'HBB'
                elif 50 <= temp_sol_hex <= 60:
                    result['classification'] = 'HPV-31'
                elif 60 <= temp_sol_hex <= 65:
                    result['classification'] = 'HPV-33'
                else:
                    result['classification'] = 'No target'
            else:
                result['classification'] = 'Contamination'
    else:
        # FAM local optimal solutions > 2, check HEX channel
        if len(peaks_hex) <= 2:
            if 50 <= temp_sol_hex <= 60:
                result['classification'] = 'HPV-31'
            elif 60 <= temp_sol_hex <= 65:
                result['classification'] = 'HPV-33'
            else:
                result['classification'] = 'No target'
        else:
            result['classification'] = 'Contamination'
    
    return result

def format_result(result, sample_number):
    """
    Format analysis result as a concise string
    
    Parameters:
    result: Result dictionary returned by analyze_both_channels function
    sample_number: Sample number
    
    Returns:
    str: Formatted result string
    """
    return f"Sample {sample_number}: {result['classification']}"

# Interface to maintain compatibility with original code
def analyze_peaks(spline, peaks, temp_sol):
    """
    Single channel analysis interface (to maintain compatibility with original code)
    Actual analysis should use analyze_both_channels
    """
    return {
        'peaks_count': len(peaks),
        'temperature': temp_sol
    }