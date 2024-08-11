import tkinter as tk
from tkinter import messagebox

# Function to add student data
def add_student():
    name = entry_name.get()
    math = entry_math.get()
    science = entry_science.get()
    english = entry_english.get()
    
    if not name or not math or not science or not english:
        messagebox.showerror("Input Error", "All fields are required")
        return
    
    try:
        math = float(math)
        science = float(science)
        english = float(english)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid marks")
        return
    
    total = math + science + english
    average = total / 3
    
    student_data[name] = {
        "Math": math,
        "Science": science,
        "English": english,
        "Total": total,
        "Average": average
    }
    
    messagebox.showinfo("Success", f"Data for {name} added successfully!")
    clear_entries()

# Function to clear input fields
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_math.delete(0, tk.END)
    entry_science.delete(0, tk.END)
    entry_english.delete(0, tk.END)

# Function to display report
def show_report():
    if not student_data:
        messagebox.showinfo("No Data", "No student data available")
        return
    
    report_window = tk.Toplevel(root)
    report_window.title("Student Marks Report")
    report_window.geometry("400x300")
    
    report_text = tk.Text(report_window, font=('Arial', 12))
    report_text.pack(expand=True, fill='both')
    
    for name, data in student_data.items():
        report_text.insert(tk.END, f"Name: {name}\n")
        report_text.insert(tk.END, f"Math: {data['Math']}\n")
        report_text.insert(tk.END, f"Science: {data['Science']}\n")
        report_text.insert(tk.END, f"English: {data['English']}\n")
        report_text.insert(tk.END, f"Total: {data['Total']}\n")
        report_text.insert(tk.END, f"Average: {data['Average']:.2f}\n")
        report_text.insert(tk.END, "-"*30 + "\n")

# Main application setup
root = tk.Tk()
root.title("Modern Student Marks Report")
root.geometry("400x400")
root.configure(background="lightgray")

student_data = {}

# Labels and entry fields
tk.Label(root, text="Student Name", font=('Arial', 14), bg="lightgray").pack(pady=10)
entry_name = tk.Entry(root, font=('Arial', 14), width=20)
entry_name.pack()

tk.Label(root, text="Math Marks", font=('Arial', 14), bg="lightgray").pack(pady=10)
entry_math = tk.Entry(root, font=('Arial', 14), width=20)
entry_math.pack()

tk.Label(root, text="Science Marks", font=('Arial', 14), bg="lightgray").pack(pady=10)
entry_science = tk.Entry(root, font=('Arial', 14), width=20)
entry_science.pack()

tk.Label(root, text="English Marks", font=('Arial', 14), bg="lightgray").pack(pady=10)
entry_english = tk.Entry(root, font=('Arial', 14), width=20)
entry_english.pack()

# Buttons to add data and show report
tk.Button(root, text="Add Student", font=('Arial', 14), bg="lightblue", command=add_student).pack(pady=20)
tk.Button(root, text="Show Report", font=('Arial', 14), bg="lightgreen", command=show_report).pack(pady=10)

# Run the main event loop
root.mainloop()
