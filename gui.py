import tkinter as tk
from tkinter import messagebox
from fractions import Fraction
from matrix_f import Matrix
import webbrowser
def parse_matrix(text):
    try:
        rows = text.strip().split("\n")
        matrix = [list(map(Fraction, row.split())) for row in rows]
        return matrix
    except:
        return None

def start_app():
    def open_link(url):
        webbrowser.open(url)
        
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
     
    def show_developer_info():
        info_window = tk.Toplevel(window)
        info_window.title("About the Developer")
        info_window.geometry("950x350")
        info_window.iconbitmap("matrix_icon_215545.ico") 
        info_window.transient(window)
        info_window.grab_set()

        title_label = tk.Label(
            info_window,
            text="About the developer",
            font=("Arial", 14, "bold")
        )
        title_label.pack(pady=10)

        developer_label = tk.Label(
            info_window,
            text=(
                "🧑‍💻Developed by Nicolás Urrutia Lerena.\n"
                "💻I'm a computer science, data science and AI student at the University of Deusto. I'm passionate about mathematics and programming.\n This project is part of my exploration into linear algebra and algorithm implementation.\n"
                "I have been coding since I was 13 years old and I love creating useful applications that solve real-world problems.\n"
                " \n"
                "CONTACT:"
            ),
            justify=tk.LEFT,)
        developer_label.pack(pady=10)
        contact_text = tk.Text(
            info_window,
            width=80,
            height=5,
            borderwidth=0,
            highlightthickness=0,
            font=("TkDefaultFont", 10),
            bg=info_window.cget("bg"),  # same background as window
        )
        contact_text.pack(pady=10, padx=10)

        # Insert the text
        contact_text.insert(tk.END,
            "📩 Email: nicolas.urrutia@opendeusto.es , nicourru@icloud.com\n"
            "🌐 GitHub: https://github.com/nico-urrutia\n"
            "⛓️ LinkedIn: https://www.linkedin.com/in/nicolas-urrutia-lerena-833465383/\n"
        )

        # Disable editing
        contact_text.config(state=tk.DISABLED)

        # Function to add clickable link
        def add_link(tag_name, start, end, url):
            contact_text.tag_add(tag_name, start, end)
            contact_text.tag_config(tag_name, foreground="blue", underline=True)
            contact_text.tag_bind(tag_name, "<Button-1>", lambda e: webbrowser.open(url))

        # Add tags for each clickable part
        # Adjust indices to match the positions in the text
        add_link("email1", "1.10", "1.39", "mailto:nicolas.urrutia@opendeusto.es")
        add_link("email2", "1.42", "1.61", "mailto:nicourru@icloud.com")
        add_link("github", "2.11", "2.end", "https://github.com/nico-urrutia")
        add_link("linkedin", "3.13", "3.end", "https://www.linkedin.com/in/nicolas-urrutia-lerena-833465383/")

        close_button = tk.Button(
            info_window,
            text="Close",
            width=10,
            command=info_window.destroy
        )
        close_button.pack(pady=10)


    tk.Button(window, text="ℹ️Developer Info", command=show_developer_info).pack()

    label = tk.Label(window, text="Enter matrix (rows separated by newlines, elements by spaces):", font=("Arial", 9, "bold"))
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
