import tkinter as tk
from tkinter import filedialog

def calculate_gc_content(sequence):
    gc_count = sequence.count('G') + sequence.count('C')
    total_bases = len(sequence)
    gc_content = (gc_count / total_bases) * 100 if total_bases > 0 else 0
    return gc_content

def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt")])
    if file_path:
        calculate_and_display_gc_content(file_path)

def calculate_and_display_gc_content(file_path):
    with open(file_path, 'r') as file:
        sequence = file.read().upper()
        result = calculate_gc_content(sequence)
        result_text.set(f'GC Content: {result:.2f}%')

def clear_result():
    result_text.set("")
    file_path_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("GC Content Calculator with File Handling")

# Set window dimensions and center on screen
window_width = 400
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

# Create and pack widgets
tk.Label(root, text="GC Content Calculator", font=("Helvetica", 16, "bold")).pack(pady=10)

open_file_button = tk.Button(root, text="Open File", command=open_file_dialog, padx=10, pady=5, bg="#4CAF50", fg="white")
open_file_button.pack(pady=10)

calculate_button = tk.Button(root, text="Calculate GC Content", command=lambda: calculate_and_display_gc_content(file_path_entry.get()), padx=10, pady=5, bg="#008CBA", fg="white")
calculate_button.pack(pady=5)

file_path_entry = tk.Entry(root, width=40)
file_path_entry.pack(pady=5)

clear_button = tk.Button(root, text="Clear Result", command=clear_result, padx=10, pady=5, bg="#FF5733", fg="white")
clear_button.pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Helvetica", 12))
result_label.pack(pady=10)

# Start the main loop
root.mainloop()
