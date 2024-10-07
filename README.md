[![CI](https://github.com/jessc0202/Sizhe_Chen_mini_Project_5/actions/workflows/cicd.yml/badge.svg)](https://github.com/jessc0202/Sizhe_Chen_mini_Project_5/actions/workflows/cicd.yml)

# Drug Use Data Project

This project extracts, transforms, and loads (ETL) drug use data from a CSV file into an SQLite database. It includes functions to handle the creation of the database, table schema, data insertion, and extraction.

- **Database Schema**:
The SQLite database (`DrugUseDB.db`) is created with a table named `DrugUseDB`. The table schema includes the following columns:

- **`age`** (`TEXT`): Represents the age group in the dataset.
- **`n`** (`INTEGER`): Number of individuals in the specified age group.
- **`alcohol_use`** (`REAL`): Percentage of individuals who have used alcohol.
- **`alcohol_frequency`** (`REAL`): Frequency of alcohol use within the age group.
- **`marijuana_use`** (`REAL`): Percentage of individuals who have used marijuana.
- **`marijuana_frequency`** (`REAL`): Frequency of marijuana use within the age group.
- **`cocaine_use`** (`REAL`): Percentage of individuals who have used cocaine.
- **`cocaine_frequency`** (`TEXT`): Frequency of cocaine use within the age group.
- **`crack_use`** (`REAL`): Percentage of individuals who have used crack.
- **`crack_frequency`** (`TEXT`): Frequency of crack use within the age group.
- **`heroin_use`** (`REAL`): Percentage of individuals who have used heroin.
- **`heroin_frequency`** (`TEXT`): Frequency of heroin use within the age group.
- **`hallucinogen_use`** (`REAL`): Percentage of individuals who have used hallucinogens.
- **`hallucinogen_frequency`** (`TEXT`): Frequency of hallucinogen use within the age group.
- **`inhalant_use`** (`REAL`): Percentage of individuals who have used inhalants.
- **`inhalant_frequency`** (`TEXT`): Frequency of inhalant use within the age group.
- **`pain_reliever_use`** (`REAL`): Percentage of individuals who have used pain relievers.
- **`pain_reliever_frequency`** (`TEXT`): Frequency of pain reliever use within the age group.
- **`oxycontin_use`** (`REAL`): Percentage of individuals who have used OxyContin.
- **`oxycontin_frequency`** (`REAL`): Frequency of OxyContin use within the age group.
- **`tranquilizer_use`** (`REAL`): Percentage of individuals who have used tranquilizers.
- **`tranquilizer_frequency`** (`REAL`): Frequency of tranquilizer use within the age group.
- **`stimulant_use`** (`REAL`): Percentage of individuals who have used stimulants.
- **`stimulant_frequency`** (`REAL`): Frequency of stimulant use within the age group.
- **`meth_use`** (`REAL`): Percentage of individuals who have used methamphetamine.
- **`meth_frequency`** (`TEXT`): Frequency of methamphetamine use within the age group.
- **`sedative_use`** (`REAL`): Percentage of individuals who have used sedatives.
- **`sedative_frequency`** (`REAL`): Frequency of sedative use within the age group.

## Requirements

- Python 3.x
- `sqlite3` (Standard library)
- `csv` (Standard library)
- `os` (Standard library)
- `requests` (If you use the `extract` function to fetch data from a URL)

## Files

- `main.py`: The main script containing the `load` and `extract` functions.
- `drug-use-by-age.csv`: The CSV file containing the drug use data by age (This can be downloaded using the `extract` function or provided locally).

## Function Overview

### 1. `load()`
This function loads data from a CSV file and inserts it into an SQLite database (`DrugUseDB.db`). 

- **Parameters**:
  - `dataset` (str): Path to the CSV file. The default path is `"/Users/chensi/Desktop/MIDS/Fall 2024/IDS 706/drug-use-by-age.csv"`.

- **Process**:
  1. Prints the current working directory.
  2. Reads the specified CSV file.
  3. Connects to an SQLite database (`DrugUseDB.db`). If the database does not exist, it will be created.
  4. Drops the `DrugUseDB` table if it exists to ensure a fresh start.
  5. Creates a new table named `DrugUseDB` with columns such as `age`, `n`, `alcohol_use`, `marijuana_use`, etc., to store drug use statistics.
  6. Inserts rows from the CSV file into the database using `executemany`.
  7. Commits the changes and closes the database connection.
  
- **Returns**: A string `"DrugUseDB.db"` indicating the database file created.

### 2. `extract()`
- **Parameters**:
  - `url` (str): URL of the CSV file to download.
  - `file_path` (str): Path to save the downloaded file.

### 3. `query()`

This function performs multiple database operations on the `DrugUseDB.db` SQLite database, including querying, inserting, updating, and deleting records.

- **Purpose**: To demonstrate how to interact with the SQLite database by performing various SQL operations.

#### Operations Performed

1. **SELECT**:
    - Queries the entire `DrugUseDB` table and prints all the current records to the console.
    - This is useful for inspecting the contents of the database before making any changes.

2. **INSERT**:
    - Before inserting new data, it checks if a record with `age = '11'` and `n = 1000` already exists in the table using:
      ```sql
      SELECT COUNT(*) FROM DrugUseDB WHERE age = '11' AND n = 1000
      ```
    - If no such record exists (i.e., the count is 0), it performs an `INSERT` operation to add a new record with the specified values:
      ```python
      '11', 1000, 60.0, 5.0, 25.0, 4.0, 2.0, '3.0', 1.0, '2.0', 0.5, 
      '1.0', 0.3, '2.0', 0.2, '1.5', 0.4, '3.0', 0.2, '2.5', 0.3, 
      '3.5', 0.5, '4.0', 0.1, '2.0', 0.2, '2.5'
      ```
    - This step ensures that duplicate records are not inserted into the table.

3. **UPDATE**:
    - Updates an existing record in the table where `age = '12'`.
    - Sets the values of `alcohol_use` to `70.0` and `marijuana_use` to `30.0`:
      ```sql
      UPDATE DrugUseDB 
      SET alcohol_use = 70.0, marijuana_use = 30.0
      WHERE age = '12'
      ```

4. **DELETE**:
    - Deletes a record from the table where `age = '21'`:
      ```sql
      DELETE FROM DrugUseDB 
      WHERE age = '21'
      ```
    - This operation removes specific records from the table based on the given condition.

5. **Commit Changes**:
    - Commits all changes to the database to ensure that the `INSERT`, `UPDATE`, and `DELETE` operations are saved.

6. **Close Connection**:
    - Closes the connection to the database to free up resources.

- **Returns**: A string `"Success"` indicating that all operations were completed successfully.


