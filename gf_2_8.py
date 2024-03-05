import tkinter as tk
from tkinter import ttk

def gf_mult(a, b):
    """
    Multiply two 8-bit numbers in GF(2^8) using the irreducible polynomial 0x11B.
    """
    # Initialize the result
    result = 0
    # Iterate through all bits of b
    for bit in range(8):
        # If the current bit of b is set, add (XOR) a to the result
        if b & (1 << bit):
            result ^= a << bit
    # Modular reduction by the irreducible polynomial 0x11B
    for bit in range(15, 7, -1):
        if result & (1 << bit):
            # If bit is set, reduce it by the irreducible polynomial shifted accordingly
            result ^= 0x11B << (bit - 8)
    # Ensure the result fits in 8 bits
    return result & 0xFF

def calculate_result():
    a_hex = entry_a.get()
    b_hex = entry_b.get()
    a = int(a_hex, 16)
    b = int(b_hex, 16)
    result = gf_mult(a, b)
    result_label.config(text=f"Result (in hex): {result:02X}")

# Create the main window
root = tk.Tk()
root.title("GF(2^8) Multiplication")

# Create and pack the widgets
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_a = ttk.Label(frame, text="Enter A in hex (e.g., '1A'):")
label_a.grid(column=0, row=0, sticky=tk.W, pady=2)
entry_a = ttk.Entry(frame, width=10)
entry_a.grid(column=1, row=0, sticky=(tk.W, tk.E), pady=2)

label_b = ttk.Label(frame, text="Enter B in hex (e.g., '03'):")
label_b.grid(column=0, row=1, sticky=tk.W, pady=2)
entry_b = ttk.Entry(frame, width=10)
entry_b.grid(column=1, row=1, sticky=(tk.W, tk.E), pady=2)

calculate_button = ttk.Button(frame, text="Calculate", command=calculate_result)
calculate_button.grid(column=0, row=2, columnspan=2, pady=5)

result_label = ttk.Label(frame, text="Result (in hex): ")
result_label.grid(column=0, row=3, columnspan=2, sticky=tk.W, pady=2)

# Run the application
root.mainloop()
