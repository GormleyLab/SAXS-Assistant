import sys
import os

# If clone rep and want to run locally, use the command below to add the src folder to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))


from saxs_assistant.runner import (
    analyze_and_save,
    prepare_dataframe,
    analyze_and_plot_all,
)

from saxs_assistant.plotting import plot_solved_summary, plot_flagged
from saxs_assistant.organizer import combine_sessions
from joblib import load


# prepare_dataframe(
#     folder_path="C:/Users/Cesar/Box/Sync files/SAXS project/Manuscript/Test Data/local test/profiles",
#     angular_unit="1/A",
# )

# analyze_and_save(
#     "C:/Users/Cesar/Box/Sync files/SAXS project/Manuscript/Test Data/local test/input_df_Jun_20_25.xlsx",
#     start_index=2,
# )

# plot_solved_summary(
#     "C:/Users/Cesar/Box/Sync files/SAXS project/Manuscript/Test Data/local test/return/plot_data.joblib",
#     pdf_name="samples0",
# )
# combine_sessions(
#     "C:/Users/Cesar/Box/Sync files/SAXS project/Manuscript/Test Data/local test"
# )


import os
from pathlib import Path


def clean_path(path_str):
    """
    Cleans a file path string to work across OS.
    Converts Windows-style paths with escape characters to usable format.
    """
    # Replace common escape sequences (e.g., \t, \n) if the user pastes a raw Windows path
    path_str = path_str.encode("unicode_escape").decode("utf-8")  # Escapes \t, \n, etc.
    path_str = path_str.replace("\\\\", "\\")  # In case of double backslashes
    cleaned = Path(path_str).expanduser().resolve()
    return str(cleaned)


# new = clean_path(
#     r"C:\Users\Cesar\Box\Sync files\SAXS project\Manuscript\Test Data\local test\plot_data_100.joblib"
# )


# plot_flagged(
#     "C:/Users/Cesar/Box/Sync files/SAXS project/Manuscript/Test Data/local test/final_results_Plots.joblib"
# )

# plot_data = load(
#     "C:/Users/Cesar/Box/Sync files/SAXS project/Manuscript/Test Data/local test/plot_data_100.joblib"
# )
# # Debugging aid

analyze_and_plot_all(
    "C:/Users/Cesar/Box/Sync files/SAXS project/Manuscript/Test Data/local test/input_df_Jun_20_25.xlsx",
    music=True,
)


# pip install -e .[music]
