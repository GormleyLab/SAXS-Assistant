import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))


from saxs_assistant.runner import (
    analyze_and_save,
    prepare_dataframe,
    analyze_and_plot_all,
)

from saxs_assistant.plotting import plot_solved_summary, plot_flagged
from saxs_assistant.organizer import combine_sessions
from joblib import load

print("ran")

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

# def clean_path(path_str, resolve_absolute=True):
#     """
#     Cleans up a path string, fixing Windows-style slashes and removing extra quotes.

#     Args:
#         path_str (str): The raw path string.
#         resolve_absolute (bool): Whether to resolve to absolute path.

#     Returns:
#         str: Cleaned-up path.
#     """
#     if not isinstance(path_str, str):
#         raise TypeError("Path must be a string.")

#     # Strip quotes and whitespace
#     path_str = path_str.strip().strip('"').strip("'")

#     # Replace backslashes with forward slashes
#     cleaned = path_str.replace("\\", "/")

#     # Optionally resolve absolute path
#     if resolve_absolute:
#         cleaned = os.path.abspath(cleaned)

#     return cleaned
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
#     r"C:\Users\Cesar\Box\Sync files\SAXS project\Manuscript\Test Data\local test\plot_data_100.joblib"
# )
# print(new)
# plot_flagged(
#     "C:/Users/Cesar/Box/Sync files/SAXS project/Manuscript/Test Data/local test/final_results_Plots.joblib"
# )

# plot_data = load(
#     "C:/Users/Cesar/Box/Sync files/SAXS project/Manuscript/Test Data/local test/plot_data_100.joblib"
# )
# # Debugging aid
# for sample_id, item in plot_data.items():
#     print(f"{sample_id} keys: {item.keys()}")
analyze_and_plot_all(
    "C:/Users/Cesar/Box/Sync files/SAXS project/Manuscript/Test Data/local test/input_df_Jun_20_25.xlsx",
    music=True,
)


# pip install -e .[music]
