import tkinter as tk
import pyjokes

def click_button(gen):
    value = next(gen)
    text_widget.delete("1.0", tk.END)  # Clear the text widget
    text_widget.insert(tk.END, value)  # Insert the joke

root = tk.Tk()
root.title("Jokes Generator")
root.geometry("400x500")  # Set window size

# Multiline Text widget
text_widget = tk.Text(root, wrap="word", font=("Arial", 16), relief="solid", bd=6)
text_widget.grid(row=0, column=0, columnspan=4, rowspan=5, sticky="nsew", padx=20, pady=20)

# Create button and configure grid
button = tk.Button(root, text="Get Joke", font=("Arial", 16), command=lambda t=pyjokes.forever(): click_button(t))
button.grid(row=0, column=4, rowspan=5, sticky="nsew")

for i in range(5):  # 5 rows
    root.grid_rowconfigure(i, weight=1)
for i in range(4):  # 4 columns
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
