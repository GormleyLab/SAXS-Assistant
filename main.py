from src.runner import run_analysis
import pandas as pd
from pathlib import Path
import argparse
import json
from joblib import dump
import os


def sanitize_path(path_str):
    # Remove quotes and convert to a proper Path object
    path_str = path_str.strip().strip('"').strip("'")
    return Path(path_str)


def clean_dataframe_paths(df, column_name):
    # Remove quotes and normalize paths in a specific column
    df[column_name] = df[column_name].apply(
        lambda x: str(Path(str(x).strip().strip('"').strip("'")))
    )
    return df


def main(df_path, start_index=0, end_index=None, output_dir="outputs"):
    # Sanitize input paths
    df_path = sanitize_path(df_path)
    output_dir = sanitize_path(output_dir)
    print(f"Using input file: {df_path}")
    print(f"Saving results to: {output_dir}")

    # Load the dataframe
    df = pd.read_excel(df_path)
    df = clean_dataframe_paths(df, "path")  # Replace with your actual column name
    df["path"] = df["path"] + "/"

    if end_index is None:
        plot_data, updated_df = run_analysis(df, start_index)
    elif int(end_index) > len(df):
        raise ValueError(
            f"end_index {end_index} is greater than the length of the dataframe {len(df)}"
        )
    else:
        plot_data, updated_df = run_analysis(df[: int(end_index)], start_index)

    # Save results
    os.makedirs(output_dir, exist_ok=True)
    dump(plot_data, f"{output_dir}/plot_data.joblib")
    updated_df.to_excel(f"{output_dir}/results.xlsx")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="Path to a JSON config file")
    parser.add_argument("df_path", nargs="?", help="Path to the input Excel file")
    parser.add_argument(
        "--start_index", type=int, default=0, help="Index to start analysis from"
    )
    parser.add_argument(
        "--end_index",
        default=None,
        help="If any, index to stop analysis at (exclusive, default is None which means all data)",
    )
    parser.add_argument(
        "--output_dir", default="outputs", help="Folder to save results"
    )

    args = parser.parse_args()

    if args.config:
        with open(args.config) as f:
            config = json.load(f)
        df_path = config["df_path"]
        start_index = config.get("start_index", 0)
        end_index = config.get("end_index", None)
        output_dir = config.get("output_dir", "outputs")
    else:
        df_path = args.df_path
        start_index = args.start_index
        end_index = args.end_index
        output_dir = args.output_dir

    main(df_path, start_index, end_index, output_dir)


# .\.venv\Scripts\activate.bat -- in cmd
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -- vscode run this first
# .\.venv\Scripts\activate   #thhen this , but will try to make a batch file to do this


# python main.py --config config.json   #run this to test


# Yank the files after when done

# twine yank saxs_assistant1 -v 0.1.1.dev10
