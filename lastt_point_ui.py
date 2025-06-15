import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from sympy import symbols, sympify, integrate, latex
from scipy import integrate as scipy_integrate
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

x, y = symbols('x y')

def plot_surface(expr, a, b, c, d, filename="surface_plot.pdf"):
    f_lambdified = lambda x_val, y_val: float(expr.evalf(subs={x: x_val, y: y_val}))
    X, Y = np.meshgrid(np.linspace(a, b, 50), np.linspace(c, d, 50))
    Z = np.vectorize(f_lambdified)(X, Y)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
    ax.set_title(f'Surface Plot of $f(x, y) = {latex(expr)}$', fontsize=14)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

def generate_pdf(content, image="surface_plot.pdf", output="integral_result.pdf"):
    with PdfPages(output) as pdf:
        fig, ax = plt.subplots(figsize=(8.27, 11.69))
        ax.axis('off')
        wrapped = "\n".join(content.splitlines())
        ax.text(0.05, 0.95, wrapped, va='top', ha='left', fontsize=12, family='monospace')
        pdf.savefig(fig)
        plt.close()

        img = plt.imread(image)
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.axis('off')
        ax.imshow(img)
        pdf.savefig(fig)
        plt.close()

def compute_integral():
    try:
        func_str = entry_func.get()
        a = float(sympify(entry_a.get()))
        b = float(sympify(entry_b.get()))
        c = float(sympify(entry_c.get()))
        d = float(sympify(entry_d.get()))

        expr = sympify(func_str)
        f_num = lambda x_val, y_val: float(expr.evalf(subs={x: x_val, y: y_val}))

        integral_inner = integrate(expr, (y, c, d))
        integral_outer = integrate(integral_inner, (x, a, b))

        result, error = scipy_integrate.dblquad(f_num, a, b, lambda x: c, lambda x: d)

        steps = f"""
🔢 Function: f(x, y) = {latex(expr)}

📐 Region of Integration: 
   x from {a:.5f} to {b:.5f}
   y from {c:.5f} to {d:.5f}

🧮 Step 1 – Set up the integral:
   ∬ f(x, y) dx dy = ∫ₐᵇ ∫𝚌ᵈ f(x, y) dy dx

🧮 Step 2 – Inner integral:
   ∫ from {c:.5f} to {d:.5f} of {latex(expr)} dy = {latex(integral_inner)}

🧮 Step 3 – Outer integral:
   ∫ from {a:.5f} to {b:.5f} of ({latex(integral_inner)}) dx = {latex(integral_outer)}

✅ Symbolic result: {integral_outer.evalf():.10f}

🔢 Numerical result: {result:.10f}
📉 Estimated error: {error:.2e}
"""

        output_text.config(state='normal')
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, steps)
        output_text.config(state='disabled')

        plot_surface(expr, a, b, c, d)
        generate_pdf(steps)

        messagebox.showinfo("Success", "Calculation complete. Results exported to PDF.")

    except Exception as e:
        output_text.config(state='normal')
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"❌ Error: {str(e)}")
        output_text.config(state='disabled')

# Interfaz
root = tk.Tk()
root.title("2D Integral Calculator with Procedure + PDF Export")
root.geometry("800x740")
root.configure(bg="#f4f7fa")

style = ttk.Style()
style.theme_use('clam')
style.configure("TLabel", font=("Segoe UI", 12), background="#f4f7fa")
style.configure("TEntry", font=("Segoe UI", 12))
style.configure("TButton", font=("Segoe UI", 12), padding=5)

main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill='both', expand=True)

ttk.Label(main_frame, text="Double Integral Calculator", font=("Segoe UI", 18, "bold")).pack(pady=10)

form = ttk.Frame(main_frame)
form.pack(pady=10)

ttk.Label(form, text="f(x, y) =").grid(row=0, column=0, sticky="e", padx=5)
entry_func = ttk.Entry(form, width=40)
entry_func.grid(row=0, column=1, pady=5)

ttk.Label(form, text="x from a =").grid(row=1, column=0, sticky="e", padx=5)
entry_a = ttk.Entry(form, width=10)
entry_a.grid(row=1, column=1, sticky="w", padx=5)

ttk.Label(form, text="to b =").grid(row=1, column=1, sticky="e", padx=100)
entry_b = ttk.Entry(form, width=10)
entry_b.grid(row=1, column=1, sticky="e", padx=5)

ttk.Label(form, text="y from c =").grid(row=2, column=0, sticky="e", padx=5)
entry_c = ttk.Entry(form, width=10)
entry_c.grid(row=2, column=1, sticky="w", padx=5)

ttk.Label(form, text="to d =").grid(row=2, column=1, sticky="e", padx=100)
entry_d = ttk.Entry(form, width=10)
entry_d.grid(row=2, column=1, sticky="e", padx=5)

ttk.Button(main_frame, text="Compute Integral & Export PDF", command=compute_integral).pack(pady=10)

output_text = scrolledtext.ScrolledText(main_frame, height=20, font=("Consolas", 11), wrap=tk.WORD, bg="white")
output_text.pack(fill="both", expand=True, padx=10)
output_text.config(state='disabled')

root.mainloop()
