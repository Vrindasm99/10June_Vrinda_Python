# RepairMate - Simple Desktop App for TechRepair Hub
# Demonstrates: Classes, File I/O, SQLite, Regex, Exception Handling, Tkinter

import tkinter as tk
from tkinter import messagebox
import sqlite3, re

# =================== Database Setup ===================
def init_db():
    conn = sqlite3.connect("repairmate.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS customers
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT, phone TEXT, email TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS repairs
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  customer_id INTEGER, device TEXT, issue TEXT,
                  technician TEXT, status TEXT)''')
    conn.commit()
    conn.close()

# =================== Classes ===================
class Customer:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def save(self):
        conn = sqlite3.connect("repairmate.db")
        c = conn.cursor()
        c.execute("INSERT INTO customers(name, phone, email) VALUES (?, ?, ?)",
                  (self.name, self.phone, self.email))
        conn.commit()
        conn.close()

class RepairOrder:
    def __init__(self, cust_id, device, issue, technician, status):
        self.cust_id = cust_id
        self.device = device
        self.issue = issue
        self.technician = technician
        self.status = status

    def save(self):
        conn = sqlite3.connect("repairmate.db")
        c = conn.cursor()
        c.execute("""INSERT INTO repairs(customer_id, device, issue, technician, status)
                     VALUES (?, ?, ?, ?, ?)""",
                     (self.cust_id, self.device, self.issue, self.technician, self.status))
        conn.commit()
        conn.close()

class Billing:
    def __init__(self, parts_cost, service_cost, tax_rate=0.18):
        self.parts_cost = parts_cost
        self.service_cost = service_cost
        self.tax_rate = tax_rate

    def calculate_total(self):
        try:
            subtotal = float(self.parts_cost) + float(self.service_cost)
            tax = subtotal * self.tax_rate
            return subtotal + tax
        except ValueError:
            raise Exception("Invalid cost values entered!")

    def save_invoice(self, customer_name):
        total = self.calculate_total()
        with open(f"{customer_name}_invoice.txt", "w") as f:
            f.write(f"Invoice for {customer_name}\nTotal: ₹{total}\n")
        return total

# =================== Regex Search ===================
def regex_search(pattern):
    conn = sqlite3.connect("repairmate.db")
    c = conn.cursor()
    c.execute("SELECT * FROM repairs")
    matches = []
    for row in c.fetchall():
        if re.search(pattern, row[5], re.IGNORECASE):  # status column
            matches.append(row)
    conn.close()
    return matches

# =================== GUI ===================
class RepairMateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RepairMate - TechRepair Hub")

        tk.Label(root, text="Customer Name").grid(row=0, column=0)
        tk.Label(root, text="Phone").grid(row=1, column=0)
        tk.Label(root, text="Email").grid(row=2, column=0)

        self.name = tk.Entry(root)
        self.phone = tk.Entry(root)
        self.email = tk.Entry(root)

        self.name.grid(row=0, column=1)
        self.phone.grid(row=1, column=1)
        self.email.grid(row=2, column=1)

        tk.Button(root, text="Add Customer", command=self.add_customer).grid(row=3, column=0, columnspan=2, pady=10)

    def add_customer(self):
        try:
            cust = Customer(self.name.get(), self.phone.get(), self.email.get())
            cust.save()
            messagebox.showinfo("Success", "Customer added successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# =================== Run App ===================
if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    app = RepairMateApp(root)
    root.mainloop()
