import sqlite3


def query():
    """Query the database and perform insert, update, and delete operations"""
    conn = sqlite3.connect("DrugUseDB.db")
    cursor = conn.cursor()

    # Perform SELECT
    cursor.execute("SELECT * FROM DrugUseDB")
    print("Current records in DrugUseDB:")
    print(cursor.fetchall())

    # Perform INSERT only if the record does not already exist
    cursor.execute("SELECT COUNT(*) FROM DrugUseDB WHERE age = '11' AND n = 1000")
    if cursor.fetchone()[0] == 0:
        cursor.execute(
            """
            INSERT INTO DrugUseDB (age, n, alcohol_use, alcohol_frequency, marijuana_use, marijuana_frequency, cocaine_use, 
                                   cocaine_frequency, crack_use, crack_frequency, heroin_use, heroin_frequency, 
                                   hallucinogen_use, hallucinogen_frequency, inhalant_use, inhalant_frequency, 
                                   pain_reliever_use, pain_reliever_frequency, oxycontin_use, oxycontin_frequency, 
                                   tranquilizer_use, tranquilizer_frequency, stimulant_use, stimulant_frequency, meth_use, 
                                   meth_frequency, sedative_use, sedative_frequency) 
            VALUES ('11', 1000, 60.0, 5.0, 25.0, 4.0, 2.0, '3.0', 1.0, '2.0', 0.5, '1.0', 0.3, '2.0', 0.2, '1.5', 
                    0.4, '3.0', 0.2, '2.5', 0.3, '3.5', 0.5, '4.0', 0.1, '2.0', 0.2, '2.5')
            """
        )

    # Perform UPDATE
    cursor.execute(
        """
        UPDATE DrugUseDB 
        SET alcohol_use = 70.0, marijuana_use = 30.0
        WHERE age = '12'
        """
    )

    # Perform DELETE
    cursor.execute(
        """
        DELETE FROM DrugUseDB 
        WHERE age = '21'
        """
    )

    conn.commit()  # Ensure all changes are saved
    conn.close()
    return "Success"  # Return success for testing

