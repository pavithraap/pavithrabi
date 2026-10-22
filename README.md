# Python Data Analysis Projects

This repository contains two standalone data-analysis scripts:

- `project 1.py` analyzes student placement data and exports a cleaned CSV.
- `pro-2.py` cleans and analyzes e-commerce order data and displays a chart.

## Requirements

- Python 3.9 or newer
- The CSV dataset needed by the script you want to run

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Place your authorized dataset beside the scripts, then run the matching script:

```powershell
python "project 1.py"
python "pro-2.py"
```

`project 1.py` expects
`Student_Placement_Analyst_Project FE Added and cleaned file.csv`.
`pro-2.py` expects `ecommerce_dirty_dataset_375_rows file.csv task 1.csv`.

The datasets are not included in this repository. Keep them private and place
your authorized local copies beside the scripts. The placement script writes
`student_placement_final_analysis.csv`; CSV datasets and generated CSV output
are excluded from Git by `.gitignore`.
