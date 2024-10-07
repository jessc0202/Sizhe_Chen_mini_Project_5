"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,ingred_FPro,avg_FPro_products,avg_distance_root,ingred_normalization_term,semantic_tree_name,semantic_tree_node
"""

import sqlite3
import csv
import os


# load the csv file and insert into a new sqlite3 database
def load(
    dataset="/Users/chensi/Desktop/MIDS/Fall 2024/IDS 706/drug-use-by-age.csv",
):
    """ "Transforms and Loads data into the local SQLite3 database"""

    # prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    conn = sqlite3.connect("DrugUseDB.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS DrugUseDB")
    c.execute(
        """
            CREATE TABLE DrugUseDB (
                age TEXT, 
                n INTEGER,
                alcohol_use REAL,
                alcohol_frequency REAL,
                marijuana_use REAL,
                marijuana_frequency REAL,
                cocaine_use REAL,
                cocaine_frequency TEXT,
                crack_use REAL,
                crack_frequency TEXT,
                heroin_use REAL,
                heroin_frequency TEXT,
                hallucinogen_use REAL,
                hallucinogen_frequency TEXT,
                inhalant_use REAL,
                inhalant_frequency TEXT,
                pain_reliever_use REAL,
                pain_reliever_frequency TEXT,
                oxycontin_use REAL,
                oxycontin_frequency REAL,
                tranquilizer_use REAL,
                tranquilizer_frequency REAL,
                stimulant_use REAL,
                stimulant_frequency REAL,
                meth_use REAL,
                meth_frequency TEXT,
                sedative_use REAL,
                sedative_frequency REAL
            )
        """
    )

    # insert
    c.executemany(
        """
        INSERT INTO DrugUseDB (
                age, n, alcohol_use, alcohol_frequency, marijuana_use, marijuana_frequency, cocaine_use, 
                cocaine_frequency, crack_use, crack_frequency, heroin_use, heroin_frequency, 
                hallucinogen_use, hallucinogen_frequency, inhalant_use, inhalant_frequency, 
                pain_reliever_use, pain_reliever_frequency, oxycontin_use, oxycontin_frequency, 
                tranquilizer_use, tranquilizer_frequency, stimulant_use, stimulant_frequency, meth_use, 
                meth_frequency, sedative_use, sedative_frequency
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        payload,
    )
    conn.commit()
    conn.close()
    return "DrugUseDB.db"
