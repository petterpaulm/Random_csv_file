# Random CSV Generator

This project provides a Python script for generating csv files with random data. It's designed to allow users to specify the number of columns, the type of each column (string or float), and optionally, the directory where the CSV file will be saved. This tool can be useful for generating datasets for testing, data analysis practice, or other applications where mock data is needed.

## Features

- Generate CSV files with custom number of columns and rows.
- Customize each column to contain wither random strings or floating-point numbers.
- Specify output directory (optional).


## Getting Started

### Prerequisites

- Python 3.11.x or newer.

## Installation

Clone this repo to your local machine

```bash
bash
git clone https://github.com/petterpaulm/random-csv-generator.git
cd random-csv-generator
```

### Usage

To use the script, run it with Python and specify your parameters. Here's an example command:

```bash
python
python generate_random_csv.py --num_columns 5 --column_types string float string float string --file_name my_random_data.csv --directory_path ./data

```

Replace `--num_columns`, `--column_types`, `--file_name`, and `--directory_path` with your desired configuration.
