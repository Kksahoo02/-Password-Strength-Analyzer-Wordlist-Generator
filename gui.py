import tkinter as tk
from tkinter import messagebox
from pass_strength import analyze_password_strength, generate_wordlist  # Import the functions from your script

# Function to analyze password strength
def analyze_password():
    password = password_entry.get()  # Get the password input
    strength = analyze_password_strength(password)  # Call the function to analyze the password
    strength_label.config(text=f"Password Strength: {strength}")  # Display strength result

# Function to generate custom wordlist
def generate_custom_wordlist():
    name = name_entry.get()  # Get the name input
    date = date_entry.get()  # Get the date input
    pet = pet_entry.get()  # Get the pet's name input
    
    if not name or not date or not pet:
        messagebox.showerror("Input Error", "Please fill all fields to generate the wordlist.")
        return
    
    wordlist = generate_wordlist(name, date, pet)  # Call the function to generate wordlist
    wordlist_text.delete(1.0, tk.END)  # Clear previous text in wordlist text box
    for word in wordlist:
        wordlist_text.insert(tk.END, word + "\n")  # Display the generated wordlist

# Create main window
root = tk.Tk()
root.title("Password Strength Analyzer and Wordlist Generator")

# Create and place input fields for password
password_label = tk.Label(root, text="Enter your password:")
password_label.pack(pady=5)
password_entry = tk.Entry(root, width=40, show="*")
password_entry.pack(pady=5)

# Create button to analyze password strength
analyze_button = tk.Button(root, text="Analyze Strength", command=analyze_password)
analyze_button.pack(pady=10)

# Label to display password strength result
strength_label = tk.Label(root, text="Password Strength: ", font=("Helvetica", 12))
strength_label.pack(pady=5)

# Create input fields for custom wordlist
name_label = tk.Label(root, text="Enter your name:")
name_label.pack(pady=5)
name_entry = tk.Entry(root, width=40)
name_entry.pack(pady=5)

date_label = tk.Label(root, text="Enter a memorable date (e.g., year):")
date_label.pack(pady=5)
date_entry = tk.Entry(root, width=40)
date_entry.pack(pady=5)

pet_label = tk.Label(root, text="Enter your pet's name:")
pet_label.pack(pady=5)
pet_entry = tk.Entry(root, width=40)
pet_entry.pack(pady=5)

# Button to generate wordlist
generate_button = tk.Button(root, text="Generate Custom Wordlist", command=generate_custom_wordlist)
generate_button.pack(pady=10)

# Text box to display the generated wordlist
wordlist_label = tk.Label(root, text="Generated Wordlist:")
wordlist_label.pack(pady=5)
wordlist_text = tk.Text(root, width=40, height=10)
wordlist_text.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
