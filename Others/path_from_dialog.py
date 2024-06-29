from tkinter import filedialog as fd

path:str = fd.askopenfilename()

print(f"""

Chosen File Path:
    {path}
""")

# ------------------

l:list = [1, 2, 3, 4, 5]

print("Pretty List: ")
print(*l, sep="-", end="\n")

# ------------------

