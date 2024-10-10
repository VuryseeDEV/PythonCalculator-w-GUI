import tkinter as tk
import math

calculation = ""

def addToCalc(symbol):
    global calculation
    #This is optional, just person pref since I don't like using '*' and '/'
    if symbol == "*":
        symbol = "×"
    elif symbol == "/":
        symbol = "÷"
    
    calculation += str(symbol)# Append the symbol to the calculation string
    txtResult.delete(1.0, "end") # Clears text box
    txtResult.insert(1.0, calculation) # Displays calculation


def evalCalc():
    global calculation
    try:
        calc = calculation.replace("×", "*").replace("÷", "/")  # For better readability
        
        # Handle square root operation
        while "√" in calc:
            index = calc.index("√")
            number_start = index + 1
            number_end = number_start
            while number_end < len(calc) and calc[number_end].isdigit():
                number_end += 1
            number = calc[number_start:number_end]
            calc = calc[:index] + str(math.sqrt(float(number))) + calc[number_end:]  # Replace "√" with the square root value
        
        # Evaluate the rest of the expression
        calculation = str(eval(calc))

        txtResult.delete(1.0, "end") 
        txtResult.insert(1.0, calculation)
    except Exception as e:
        clearField()
        txtResult.insert(1.0, "Error..")

        pass
    pass

#Func to clear text box
def clearField(): 
    global calculation
    calculation = "" # Reset the calculation string
    txtResult.delete(1.0, "end")
    pass

#bUtToN cReAtOr!!!
def create_button(root, text, row, column, command, bg_color="#616469", fg_color="black"):
    button = tk.Button(root,
                       text=text,
                       command=command,
                       width=5,
                       font=("Arial", 12),
                       bg=bg_color,  
                       fg=fg_color       
                       )
    button.grid(row=row, column=column, sticky="nsew")
    return button

#Creates window
root=tk.Tk()
root.geometry("300x400")
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

# Configures the grid to make rows and columns expandable
# (As you alternate the window's size, the button sizes also change)
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)


# 0-9 buttons 
create_button(root, "1", 2, 1, lambda: addToCalc(1), bg_color="#787673", fg_color="black")
create_button(root, "2", 2, 2, lambda: addToCalc(2), bg_color="#787673", fg_color="black")
create_button(root, "3", 2, 3, lambda: addToCalc(3), bg_color="#787673", fg_color="black")
create_button(root, "4", 3, 1, lambda: addToCalc(4), bg_color="#787673", fg_color="black")
create_button(root, "5", 3, 2, lambda: addToCalc(5), bg_color="#787673", fg_color="black")
create_button(root, "6", 3, 3, lambda: addToCalc(6), bg_color="#787673", fg_color="black")
create_button(root, "7", 4, 1, lambda: addToCalc(7), bg_color="#787673", fg_color="black")
create_button(root, "8", 4, 2, lambda: addToCalc(8), bg_color="#787673", fg_color="black")
create_button(root, "9", 4, 3, lambda: addToCalc(9), bg_color="#787673", fg_color="black")
create_button(root, "0", 5, 2, lambda: addToCalc(0), bg_color="#787673", fg_color="black")


#operators (+, -, ×, ÷, =)
create_button(root, "+", 2, 4, lambda: addToCalc("+"), bg_color="#474645", fg_color="black")
create_button(root, "-", 3, 4, lambda: addToCalc("-"), bg_color="#474645", fg_color="black")
create_button(root, "×", 4, 4, lambda: addToCalc("*"), bg_color="#474645", fg_color="black")
create_button(root, "÷", 5, 4, lambda: addToCalc("/"), bg_color="#474645", fg_color="black")
create_button(root, "=", 6, 3, evalCalc, bg_color="#f0ad4e", fg_color="black")
create_button(root, "√", 6, 4, lambda: addToCalc("√"), bg_color="#474645", fg_color="black")  # Square root button
create_button(root, "^", 5, 4, lambda: addToCalc("**"), bg_color="#474645", fg_color="black")  # Exponent button (using Python's '**' for power)

#extra buttons
create_button(root, "C", 6, 1, clearField, bg_color="#787673", fg_color="black")
create_button(root, "(", 5, 1, lambda: addToCalc("("), bg_color="#787673", fg_color="black")
create_button(root, ")", 5, 3, lambda: addToCalc(")"), bg_color="#787673", fg_color="black")
create_button(root, ".", 6, 2, lambda: addToCalc("."), bg_color="#787673", fg_color="black")


# Start the GUI event loop
root.mainloop()
