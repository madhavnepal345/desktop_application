import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

def connect_db():
    return sqlite3.connect('employees.db')

class EmployeeManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("1000x1000")

        # Widgets for employee details
        self.name_label = tk.Label(root, text="Name")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.age_label = tk.Label(root, text="Age")
        self.age_label.grid(row=1, column=0, padx=10, pady=10)
        self.age_entry = tk.Entry(root)
        self.age_entry.grid(row=1, column=1, padx=10, pady=10)

        self.department_label = tk.Label(root, text="Department")
        self.department_label.grid(row=2, column=0, padx=10, pady=10)
        self.department_entry = tk.Entry(root)
        self.department_entry.grid(row=2, column=1, padx=10, pady=10)

        self.position_label = tk.Label(root, text="Position")
        self.position_label.grid(row=3, column=0, padx=10, pady=10)
        self.position_entry = tk.Entry(root)
        self.position_entry.grid(row=3, column=1, padx=10, pady=10)

        # Buttons for actions
        self.add_button = tk.Button(root, text="Add Employee", command=self.add_employee)
        self.add_button.grid(row=4, column=0, padx=10, pady=10)

        self.view_button = tk.Button(root, text="View Employees", command=self.view_employees)
        self.view_button.grid(row=4, column=1, padx=10, pady=10)

        self.update_button = tk.Button(root, text="Update Employee", command=self.update_employee)
        self.update_button.grid(row=4, column=2, padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Delete Employee", command=self.delete_employee)
        self.delete_button.grid(row=4, column=3, padx=10, pady=10)

        # Treeview to display employees
        self.tree = ttk.Treeview(root, columns=("ID", "Name", "Age", "Department", "Position"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Department", text="Department")
        self.tree.heading("Position", text="Position")
        self.tree.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

    def add_employee(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        department = self.department_entry.get()
        position = self.position_entry.get()

        if name and age and department and position:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO employees (name, age, department, position) VALUES (?, ?, ?, ?)",
                           (name, age, department, position))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Employee added successfully")
            self.view_employees()
        else:
            messagebox.showwarning("Input error", "Please fill all fields")

    def view_employees(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees")
        rows = cursor.fetchall()
        conn.close()

        for row in self.tree.get_children():
            self.tree.delete(row)

        for row in rows:
            self.tree.insert("", "end", values=row)

    def update_employee(self):
        selected_item = self.tree.selection()[0]
        selected_id = self.tree.item(selected_item)['values'][0]

        name = self.name_entry.get()
        age = self.age_entry.get()
        department = self.department_entry.get()
        position = self.position_entry.get()

        if name and age and department and position:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("UPDATE employees SET name=?, age=?, department=?, position=? WHERE id=?",
                           (name, age, department, position, selected_id))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Employee updated successfully")
            self.view_employees()
        else:
            messagebox.showwarning("Input error", "Please fill all fields")

    def delete_employee(self):
        selected_item = self.tree.selection()[0]
        selected_id = self.tree.item(selected_item)['values'][0]

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employees WHERE id=?", (selected_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Employee deleted successfully")
        self.view_employees()

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManagementSystem(root)
    root.mainloop()
