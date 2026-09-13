import tkinter as tk
from tkinter import ttk

# ---------------- SIMULATION ----------------

def run_simulation():
    text = input_box.get("1.0", tk.END).strip()

    if not text:
        status.config(text="⚠ Enter instructions first!")
        return

    lines = [x.strip().upper() for x in text.splitlines() if x.strip()]

    risc = []
    cisc = []
    risc_cycles = 0
    cisc_cycles = 0

    for line in lines:

        if line.startswith("ADD"):
            risc += ["LOAD", "ADD", "STORE"]
            risc_cycles += 3
            cisc += ["ADD"]
            cisc_cycles += 2

        elif line.startswith("SUB"):
            risc += ["LOAD", "SUB", "STORE"]
            risc_cycles += 3
            cisc += ["SUB"]
            cisc_cycles += 2

        elif line.startswith("MUL"):
            risc += ["LOAD", "MUL", "STORE"]
            risc_cycles += 3
            cisc += ["MUL"]
            cisc_cycles += 3

        elif line.startswith("MOV"):
            risc += ["LOAD", "STORE"]
            risc_cycles += 2
            cisc += ["MOV"]
            cisc_cycles += 2

        else:
            risc.append(line)
            cisc.append(line)
            risc_cycles += 1
            cisc_cycles += 1

    show_results(risc, cisc, risc_cycles, cisc_cycles)


# ---------------- DISPLAY RESULTS ----------------

def show_results(risc, cisc, rc, cc):

    risc_count.set(str(len(risc)))
    cisc_count.set(str(len(cisc)))
    risc_cycle.set(str(rc))
    cisc_cycle.set(str(cc))

    risc_list.delete("1.0", tk.END)
    cisc_list.delete("1.0", tk.END)

    for i, x in enumerate(risc, 1):
        risc_list.insert(tk.END, f"  {i:02}  →  {x}\n")

    for i, x in enumerate(cisc, 1):
        cisc_list.insert(tk.END, f"  {i:02}  →  {x}\n")

    # Performance bars
    max_cycle = max(rc, cc, 1)
    risc_bar["value"] = (rc / max_cycle) * 100
    cisc_bar["value"] = (cc / max_cycle) * 100

    if rc < cc:
        result.config(
            text="⚡ RISC is faster in this simulation",
        )
    elif cc < rc:
        result.config(
            text="⚡ CISC is faster in this simulation",
        )
    else:
        result.config(
            text="⚖ Both have equal estimated cycles"
        )

    status.config(text="✓ Simulation completed successfully")


def example():
    input_box.delete("1.0", tk.END)
    input_box.insert(
        tk.END,
        "ADD R1,R2\n"
        "SUB R3,R4\n"
        "MUL R5,R6\n"
        "MOV R1,R2"
    )
    status.config(text="Example program loaded")


def clear_all():
    input_box.delete("1.0", tk.END)
    risc_list.delete("1.0", tk.END)
    cisc_list.delete("1.0", tk.END)

    risc_count.set("0")
    cisc_count.set("0")
    risc_cycle.set("0")
    cisc_cycle.set("0")

    risc_bar["value"] = 0
    cisc_bar["value"] = 0

    result.config(text="Run simulation to compare architectures")
    status.config(text="Ready")


# ---------------- MAIN WINDOW ----------------

root = tk.Tk()
root.title("RISC vs CISC Simulator")
root.geometry("1050x720")
root.configure(bg="#101827")

# Style
style = ttk.Style()
style.theme_use("clam")

style.configure(
    "RISC.Horizontal.TProgressbar",
    troughcolor="#202c3d",
    background="#38bdf8",
    thickness=12
)

style.configure(
    "CISC.Horizontal.TProgressbar",
    troughcolor="#202c3d",
    background="#f472b6",
    thickness=12
)

# ---------------- HEADER ----------------

header = tk.Frame(root, bg="#172235", height=90)
header.pack(fill="x")

tk.Label(
    header,
    text="⚙  RISC  VS  CISC",
    font=("Segoe UI", 26, "bold"),
    fg="white",
    bg="#172235"
).pack(pady=(15, 0))

tk.Label(
    header,
    text="Computer Organization & Architecture • Instruction Simulation Tool",
    font=("Segoe UI", 11),
    fg="#9fb0c5",
    bg="#172235"
).pack()

# ---------------- INPUT ----------------

tk.Label(
    root,
    text="ASSEMBLY PROGRAM",
    font=("Segoe UI", 11, "bold"),
    fg="#38bdf8",
    bg="#101827"
).pack(anchor="w", padx=35, pady=(20, 5))

input_box = tk.Text(
    root,
    height=6,
    font=("Consolas", 12),
    bg="#172235",
    fg="#e5e7eb",
    insertbackground="white",
    relief="flat",
    padx=15,
    pady=12
)
input_box.pack(fill="x", padx=35)

input_box.insert(
    tk.END,
    "ADD R1,R2\nSUB R3,R4\nMUL R5,R6\nMOV R1,R2"
)

# ---------------- BUTTONS ----------------

button_frame = tk.Frame(root, bg="#101827")
button_frame.pack(pady=12)

tk.Button(
    button_frame,
    text="▶  RUN SIMULATION",
    command=run_simulation,
    font=("Segoe UI", 11, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    relief="flat",
    padx=25,
    pady=10
).grid(row=0, column=0, padx=8)

tk.Button(
    button_frame,
    text="📋 LOAD EXAMPLE",
    command=example,
    font=("Segoe UI", 10, "bold"),
    bg="#334155",
    fg="white",
    relief="flat",
    padx=20,
    pady=10
).grid(row=0, column=1, padx=8)

tk.Button(
    button_frame,
    text="✕ CLEAR",
    command=clear_all,
    font=("Segoe UI", 10, "bold"),
    bg="#7f1d1d",
    fg="white",
    relief="flat",
    padx=20,
    pady=10
).grid(row=0, column=2, padx=8)

# ---------------- RESULT CARDS ----------------

cards = tk.Frame(root, bg="#101827")
cards.pack(fill="x", padx=35, pady=5)

risc_card = tk.Frame(cards, bg="#172235")
risc_card.pack(side="left", expand=True, fill="both", padx=(0, 8))

cisc_card = tk.Frame(cards, bg="#172235")
cisc_card.pack(side="left", expand=True, fill="both", padx=(8, 0))

tk.Label(
    risc_card, text="RISC",
    font=("Segoe UI", 18, "bold"),
    fg="#38bdf8", bg="#172235"
).pack(pady=8)

tk.Label(
    risc_card, text="Simple instruction model",
    fg="#94a3b8", bg="#172235"
).pack()

risc_count = tk.StringVar(value="0")
risc_cycle = tk.StringVar(value="0")

tk.Label(
    risc_card,
    textvariable=risc_count,
    font=("Segoe UI", 24, "bold"),
    fg="white", bg="#172235"
).pack()

tk.Label(
    risc_card, text="Instructions",
    fg="#94a3b8", bg="#172235"
).pack()

tk.Label(
    risc_card,
    textvariable=risc_cycle,
    font=("Segoe UI", 20, "bold"),
    fg="#38bdf8", bg="#172235"
).pack()

tk.Label(
    risc_card, text="Estimated Clock Cycles",
    fg="#94a3b8", bg="#172235"
).pack(pady=(0, 10))

tk.Label(
    cisc_card, text="CISC",
    font=("Segoe UI", 18, "bold"),
    fg="#f472b6", bg="#172235"
).pack(pady=8)

tk.Label(
    cisc_card, text="Complex instruction model",
    fg="#94a3b8", bg="#172235"
).pack()

cisc_count = tk.StringVar(value="0")
cisc_cycle = tk.StringVar(value="0")

tk.Label(
    cisc_card,
    textvariable=cisc_count,
    font=("Segoe UI", 24, "bold"),
    fg="white", bg="#172235"
).pack()

tk.Label(
    cisc_card, text="Instructions",
    fg="#94a3b8", bg="#172235"
).pack()

tk.Label(
    cisc_card,
    textvariable=cisc_cycle,
    font=("Segoe UI", 20, "bold"),
    fg="#f472b6", bg="#172235"
).pack()

tk.Label(
    cisc_card, text="Estimated Clock Cycles",
    fg="#94a3b8", bg="#172235"
).pack(pady=(0, 10))

# ---------------- EXECUTION LOG ----------------

logs = tk.Frame(root, bg="#101827")
logs.pack(fill="both", expand=True, padx=35, pady=12)

left = tk.Frame(logs, bg="#172235")
left.pack(side="left", expand=True, fill="both", padx=(0, 6))

right = tk.Frame(logs, bg="#172235")
right.pack(side="left", expand=True, fill="both", padx=(6, 0))

tk.Label(
    left, text="RISC EXECUTION",
    font=("Segoe UI", 11, "bold"),
    fg="#38bdf8", bg="#172235"
).pack(pady=6)

risc_list = tk.Text(
    left, font=("Consolas", 10),
    bg="#0f172a", fg="#dbeafe",
    relief="flat"
)
risc_list.pack(fill="both", expand=True, padx=8, pady=(0, 8))

tk.Label(
    right, text="CISC EXECUTION",
    font=("Segoe UI", 11, "bold"),
    fg="#f472b6", bg="#172235"
).pack(pady=6)

cisc_list = tk.Text(
    right, font=("Consolas", 10),
    bg="#0f172a", fg="#fce7f3",
    relief="flat"
)
cisc_list.pack(fill="both", expand=True, padx=8, pady=(0, 8))

# ---------------- PERFORMANCE ----------------

tk.Label(
    root,
    text="CLOCK CYCLE COMPARISON",
    font=("Segoe UI", 10, "bold"),
    fg="#cbd5e1",
    bg="#101827"
).pack()

risc_bar = ttk.Progressbar(
    root, style="RISC.Horizontal.TProgressbar",
    maximum=100
)
risc_bar.pack(fill="x", padx=35, pady=3)

cisc_bar = ttk.Progressbar(
    root, style="CISC.Horizontal.TProgressbar",
    maximum=100
)
cisc_bar.pack(fill="x", padx=35, pady=3)

result = tk.Label(
    root,
    text="Run simulation to compare architectures",
    font=("Segoe UI", 12, "bold"),
    fg="white",
    bg="#101827"
)
result.pack(pady=6)

status = tk.Label(
    root,
    text="Ready",
    font=("Segoe UI", 9),
    fg="#64748b",
    bg="#101827"
)
status.pack(pady=(0, 8))

root.mainloop()   