# Used Cars EDA and Business Questions

This repository contains a Jupyter notebook for exploratory analysis of Craigslist used-vehicle listings. The notebook asks questions about vehicle type, title status, condition, listing dates, odometer readings, and fuel type.

## Dataset

The notebook expects the `vehicles.csv` file from the [Craigslist carstrucks-data dataset on Kaggle](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data). **The dataset is not included in this repository.** Obtain it through Kaggle and comply with the dataset's terms before using it. Do not commit the CSV: it contains listing data and can be large.

By default, the notebook looks for `data/vehicles.csv`, then `vehicles.csv` in the repository root, and then the Kaggle path `/kaggle/input/craigslist-carstrucks-data/vehicles.csv`. To use another location, set `USED_CARS_CSV` to the full path of the CSV file before starting Jupyter, for example:

```bash
export USED_CARS_CSV="$HOME/datasets/vehicles.csv"
```

If the file cannot be found, the notebook reports the supported locations rather than failing on a hard-coded Kaggle-only directory.

## Run the notebook

1. Use Python 3.11 or newer with Jupyter installed (the pinned pandas release requires Python 3.11+).
2. Install the analysis libraries used by the notebook:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Download the dataset and either put it in `data/vehicles.csv` or set `USED_CARS_CSV`.
4. Start Jupyter from the repository root and open `vehicles-EDA.ipynb`.
5. Run the cells from top to bottom.

The notebook intentionally keeps missing values missing instead of replacing them with global means or the most common category. Pandas aggregations and plots generally omit missing values; inspect the missing-value summary before interpreting results. The posting-time analysis uses the listing's `posting_date`, not the vehicle's model year.

## Repository contents

- `vehicles-EDA.ipynb` — exploratory analysis notebook; saved cell outputs are cleared to avoid shipping large or potentially sensitive listing data.
- `requirements.txt` — pinned versions of the notebook's analysis libraries.

## Limitations

The dataset is external and is not vendored, so a full notebook run is not possible from a fresh clone until the user obtains it. No performance, market conclusion, or result in this README is represented as independently validated. Listings are historical scraped data and may be incomplete, duplicated, or otherwise unrepresentative; the analyses are descriptive, not valuation advice.
