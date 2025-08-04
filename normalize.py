import pandas as pd
import os
import numpy as np
import math

input_folder = "csv_export"
output_file = "normalized.xlsx"

results = []

for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):  # Adjust extension if needed
        filepath = os.path.join(input_folder, filename)
        df = pd.read_csv(filepath, sep=None, engine='python')  # auto-detect delimiter

        # Calculate ratios
        B2M_normalized = np.log10(df["BV 421-A"]) / np.log10(df["FITC-A"])
        
        # Store summary stats        
        results.append({
            "File": filename,
            "B2M Mean": B2M_normalized.mean(),
            "B2M Std": B2M_normalized.std(),
            "Total Events": len(df)
        })

# Write all summaries to a new Excel file
summary_df = pd.DataFrame(results)
summary_df.to_excel(output_file, index=False)
