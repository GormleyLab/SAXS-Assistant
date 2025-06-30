import os

from plotting.plot_solved_summary import plot_solved_summary

# Path to your joblib file with the dictionary
plot_data_path = "C:/Users/Cesar/Box/Sync files/SAXS project/Manuscript/Test Outputs/plot_data.joblib"

# Output folder for plots
output_folder = (
    "C:/Users/Cesar/Box/Sync files/SAXS project/Manuscript/Test Outputs/summary_plots"
)
pdf_name = "test_summary.pdf"

# Run the function
plot_solved_summary(
    plot_data_path=plot_data_path, output_folder=output_folder, pdf_name=pdf_name
)
print(f"Plots saved to {output_folder}/{pdf_name}")
