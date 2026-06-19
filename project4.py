# data_cleaner.py

"""
Data Cleaning Automation and Data Quality Management System
- Load CSV / Excel / JSON
- Handle missing values
- Remove duplicates
- Detect & standardize dates
- Clean text columns
- Dataset summary

import os
import re
import warnings

import numpy as np
import pandas as pd
from tabulate import tabulate

warnings.filterwarnings("ignore")


class DataCleaner:
    """
    Automated Data Cleaning System
    """

    def __init__(self):

        self.df = None

        self.cleaned_dir = "cleaned_data"

        self.reports_dir = "reports"

        os.makedirs(
            self.cleaned_dir,
            exist_ok=True
        )

        os.makedirs(
            self.reports_dir,
            exist_ok=True
        )

    # --------------------------------------------
    # LOAD DATASET
    # --------------------------------------------

    def load_dataset(
            self,
            file_path
    ):

        """
        Load CSV, Excel or JSON file.
        """

        try:

            extension = file_path.split(".")[-1]

            if extension == "csv":

                self.df = pd.read_csv(
                    file_path
                )

            elif extension == "xlsx":

                self.df = pd.read_excel(
                    file_path
                )

            elif extension == "json":

                self.df = pd.read_json(
                    file_path
                )

            else:

                raise ValueError(
                    "Unsupported File Format"
                )

            print(

                f"\n Loaded "

                f"{len(self.df)} "

                f"records"

            )

            print(

                f" Total Columns: "

                f"{self.df.shape[1]}"

            )

        except FileNotFoundError:

            print(
                "\n File not found."
            )

        except Exception as e:

            print(

                f"\n Error: "

                f"{e}"

            )

    # --------------------------------------------
    # DATASET SUMMARY
    # --------------------------------------------

    def dataset_summary(self):

        """
        Display dataset summary.
        """

        summary = {

            "Total Records":

                len(self.df),

            "Total Columns":

                self.df.shape[1],

            "Missing Values":

                self.df.isnull()

                .sum()

                .sum(),

            "Duplicate Records":

                self.df

                .duplicated()

                .sum(),

            "Memory Usage (MB)":

                round(

                    self.df

                    .memory_usage(

                        deep=True

                    )

                    .sum()

                    /

                    (1024**2),

                    2

                )

        }

        print(

            "\n DATASET SUMMARY\n"

        )

        print(

            tabulate(

                summary.items(),

                headers=[

                    "Metric",

                    "Value"

                ],

                tablefmt="pretty"

            )

        )

    # --------------------------------------------
    # HANDLE MISSING VALUES
    # --------------------------------------------

    def handle_missing_values(

            self,

            strategy="mean"

    ):

        """
        Handle missing values.

        Strategies:

        mean

        median

        mode

        forward_fill

        backward_fill
        """

        print(

            "\n Handling "

            "Missing Values..."

        )

        missing_before = (

            self.df

            .isnull()

            .sum()

            .sum()

        )

        numeric_cols = (

            self.df

            .select_dtypes(

                include=np.number

            )

            .columns

        )

        if strategy == "mean":

            for col in numeric_cols:

                self.df[col] = (

                    self.df[col]

                    .fillna(

                        self.df[col]

                        .mean()

                    )

                )

        elif strategy == "median":

            for col in numeric_cols:

                self.df[col] = (

                    self.df[col]

                    .fillna(

                        self.df[col]

                        .median()

                    )

                )

        elif strategy == "mode":

            for col in self.df.columns:

                self.df[col] = (

                    self.df[col]

                    .fillna(

                        self.df[col]

                        .mode()[0]

                    )

                )

        elif strategy == "forward_fill":

            self.df.fillna(

                method="ffill",

                inplace=True

            )

        elif strategy == "backward_fill":

            self.df.fillna(

                method="bfill",

                inplace=True

            )

        else:

            raise ValueError(

                "Invalid Strategy"

            )

        missing_after = (

            self.df

            .isnull()

            .sum()

            .sum()

        )

        print(

            f" Missing Before: "

            f"{missing_before}"

        )

        print(

            f" Missing After : "

            f"{missing_after}"

        )

    # --------------------------------------------
    # REMOVE DUPLICATES
    # --------------------------------------------

    def remove_duplicates(self):

        """
        Remove duplicate records.
        """

        duplicates = (

            self.df

            .duplicated()

            .sum()

        )

        self.df.drop_duplicates(

            inplace=True

        )

        print(

            f"\n Removed "

            f"{duplicates} "

            f"duplicate records"

        )

    # --------------------------------------------
    # DETECT DATE COLUMNS
    # --------------------------------------------

    def clean_dates(self):

        """
        Detect and standardize dates.
        """

        print(

            "\n Cleaning "

            "Date Columns..."

        )

        for col in self.df.columns:

            try:

                converted = pd.to_datetime(

                    self.df[col],

                    errors="coerce"

                )

                valid_ratio = (

                    converted

                    .notna()

                    .mean()

                )

                if valid_ratio > 0.7:

                    self.df[col] = converted

                    print(

                        f" Standardized "

                        f"{col}"

                    )

            except:

                continue

    # --------------------------------------------
    # CLEAN TEXT COLUMNS
    # --------------------------------------------

    def clean_text(self):

        """
        Clean text columns.
        """

        print(

            "\n Cleaning "

            "Text Columns..."

        )

        text_cols = (

            self.df

            .select_dtypes(

                include="object"

            )

            .columns

        )

        for col in text_cols:

            self.df[col] = (

                self.df[col]

                .astype(str)

                .str.strip()

                .str.title()

            )

            self.df[col] = (

                self.df[col]

                .apply(

                    lambda x:

                    re.sub(

                        r"[^A-Za-z0-9 ]",

                        "",

                        x

                    )

                )

            )

        print(

            f" Cleaned "

            f"{len(text_cols)} "

            f"text columns"

        )

    # --------------------------------------------
    # SAVE CLEANED DATASET
    # --------------------------------------------

    def export_cleaned_dataset(

            self,

            filename=

            "cleaned_dataset.csv"

    ):

        path = os.path.join(

            self.cleaned_dir,

            filename

        )

        self.df.to_csv(

            path,

            index=False

        )

        print(

            f"\n Cleaned "

            f"Dataset Saved:\n"

            f"{path}"

        )


# --------------------------------------------
# MAIN FUNCTION
# --------------------------------------------

def main():

    print(

        "\n"

        +

        "="*60

    )

    print(

        " DATA CLEANING AUTOMATION SYSTEM "

    )

    print(

        "="*60

    )

    cleaner = DataCleaner()

    file_path = input(

        "\nEnter dataset path: "

    )

    cleaner.load_dataset(

        file_path

    )

    cleaner.dataset_summary()

    cleaner.handle_missing_values(

        strategy="mean"

    )

    cleaner.remove_duplicates()

    cleaner.clean_dates()

    cleaner.clean_text()

    cleaner.export_cleaned_dataset()

    print(

        "\n Cleaning "

        "Completed Successfully"

    )


if __name__ == "__main__":

    main()
