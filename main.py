import tkinter as tk
import random
import string

def generate_email_variations(email, num_variations):
    variations = []
    for _ in range(num_variations):
        random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        generated_email = f"{email.split('@')[0]}+{random_string}@{email.split('@')[1]}"
        variations.append(generated_email)
    return variations

def save_to_file(email_variations):
    with open("results.txt", "w") as file:
        for variation in email_variations:
            file.write(variation + '\n')

def generate_emails():
    email = email_entry.get()
    num_variations = int(variations_entry.get())
    
    email_variations = generate_email_variations(email, num_variations)
    
    save_to_file(email_variations)

# Create the main window
window = tk.Tk()
window.title("Email Generator v1.0 by 13marcell13")

# Email Entry
email_label = tk.Label(window, text="Enter your email:")
email_label.pack()

email_entry = tk.Entry(window)
email_entry.pack()

# Variations Entry
variations_label = tk.Label(window, text="Number of variations:")
variations_label.pack()

variations_entry = tk.Entry(window)
variations_entry.pack()

# Generate Button
generate_button = tk.Button(window, text="Generate", command=generate_emails)
generate_button.pack()

# Run the main loop
window.mainloop()