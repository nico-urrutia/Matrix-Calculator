# Matrix-Calculator

## Description
Matrix Calculator is a Python program that performs various operations on matrices, including calculating the determinant, rank, inverse, and more. The program provides a graphical user interface built with Tkinter for easy interaction.

---

## About the Developer
🧑‍💻 Developed by Nicolás Urrutia. I'm a student at the University of Deusto, passionate about mathematics and programming. This project is part of my exploration into linear algebra and algorithm implementation.  

📩 Email: nicolas.urrutia@opendeusto.es, nicourru@icloud.com  
🌐 GitHub: [https://github.com/nico-urrutia](https://github.com/nico-urrutia)  
⛓️ LinkedIn: [https://www.linkedin.com/in/nicolas-urrutia-lerena-833465383](https://www.linkedin.com/in/nicolas-urrutia-lerena-833465383)  

---

## Features
- Calculate the determinant of any square matrix
- Compute the rank of a matrix using Gaussian elimination
- Compute the inverse of invertible matrices
- Matrix transpose
- GUI for entering matrices and displaying results

---

## Installation & Requirements
- Install Python 3.9 or higher 🐍  
- No external packages are required; the program uses standard Python libraries (`tkinter` and `fractions`)  
- Clone or download the repository 🐱  

```bash
git clone https://github.com/nico-urrutia/matrix-calculator.git
cd matrix-calculator
```

## How to Run
From the terminal or command prompt:
```bash
python main.py #This launches the GUI.
```
Example Input
```
1 2 3
4 5 6
7 8 9
```
Click the buttons to calculate Determinant, Rank, or Inverse.

```bash
Project Structure
matrix_calculator/
│
├── main.py         # Launches the GUI
├── gui.py          # Tkinter interface for user input and output
└── matrix_f.py     # All matrix operations (determinant, inverse, rank, transpose, etc.)
```

## Known Limitations
- **Main problem:** The recursive determinant calculation fails strangely in specific circumstances.  (For example with fractions)
- Determinant calculation using recursion can be slow for large matrices (n > 8).  
- GUI input is limited to rectangular numeric matrices; invalid inputs may cause errors.  

## Future Improvements
- Fix recursive determinant calculation for matrices containing fractions.  