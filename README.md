# Parch and Posey ETL Project

## Overview

This project demonstrates a simple **ETL (Extract, Transform, Load)** pipeline built in **Bash**.
It uses the *Annual Enterprise Survey 2023 provisional dataset* from **[stats.govt.nz](https://www.stats.govt.nz/)** as a sample dataset.

The pipeline automates:

1. **Extract** – Download raw data from the source.
2. **Transform** – Clean and restructure selected columns.
3. **Load** – Store transformed data into the final *Gold layer*.

This project can be used as a beginner-friendly ETL framework or adapted for larger data engineering workflows.

---

## Project Structure

Scripts/
│── .gitignore                                   
│── bash_script/
│   ├── destinantion_file
│   ├── my_csv          
│   ├── json-and-csv.sh           
│   ├-- etl.sh
│
│         
│── sql_script/

|── .gitignore
│── .gitkeep
│ 
├──README.md             


---

## Dataset

* **Source**: [Annual Enterprise Survey – 2023 Financial Year (Provisional)](https://www.stats.govt.nz/large-datasets/csv-files-for-download/)
* **Format**: CSV
* **Columns extracted**:

  * year
  * value
  * units
  * variable_code

---

## Usage

### Run the ETL script manually

```bash
bash etl.sh
```

After running, you should see:

* `raw/` → contains the downloaded source file.
* `Transformed/` → contains `new_data.csv` with selected columns.
* `Gold/` → contains the final copy of `new_data.csv`.


## Requirements

* Unix/Linux environment (or Git Bash on Windows)
* `curl` installed
* `awk` installed

---

## Future Enhancements

* Add conversion of CSV files into JSON format.
* Store both JSON and CSV files in a `JSON_and_CSV/` directory.
* Improve error handling and add validation checks.
* Extend transformations to support filtering and aggregations.

---

## Contributing

Contributions are welcome!

* Fork the repo
* Create a feature branch
* Submit a pull request
