# ******************************************************************************
# This file is part of SAXS Assistant.
#
#    All code from SAXS Assisstant can be used freely for non-commercial purposes.
#    If you use this code in your work, please cite the following publications:
# Add The GPA citation
# Add Franke citation
# Add Raw citation
# SAXS Assistant citation
#    SAXS Assistant is based on the code from RAW, which is a SAXS data analysis software.
#
#
#    SAXS Assistant utilizes parts of the code from RAW
#    SAXS Assistant is shared for helping the community with SAXS data analysis.
#    but it is not a replacement for RAW, and does not include all the features of RAW.
#    SAXS Assisant does not offer warranty-- use at your own risk and evaluate the results carefully.
# ******************************************************************************************************


import os
import pandas as pd
import joblib
import shutil
from typing import Optional
from natsort import natsorted


def combine_sessions(base_path: str, output_name: str = "final_results"):
    """
    Combines results from multiple concurrent SAXS analysis runs stored in folders like
    'return', 'return_1', 'return_2', etc., within a given base path.

    Parameters:
        base_path (str): Path where the return folders are located.
        output_name (str): Base name for the final output files (Excel and joblib).
    """

    return_dirs = [d for d in os.listdir(base_path) if d.startswith("return")]
    sorted_dirs = natsorted(return_dirs)

    combined_df = pd.DataFrame()
    combined_dict = {}
    seen_files = set()
    i = 0  # counter to append dfs in order
    for dir_name in sorted_dirs:
        folder_path = os.path.join(base_path, dir_name)
        results_path = os.path.join(folder_path, "results.xlsx")
        dict_path = os.path.join(folder_path, "plot_data.joblib")

        # Read and combine dataframe
        if os.path.exists(results_path):
            df = pd.read_excel(results_path)
            # If not the first folder, drop any already seen 'file name' rows
            if i > 0 and "file name" in df.columns:
                df = df[~df["file name"].isin(seen_files)]

            # Tracking new file names probs dont need but better safe
            if "file name" in df.columns:
                seen_files.update(df["file name"].dropna().unique())

            combined_df = pd.concat([combined_df, df], ignore_index=True)

        # Read and combine dictionary
        if os.path.exists(dict_path):
            temp_dict = joblib.load(dict_path)
            combined_dict.update(temp_dict)
        i += 1
    # Save combined results
    combined_df.to_excel(os.path.join(base_path, f"{output_name}.xlsx"), index=False)
    joblib.dump(combined_dict, os.path.join(base_path, f"{output_name}_Plots.joblib"))

    # Move return folders to a subdirectory
    partials_path = os.path.join(base_path, "partials")
    os.makedirs(partials_path, exist_ok=True)

    for dir_name in sorted_dirs:
        shutil.move(
            os.path.join(base_path, dir_name), os.path.join(partials_path, dir_name)
        )

    print(
        f"Combined results saved as '{output_name}.xlsx' and '{output_name}_Plots.joblib' in {base_path}"
    )
    print(f"Original folders moved to '{partials_path}'")
