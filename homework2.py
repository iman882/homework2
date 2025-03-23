import tkinter as tk
import numpy as np

class MultiplierModel:
    def __init__(self, multiplier):
        self.multiplier = np.array(multiplier, dtype=np.float64) 

    def multiply(self, value):
        value_np = np.array(value, dtype=np.float64) 
        return np.multiply(value_np, self.multiplier)  

class MultiplierView:
    def __init__(self, window):
        self.model = MultiplierModel(1)  
        window.title("Multiplier")

        tk.Label(window, text="Enter a Number:").grid(row=0, column=0)
        self.value_entry = tk.Entry(window)
        self.value_entry.grid(row=0, column=1)

        tk.Label(window, text="Enter Multiplier:").grid(row=1, column=0)
        self.multiplier_entry = tk.Entry(window)
        self.multiplier_entry.grid(row=1, column=1)

        self.calculate_btn = tk.Button(window, text="Multiply", command=self.calculate_multiplication)
        self.calculate_btn.grid(row=2, column=0, columnspan=2)

        self.result_lbl = tk.Label(window, text="Result: -")
        self.result_lbl.grid(row=3, column=0, columnspan=2)

    def calculate_multiplication(self):
        value = float(self.value_entry.get())  
        multiplier = float(self.multiplier_entry.get())  
        self.model = MultiplierModel(multiplier)  
        result = self.model.multiply(value)  
        self.result_lbl.config(text=f"Result: {result}")  
if __name__ == "__main__":
    window = tk.Tk()
    view = MultiplierView(window)
    window.mainloop()
