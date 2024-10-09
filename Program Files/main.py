import tkinter as tk


calculation = ""

def addToCalc(symbol):
    global calculation
    #This is optional, just person pref since I don't like using '*' and '/'
    if symbol == "*":
        symbol = "×"
    elif symbol == "/":
        symbol = "÷"
    #
    calculation += str(symbol)
    txtResult.delete(1.0, "end")
    txtResult.insert(1.0, calculation)


def evalCalc():
    global calculation
    try:
        #I don't like using '*' and '/' lol. This is optional
        calc = calculation.replace("×", "*").replace("÷", "/")
        #
        calculation = str(eval(calc))
        
        txtResult.delete(1.0, "end")
        txtResult.insert(1.0, calculation)
    except:
        clearField()
        txtResult.insert(1.0, "Error..")

        pass
    pass

def clearField():
    global calculation
    calculation = ""
    txtResult.delete(1.0, "end")
    pass

def create_button(root, text, row, column, command):
    button = tk.Button(root,
                      text=text,
                      command=command,
                      width=5,
                      font=("Arial", 12),
                      bg="#616469",  # Light grey background for buttons
                      fg="black"       # White text for buttons
                      )
    button.grid(row=row, column=column, sticky="nsew")
    return button

#Creates window
root=tk.Tk()
root.geometry("270x260")
root.configure(
    background="#222326"
)

txtResult = tk.Text(root,
                    height=1,               
                    width=16,               
                    font=("Arial", 18),
                    background="white",
                    foreground="black"
                    )
txtResult.grid(columnspan=5, sticky="nsew")
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

#0-9 buttons
create_button(root, "1", 2, 1, lambda: addToCalc(1))
create_button(root, "2", 2, 2, lambda: addToCalc(2))
create_button(root, "3", 2, 3, lambda: addToCalc(3))
create_button(root, "4", 3, 1, lambda: addToCalc(4))
create_button(root, "5", 3, 2, lambda: addToCalc(5))
create_button(root, "6", 3, 3, lambda: addToCalc(6))
create_button(root, "7", 4, 1, lambda: addToCalc(7))
create_button(root, "8", 4, 2, lambda: addToCalc(8))
create_button(root, "9", 4, 3, lambda: addToCalc(9))
create_button(root, "0", 5, 2, lambda: addToCalc(0))

#operators
create_button(root, "+", 2, 4, lambda: addToCalc("+"))
create_button(root, "-", 3, 4, lambda: addToCalc("-"))
create_button(root, "×", 4, 4, lambda: addToCalc("*"))
create_button(root, "÷", 5, 4, lambda: addToCalc("/"))
create_button(root, "=", 6, 3, evalCalc).grid(columnspan=2)

#extra buttons
create_button(root, "C", 6, 1, clearField).grid(columnspan=2)
create_button(root, "(", 5, 1, lambda: addToCalc("("))
create_button(root, ")", 5, 3, lambda: addToCalc(")"))

root.mainloop()
