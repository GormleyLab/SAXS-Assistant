import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))


from saxs_assistant.runner import analyze_and_save, prepare_dataframe
from saxs_assistant.plotting import plot_solved_summary
from saxs_assistant.organizer import combine_sessions

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
combine_sessions(
    "C:/Users/Cesar/Box/Sync files/SAXS project/Manuscript/Test Data/local test"
)
