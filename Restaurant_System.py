from Tkinter import*
import random
import time

root = Tk()
root.geometry("900x600+0+0")
root.title("Restaurant Management System")

#variables
text_Input = StringVar()
operator = ""

#first frame
Tops = Frame(root, width=1600, bg="pale turquoise", relief=SUNKEN)
Tops.pack(side=TOP)
#second frame
f2 = Frame(root, width=800, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

#third frame
f3 = Frame(root, width=1600, height=700, relief=SUNKEN)
f3.pack(side=LEFT)

#time
localtime = time.asctime(time.localtime(time.time()))

#===SYSTEM INFO===#
#title
lblInfo = Label(Tops, font=("arial", 50, "bold"), text="Restaurant Management Systems", fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)
lblInfo = Label(Tops, font=("arial", 20, "bold"), text=localtime, fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=1, column=0)
#=====CALCULATOR===#
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def buttonClearDisplay():
    global operator
    operator = ""
    text_Input.set("")

def buttonEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

def ref():
    x = random.randint(11156, 600898)
    randomref = str(x)
    rand.set(randomref)

    kebabPrice = float(kebab.get()) * 1.99
    drinkPrice = float(drink.get()) * 1.00
    burgerPrice = float(burger.get()) * 3.99
    pizzaPrice = float(pizza.get()) * 2.29
    chapatiPrice = float(chapati.get()) * 0.79
    porridgePrice = float(porridge.get()) * 0.99
    teaPrice = float(tea.get()) * 0.99
    fishPrice = float(fish.get()) * 1.29
    lambStewPrice = float(lambStew.get()) * 4.99
    goatStewPrice = float(goatStew.get()) * 4.89
    beefStewPrice = float(beefStew.get()) * 4.49
    chickenSandwichPrice = float(chickenSandwich.get()) * 1.89

    costOfMeal = "$", str('%.2f' % (kebabPrice + drinkPrice + burgerPrice + pizzaPrice + chapatiPrice + porridgePrice + teaPrice + fishPrice + lambStewPrice + goatStewPrice + beefStewPrice + chickenSandwichPrice))
    payTax = (kebabPrice + drinkPrice + burgerPrice + pizzaPrice + chapatiPrice + porridgePrice + teaPrice + fishPrice + lambStewPrice + goatStewPrice + beefStewPrice + chickenSandwichPrice) * 0.087
    totalCost = (kebabPrice + drinkPrice + burgerPrice + pizzaPrice + chapatiPrice + porridgePrice + teaPrice + fishPrice + lambStewPrice + goatStewPrice + beefStewPrice + chickenSandwichPrice)
    ser_charge = (kebabPrice + drinkPrice + burgerPrice + pizzaPrice + chapatiPrice + porridgePrice + teaPrice + fishPrice + lambStewPrice + goatStewPrice + beefStewPrice + chickenSandwichPrice) / 99
    overallTotal = "$", str("%.2f" % (payTax + totalCost + ser_charge))
    paidTax = "$", str("%.2f" % payTax)
    subTotal.set(costOfMeal)
    tax.set(paidTax)
    grandTotal.set(overallTotal)



def exit():
    root.destroy()

def reset():
    rand.set("")
    kebab.set("")
    burger.set("")
    pizza.set("")
    chapati.set("")
    porridge.set("")
    tea.set("")
    fish.set("")
    lambStew.set("")
    goatStew.set("")
    beefStew.set("")
    chickenSandwich.set("")
    drink.set("")
    subTotal.set("")
    tax.set("")
    grandTotal.set("")


txtDisplay = Entry(f2, font=("arial", 20, "bold"), textvariable=text_Input, bd=30, insertwidth=4, bg="pale turquoise", justify="right")
txtDisplay.grid(columnspan=4)

btn7 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"),
              text="7", bg="pale turquoise", command=lambda: btnClick(7)).grid(row=2, column=0)
btn8 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"),
              text="8", bg="pale turquoise", command=lambda: btnClick(8)).grid(row=2, column=1)
btn9 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"),
              text="9", bg="pale turquoise", command=lambda: btnClick(9)).grid(row=2, column=2)

addition = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"),
         text="+", bg="pale turquoise", command=lambda: btnClick("+")).grid(row=2, column=3)
#-----------------------------------------------------------------------------------------------------#
btn4 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"),
              text="4", bg="pale turquoise", command=lambda: btnClick(4)).grid(row=3, column=0)
btn5 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"),
              text="5", bg="pale turquoise", command=lambda: btnClick(5)).grid(row=3, column=1)
btn6 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"),
              text="6", bg="pale turquoise", command=lambda: btnClick(6)).grid(row=3, column=2)

subtraction = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"),
                  text="-", bg="pale turquoise", command=lambda: btnClick("-")).grid(row=3, column=3)
#-----------------------------------------------------------------------------------------------------#
btn1 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"),
              text="1", bg="pale turquoise", command=lambda: btnClick(1)).grid(row=4, column=0)
btn2 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"),
              text="2", bg="pale turquoise", command=lambda: btnClick(2)).grid(row=4, column=1)
btn3 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"),
              text="3", bg="pale turquoise", command=lambda: btnClick(3)).grid(row=4, column=2)

multiply = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"),
                     text="*", bg="pale turquoise", command=lambda: btnClick("*")).grid(row=4, column=3)
#-----------------------------------------------------------------------------------------------------#
btn0 = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"),
              text="0", bg="pale turquoise", command=lambda: btnClick(0)).grid(row=5, column=0)
btnClear = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"),
              text="C", bg="pale turquoise", command=lambda: buttonClearDisplay()).grid(row=5, column=1)
btnEqual = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"),
              text="=", bg="pale turquoise", command=lambda:buttonEqualsInput()).grid(row=5, column=2)

division = Button(f2, padx=16, pady=16, bd=8, fg="black", font=("arial", 20, "bold"),
                     text="/", bg="pale turquoise", command=lambda: btnClick("/")).grid(row=5, column=3)
#-----------------------------------------Restaurant Information 1-------------------------------------#
rand = StringVar()
kebab = StringVar()
burger = StringVar()
pizza = StringVar()
chapati = StringVar()
porridge = StringVar()
tea = StringVar()
fish = StringVar()
lambStew = StringVar()
goatStew = StringVar()
beefStew = StringVar()
chickenSandwich = StringVar()
drink = StringVar()
subTotal = StringVar()
tax = StringVar()
grandTotal = StringVar()

lblReference = Label(f3, font=("arial", 16, "bold"), text="Reference", bd=16, anchor="w")
lblReference.grid(row=0, column=0)
txtReference = Entry(f3, font=("arial", 16, "bold"), textvariable=rand, bd=10, insertwidth=4,
                     bg="pale turquoise", justify="right")
txtReference.grid(row=0, column=1)
#kebab
lblKebabs = Label(f3, font=("arial", 16, "bold"), text="Kebab", bd=16, anchor="w")
lblKebabs.grid(row=1, column=0)
txtKebab = Entry(f3, font=("arial", 16, "bold"), textvariable=kebab, bd=10, insertwidth=4,
                bg="pale turquoise", justify="right")
txtKebab.grid(row=1, column=1)
#burger
lblBurger = Label(f3, font=("arial", 16, "bold"), text="Burger", bd=16, anchor="w")
lblBurger.grid(row=2, column=0)
txtBurger = Entry(f3, font=("arial", 16, "bold"), textvariable=burger, bd=10, insertwidth=4,
                 bg="pale turquoise", justify="right")
txtBurger.grid(row=2, column=1)
#pizza
lblPizza = Label(f3, font=("arial", 16, "bold"), text="Pizza", bd=16, anchor="w")
lblPizza.grid(row=3, column=0)
txtPizza = Entry(f3, font=("arial", 16, "bold"), textvariable=pizza, bd=10, insertwidth=4,
                  bg="pale turquoise", justify="right")
txtPizza.grid(row=3, column=1)
#chapati
lblChapati = Label(f3, font=("arial", 16, "bold"), text="Chapati", bd=16, anchor="w")
lblChapati.grid(row=4, column=0)
txtChapati = Entry(f3, font=("arial", 16, "bold"), textvariable=chapati, bd=10, insertwidth=4,
                 bg="pale turquoise", justify="right")
txtChapati.grid(row=4, column=1)
#porridge
lblPorridge = Label(f3, font=("arial", 16, "bold"), text="Porridge", bd=16, anchor="w")
lblPorridge.grid(row=5, column=0)
txtPorridge = Entry(f3, font=("arial", 16, "bold"), textvariable=porridge, bd=10, insertwidth=4,
                   bg="pale turquoise", justify="right")
txtPorridge.grid(row=5, column=1)
#tea
lblTea = Label(f3, font=("arial", 16, "bold"), text="Tea", bd=16, anchor="w")
lblTea.grid(row=6, column=0)
txtTea = Entry(f3, font=("arial", 16, "bold"), textvariable=tea, bd=10, insertwidth=4,
               bg="pale turquoise", justify="right")
txtTea.grid(row=6, column=1)
#fish
lblFish = Label(f3, font=("arial", 16, "bold"), text="Fish", bd=16, anchor="w")
lblFish.grid(row=7, column=0)
txtFish = Entry(f3, font=("arial", 16, "bold"), textvariable=fish, bd=10, insertwidth=4,
               bg="pale turquoise", justify="right")
txtFish.grid(row=7, column=1)


#-----------------------------------Restaurant information 2------------------------------------------------------#
#lambStew
lblLambStew = Label(f3, font=("arial", 16, "bold"), text="Lamb Stew", bd=16, anchor="w")
lblLambStew.grid(row=0, column=2)
txtLambStew = Entry(f3, font=("arial", 16, "bold"), textvariable=lambStew, bd=10, insertwidth=4,
                    bg="pale turquoise", justify="right")
txtLambStew.grid(row=0, column=3)
#goatStew
lblGoatStew = Label(f3, font=("arial", 16, "bold"), text="Goat Stew", bd=16, anchor="w")
lblGoatStew.grid(row=1, column=2)
txtGoatStew = Entry(f3, font=("arial", 16, "bold"), textvariable=goatStew, bd=10, insertwidth=4,
                    bg="pale turquoise", justify="right")
txtGoatStew.grid(row=1, column=3)
#beefStew
lblBeefStew = Label(f3, font=("arial", 16, "bold"), text="Beef Stew", bd=16, anchor="w")
lblBeefStew.grid(row=2, column=2)
txtBeefStew = Entry(f3, font=("arial", 16, "bold"), textvariable=beefStew, bd=10, insertwidth=4,
                    bg="pale turquoise", justify="right")
txtBeefStew.grid(row=2, column=3)
#chicken sandwich
lblChickenSandwich = Label(f3, font=("arial", 16, "bold"), text="Chicken Sandwich", bd=16, anchor="w")
lblChickenSandwich.grid(row=3, column=2)
txtChickenSandwich = Entry(f3, font=("arial", 16, "bold"), textvariable=chickenSandwich, bd=10, insertwidth=4,
                           bg="pale turquoise", justify="right")
txtChickenSandwich.grid(row=3, column=3)

#drinks
lblDrink = Label(f3, font=("arial", 16, "bold"), text="Drink", bd=16, anchor="w")
lblDrink.grid(row=4, column=2)
txtDrink = Entry(f3, font=("arial", 16, "bold"), textvariable=drink, bd=10, insertwidth=4,
                     bg="pale turquoise", justify="right")
txtDrink.grid(row=4, column=3)
#subtotal
lblSubTotal = Label(f3, font=("arial", 16, "bold"), text="Total cost", bd=16, anchor="w")
lblSubTotal.grid(row=5, column=2)
txtSubTotal = Entry(f3, font=("arial", 16, "bold"), textvariable=subTotal, bd=10, insertwidth=4,
                 bg="pale turquoise", justify="right")
txtSubTotal.grid(row=5, column=3)
#tax
lblTax = Label(f3, font=("arial", 16, "bold"), text="State tax", bd=16, anchor="w")
lblTax.grid(row=6, column=2)
txtTax = Entry(f3, font=("arial", 16, "bold"), textvariable=tax, bd=10, insertwidth=4,
                  bg="pale turquoise", justify="right")
txtTax.grid(row=6, column=3)
#grandTotal
lblGrandTotal = Label(f3, font=("arial", 16, "bold"), text="Grand total", bd=16, anchor="w")
lblGrandTotal.grid(row=7, column=2)
txtGrandTotal = Entry(f3, font=("arial", 16, "bold"), textvariable=grandTotal, bd=10, insertwidth=4,
                 bg="pale turquoise", justify="right")
txtGrandTotal.grid(row=7, column=3)

#-----------------------------------Button------------------------------------------------------#

btnTotal = Button(f3, padx=16, pady=8, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
                  text="Total", bg="pale turquoise", command=lambda: ref()).grid(row=12, column=1)
btnReset = Button(f3, padx=16, pady=8, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
                  text="Reset", bg="pale turquoise", command=lambda: reset()).grid(row=12, column=2)
btnExit = Button(f3, padx=16, pady=8, bd=16, fg="black", font=("arial", 16, "bold"), width=10,
                  text="Exit", bg="pale turquoise", command=lambda: exit()).grid(row=12, column=3)

root.mainloop()
