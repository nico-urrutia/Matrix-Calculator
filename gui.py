import tkinter as tk
from tkinter import messagebox
from fractions import Fraction
from matrix_f import Matrix

def parse_matrix(text):
    try:
        rows = text.strip().split("\n")
        matrix = [list(map(Fraction, row.split())) for row in rows]
        return matrix
    except:
        return None

def start_app():
    def perform_operation(op):
        text = input_box.get("1.0", tk.END).strip()
        matrix = parse_matrix(text)
        if matrix is None:
            messagebox.showerror("Error", "Invalid matrix format.")
            return
        M = Matrix(matrix)
        try:
            if op == "transpose":
                result = M.transpose_m().data
            elif op == "det_rec":
                result = M.determinante_rec()
            elif op == "det_tri":
                result = M.determinante_tri()
            elif op == "rank":
                result = M.rank_gauss()
            elif op == "inverse_gauss_jordan":
                result = M.inverse_gauss_jordan()
            else:
                result = ""
            output_box.config(state="normal")
            output_box.delete("1.0", tk.END)
            try:
                for line in result:
                    for elem in line:
                        output_box.insert(tk.END, f"{elem} ")
                    output_box.insert(tk.END, "\n")
            except TypeError:
                output_box.insert(tk.END, str(result))
            output_box.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    window = tk.Tk()
    window.title("Matrix Calculator")
    window.iconbitmap("matrix_icon_215545.ico") 
    window.geometry("600x600")     

    label = tk.Label(window, text="Enter matrix (rows separated by newlines, elements by spaces):")
    label.pack(pady=5)

    input_box = tk.Text(window, width=50, height=10)
    input_box.pack()

    buttons_frame = tk.Frame(window)
    buttons_frame.pack(pady=10)

    button_height = 1 
    button_width = 25
    tk.Button(buttons_frame, width=button_width, height=button_height, text="Transpose", command=lambda: perform_operation("transpose")).grid(row=0, column=0, padx=5, pady=2)
    tk.Button(buttons_frame, width=button_width, height=button_height, text="Determinant (recursive)", command=lambda: perform_operation("det_rec")).grid(row=0, column=1, padx=5, pady=2)
    tk.Button(buttons_frame, width=button_width, height=button_height, text="Determinant (triangular)", command=lambda: perform_operation("det_tri")).grid(row=1, column=0, padx=5, pady=2)
    tk.Button(buttons_frame, width=button_width, height=button_height, text="Rank", command=lambda: perform_operation("rank")).grid(row=2, column=0, padx=5, pady=2)
    tk.Button(buttons_frame, width=button_width, height=button_height, text="Inverse (By Gauss-Jordan)", command=lambda: perform_operation("inverse_gauss_jordan")).grid(row=2, column=1, padx=5, pady=2)

    tk.Label(window, text="Result:").pack(pady=5)

    output_box = tk.Text(window, width=50, height=10, state="disabled")
    output_box.pack()

    tk.Button(window, text="Clear", command=lambda: input_box.delete("1.0", tk.END)).pack(pady=5)

    window.mainloop()
