from tkinter import *
from tkinter import ttk
from converter import Converter


class Data:
    def __init__(self):
        self.dec_in = None
        self.new_base = None
        self.new_val = None
        self.b_val = None
        self.b_base = None
        self.dec_val = None

    def build(self):
        self.dec_in = StringVar()
        self.new_base = IntVar()
        self.new_val = StringVar()
        self.b_val = StringVar()
        self.b_base = IntVar()
        self.dec_val = StringVar()


converter = Converter()
data = Data()


def calculate():
    # Check for valid base 10 -> other base input
    try:
        base = data.new_base.get()
        check_base(base)
        num = int(data.dec_in.get())
        ans = converter.decimal_to_base(num, base)
        data.new_val.set(ans)
    except ValueError:
        data.new_val.set("")

    # Check for valid other base -> base 10 input
    try:
        base = data.b_base.get()
        check_base(base)
        ans = converter.base_to_decimal(data.b_val.get(), base)
        data.dec_val.set(ans)
    except ValueError:
        data.dec_val.set("")


def check_base(base):
    if 1 <= base <= 16:
        return
    else:
        ValueError


def build():
    root = Tk()
    root.title("Base Conversion")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    data.build()

    dec_entry = ttk.Entry(mainframe, width=7, textvariable=data.dec_in)
    dec_entry.grid(column=1, row=1, sticky=E)

    ttk.Label(mainframe, text="in base").grid(column=2, row=1, sticky=(W, E))
    ttk.Label(mainframe, text="10").grid(column=3, row=1, sticky=(W, E))
    ttk.Label(mainframe, text="to base").grid(column=4, row=1, sticky=(W, E))

    new_base_entry = ttk.Entry(mainframe, width=4, textvariable=data.new_base)
    new_base_entry.grid(column=5, row=1, sticky=(W, E))

    ttk.Label(mainframe, textvariable=data.new_val).grid(column=6, row=1, sticky=W)

    val_entry = ttk.Entry(mainframe, width=7, textvariable=data.b_val)
    val_entry.grid(column=1, row=2, sticky=E)

    ttk.Label(mainframe, text="in base").grid(column=2, row=2, sticky=(W, E))

    base_entry = ttk.Entry(mainframe, width=4, textvariable=data.b_base)
    base_entry.grid(column=3, row=2, sticky=(W, E))

    ttk.Label(mainframe, text="to base").grid(column=4, row=2, sticky=(W, E))
    ttk.Label(mainframe, text="10").grid(column=5, row=2, sticky=(W, E))
    ttk.Label(mainframe, textvariable=data.dec_val).grid(column=6, row=2, sticky=W)

    ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=6, row=3, sticky=W)
    root.bind('<Return>', calculate)

    dec_entry.focus()

    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    return root


def main():
    root = build()
    root.mainloop()


if __name__ == "__main__":
    main()
