import csv
import Data
import gooeypie as gp
from datetime import datetime


coffeeType = ("Flat White", "Cappuccino", "Short Black", "Latte")
milkType = ("None", "Full Cream", "Skim", "Soy")
sizeType = ("Small", "Regular", "Large")
sugarType = ["None", "One Sugar", "Two  Sugars"]


def takeOrder(event):
    now = datetime.now()

    dt_string = now.strftime("%d/%m/%Y %H:%M")
    inputOrder = Data.Order(nameInput.text, dt_string, coffeeRadio.selected, milkRadio.selected, sugarRadio.selected, sizeRadio.selected)
    finalOrder = [inputOrder.name, inputOrder.date, inputOrder.coffee, inputOrder.milk, inputOrder.sugar, inputOrder.size]
    with open("Orders.csv", "a", newline = "") as csvfile:
        my_writer = csv.writer(csvfile, delimiter = " ")
        my_writer.writerow(finalOrder)

def previousOrder(event):
    with open("Orders.csv", newline="") as csvfile:
        data = list(csv.reader(csvfile))
    prevOrderWindow = gp.GooeyPieApp("Previous Orders")
    prevOrderWindow.set_grid(3, 1)
    app.width = 600
    app.height = 800
    prevOrderList = gp.Listbox(prevOrderWindow, data)
    prevOrderWindow.add(prevOrderList, 1, 1, fill=True)
    prevOrderWindow.run()

app = gp.GooeyPieApp("Cafe 263")
app.set_grid(10, 10)
nameInput = gp.Input(app)
coffeeRadio = gp.LabelRadiogroup(app, "Coffee Type", coffeeType)
milkRadio = gp.LabelRadiogroup(app, "Milk", milkType)
sizeRadio = gp.LabelRadiogroup(app, "Size", sizeType)
sugarRadio = gp.LabelRadiogroup(app, "Sugar", sugarType)
app.width = 300
orderBtn = gp.Button(app, "Order", takeOrder)
prevOrderBtn = gp.Button(app, "Previous Orders", previousOrder)
app.add(nameInput, 2, 1)
app.add(coffeeRadio, 3, 1, fill=True)
app.add(milkRadio, 4, 1, fill=True)
app.add(sugarRadio, 5, 1, fill=True)
app.add(sizeRadio, 6, 1, fill=True)
app.add(orderBtn, 7, 2)
app.add(prevOrderBtn, 6, 2)
app.run()


