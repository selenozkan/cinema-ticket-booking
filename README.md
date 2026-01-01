# Cinema Ticket Booking (Python + SQLite)

This is a small **toy project** that focuses on applying **Python OOP concepts** together with **basic SQL (SQLite)** in a realistic but manageable scenario.

---

## 📌 Project Overview

This application is a simple cinema ticket booking system:

- Seats are stored in a SQLite database (`cinema.db`)
- Each seat has: a seat ID (A1, A2, B1, etc.); a taken/free status; a price
- The user can: view all seats with prices and availability; choose a seat and buy a ticket if the seat is free
- A PDF ticket is generated after a successful purchase

---

## 🎯 Learning Goals

- **Python Object-Oriented Programming**: classes and objects, responsibility separation (`User`, `Seat`, `Ticket`)
- **SQLite (SQL basics)** :  `CREATE TABLE`,  `SELECT`, `INSERT`, `UPDATE`
- **Basic application flow**:  user input, validation, persistent state using a database
- **Using external libraries**: PDF generation with `fpdf`
---

## 📂 Project Structure

```
.
├── main.py        # Main application logic
├── dbprep.py      # Prepares and seeds the cinema.db database
├── cinema.db      # SQLite database (seats, prices, availability)
├── ticket.pdf     # Example generated ticket
├── test.py        # Simple python functions to handle dataabase
└── README.md
```

---

## ▶️ How to Run

1. (Optional) Reset and prepare the database:
   ```bash
   python dbprep.py
   ```

2. Run the main program:
   ```bash
   python main.py
   ```

3. After a successful purchase of cinema ticket, a `ticket.pdf` file will be generated.

---

## Notes
- This is a learning project, the focus is clarity and practice, not optimization
- Error handling and database design are intentionally simple (no advanced sql features used)

---

This project is developed as a part of [Udemy course](https://www.udemy.com/course/the-python-mega-course/)
