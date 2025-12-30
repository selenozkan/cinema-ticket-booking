from fpdf import FPDF, XPos, YPos
import random
import string
import sqlite3

db_path = "cinema.db"


class User:
    def __init__(self, name):
        self.name = name

    def buy(self, seat: "Seat"):
        """Try to buy a seat. Returns True if successful."""
        if not seat.exists():
            print(f"Seat {seat.seat_id} does not exist.")
            return False

        if not seat.is_free():
            print("Sorry, the seat is taken. Please try another seat.")
            return False

        if not seat.occupy():
            print("Sorry, the seat was just taken by someone else.")
            return False

        ticket = Ticket(
            user_name=self.name,
            price=seat.get_price(),
            seat_number=seat.seat_id,
        )
        ticket.to_pdf("ticket.pdf")
        print("Purchase successful. Enjoy the movie! ticket.pdf created.")
        return True


class Seat:
    def __init__(self, seat_id, database = db_path):
        self.seat_id = seat_id
        self.database = database

    def exists(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute(
            "SELECT 1 FROM Seat WHERE seat_id = ?", (self.seat_id,)
        )
        result = cursor.fetchone()
        connection.close()
        return result is not None

    def get_price(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute(
            "SELECT price FROM Seat WHERE seat_id = ?", (self.seat_id,)
        )
        price = cursor.fetchone()[0]
        connection.close()
        return price

    def is_free(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute(
            "SELECT taken FROM Seat WHERE seat_id = ?", (self.seat_id,)
        )
        taken = cursor.fetchone()[0]
        connection.close()
        return taken == 0

    def occupy(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE Seat SET taken = 1 WHERE seat_id = ? AND taken = 0",
            (self.seat_id,),
        )
        connection.commit()
        updated = cursor.rowcount == 1
        connection.close()
        return updated

    @staticmethod
    def show_all_seats(database = db_path):
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute(
            "SELECT seat_id, taken, price FROM Seat ORDER BY seat_id"
        )
        seats = cursor.fetchall()
        connection.close()

        print("\nSeats:\n")
        for seat_id, taken, price in seats:
            status = "Free " if taken == 0 else "Taken"
            print(f"{seat_id} - {status} - {price}")
        print()


class Ticket:
    def __init__(self, user_name, price, seat_number):
        self.user_name = user_name
        self.price = price
        self.seat_number = seat_number
        self.ticket_id = self._generate_ticket_id()

    def _generate_ticket_id(self, length= 8):
        chars = string.ascii_uppercase + string.digits
        return "".join(random.choice(chars) for _ in range(length))

    def to_pdf(self, filename):
        pdf = FPDF()
        pdf.add_page()

        pdf.set_font("Helvetica", "B", 24)
        pdf.cell(0,80,"Your Digital Ticket",
            border=1,align="C",new_x=XPos.LMARGIN,new_y=YPos.NEXT,)

        def row(label: str, value: str):
            pdf.set_font("Helvetica", "B", 14)
            pdf.cell(140, 28, label, border=1)
            pdf.set_font("Helvetica", "", 14)
            pdf.cell(0,28,value, border=1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        row("Name:", self.user_name)
        row("Ticket ID:", self.ticket_id)
        row("Price:", str(self.price))
        row("Seat:", self.seat_number)

        pdf.output(filename)


# ------------------------------------------------

if __name__ == "__main__":
    name = input("What is your name? ").strip()
    user = User(name)

    while True:
        Seat.show_all_seats()

        seat_id = input(
            "Choose a seat (A1/A2/A3, B1/B2/B3, C1/C2/C3): ").strip().upper()

        seat = Seat(seat_id)

        success = user.buy(seat)

        if success:
            break
        choice = input(
            "Do you want to check other seats or exit? (c = check, e = exit): ").strip().lower()

        if choice == "e":
            print("Goodbye!")
            break