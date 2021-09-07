import tkinter
from tkinter import messagebox

#  Give a widget a variable for text that you can change, rather than replacing the label all together
"""
Functions
"""
def calculate(tax, price, list, label):
    try:
        new_price = round(float(price) + float((float(price) * (int(tax)/100))), 2)
        list.append(new_price)
        label.grid_forget()
        global the_price
        the_price = tkinter.Label(window, text="The item costs {} when accounting for sales tax\nList:{}".format(new_price, list))
        the_price.grid(row=4, column=0, columnspan=3)
    except ValueError:
        message = tkinter.messagebox.showerror("An Error has occured", "You can't type words inside of the text boxes!")


def clear(list):
    price_box.delete(0, "end")
    the_price.grid_forget()
    the_total.grid_forget()
    del list
    global all_prices
    all_prices = []


def total(list):
    total_price = 0
    for each in list:
        total_price += each
    the_price.grid_forget()
    global the_total
    the_total = tkinter.Label(window, text="The total cost of those items is:\n${}".format(total_price))
    the_total.grid(row=3, column=0, columnspan=3)

"""
Variables
"""
all_prices = []
#  A sales tax calculator that continually appends prices until you press a "total" button
window = tkinter.Tk()
instruction_1 = tkinter.Label(window, text="Type the sales tax number:")
instruction_2 = tkinter.Label(window, text="Type the price of the item:")

tax_box = tkinter.Entry(window, width="30")
price_box = tkinter.Entry(window, width="30")

the_price = tkinter.Label(window, text="")

calculate_button = tkinter.Button(window, text="Calculate", padx="35", command=lambda : calculate(tax_box.get(), price_box.get(), all_prices, the_price))
clear_price_button = tkinter.Button(window, text="Clear Price", padx="15", command=lambda : clear(all_prices))
total_price_button = tkinter.Button(window, text="Total Price", padx="15", command=lambda : total(all_prices))

"""
Display
"""
instruction_1.grid(row=0, column=0)
tax_box.grid(row=0, column=1, padx=5, columnspan=2)
instruction_2.grid(row=1, column=0, pady=15)
price_box.grid(row=1, column=1, padx=5, pady=15, columnspan=2)
calculate_button.grid(row=2, column=0, pady=5)
clear_price_button.grid(row=2, column=1, pady=5)
total_price_button.grid(row=2, column=2, pady=5)
window.configure(background="#d9e3da")
window.title("Sales Tax Calculator")
window.mainloop()