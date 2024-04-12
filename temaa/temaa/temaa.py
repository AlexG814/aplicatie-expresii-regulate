import tkinter as tk
from tkinter import ttk
import re

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicație cu Expresii Regulate")
        self.geometry("600x500")  # Mărimea ferestrei
        self.setup_ui()

    def setup_ui(self):
        self.style = ttk.Style(self)
        self.configure(bg='#5080a0')  # Setăm culoarea de fundal a ferestrei

        self.style.theme_use('clam')  # Alegem o temă albastru închis, de exemplu 'clam'
        self.style.configure('My.TButton', background='#001f3f', foreground='white', font=('Helvetica', 12))  # Stilizăm butoanele
        self.style.configure('My.TLabel', background='#5080a0', foreground='white', font=('Helvetica', 12))  # Stilizăm etichetele

        self.pattern_label = ttk.Label(self, text="Pattern:", style='My.TLabel')
        self.pattern_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.pattern_input = ttk.Entry(self, width=50)  # Mărimea casetei de text a fost mărită
        self.pattern_input.grid(row=0, column=1, padx=10, pady=10)

        self.text1_label = ttk.Label(self, text="Text 1:", style='My.TLabel')
        self.text1_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.text1_input = tk.Text(self, height=5, width=60)  # Mărimea casetei de text a fost mărită
        self.text1_input.grid(row=1, column=1, padx=10, pady=10)

        self.text2_label = ttk.Label(self, text="Text 2:", style='My.TLabel')
        self.text2_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.text2_input = tk.Text(self, height=10, width=60)  # Mărimea casetei de text a fost mărită
        self.text2_input.grid(row=2, column=1, padx=10, pady=10)

        self.verify_button = ttk.Button(self, text="Verificare", command=self.verificare, style='My.TButton')
        self.verify_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.result_label = ttk.Label(self, text="", style='My.TLabel')
        self.result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.matches_label = ttk.Label(self, text="Match-uri din Text 2:", style='My.TLabel')
        self.matches_label.grid(row=5, column=0, padx=10, pady=10, sticky='w')
        self.matches_text = tk.Text(self, height=10, width=60)  # Mărimea casetei de text a fost mărită
        self.matches_text.grid(row=5, column=1, padx=10, pady=10)

    def verificare(self):
        pattern = self.pattern_input.get()
        text1 = self.text1_input.get("1.0", tk.END).strip()
        text2 = self.text2_input.get("1.0", tk.END)

        try:
            re.compile(pattern)
        except re.error:
            self.result_label.config(text="Pattern-ul este incorect!")
            return

        if re.search(pattern, text1):
            self.result_label.config(text="Textul 1 are match cu pattern-ul!")
        else:
            self.result_label.config(text="Textul 1 nu are match cu pattern-ul.")

        matches = re.findall(pattern, text2)
        self.matches_text.delete("1.0", tk.END)
        for match in matches:
            self.matches_text.insert(tk.END, match + "\n")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
