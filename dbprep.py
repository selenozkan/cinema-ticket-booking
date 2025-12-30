"""
Prepare (or reset) cinema.db with seats, taken flags, and prices.
    seat_id:  A1 A2 A3  B1 B2 B3  C1 C2 C3
    taken:  1 for A1, A3, B3, C1; 0 for the rest
    price: A cheapest, B mid, C most expensive (all within 90–120 range)
"""

import sqlite3

db_path = "cinema.db"

def create_table():
    """Create Seat table if it does not exist."""
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Seat (
            seat_id TEXT,
            taken INTEGER,
            price INTEGER
        )
    """)

    connection.commit()
    connection.close()


def clear_table():
    """Remove all existing seats."""
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM Seat")

    connection.commit()
    connection.close()


def insert_seats():
    """Insert all seats with taken status and prices."""
    seats = {
        "A1": (1, 90),
        "A2": (0, 95),
        "A3": (1, 98),

        "B1": (0, 105),
        "B2": (0, 110),
        "B3": (1, 112),

        "C1": (1, 115),
        "C2": (0, 118),
        "C3": (0, 120),
    }

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    for seat_id, (taken, price) in seats.items():
        cursor.execute(
            "INSERT INTO Seat VALUES (?, ?, ?)",
            (seat_id, taken, price)
        )

    connection.commit()
    connection.close()


def prepare_database():
    create_table()
    clear_table()
    insert_seats()
    print("cinema.db prepared successfully!")


if __name__ == "__main__":
    prepare_database()