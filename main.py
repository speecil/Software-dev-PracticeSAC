import csv
import Data
import gooeypie as gp

coffeeType = ('Flat White', 'Cappuccino', 'Short Black', 'Latte')
milkType = ('None', 'Full Cream', 'Skim', 'Soy')
sizeType = ('Small', 'Regular', 'Large')
sugarType = ('None', 'One Sugar', 'Two  Sugars')

def priceRefresh(event):
    price = 0
    match coffeeRadio.selected_index:
        case 0:
            price += 2.50
        case 1:
            price += 3.50
        case 2:
            price += 2.00
        case 3:
            price += 3.00
    match milkRadio.selected_index:
        case 1:
            price += 0.00
        case 2:
            price += 0.50
        case 3:
            price += 1.00
    match sizeRadio.selected_index:
        case 1:
            price += 0.50
        case 2:
            price += 1.00
    match sugarRadio.selected_index:
        case 1:
            price += 0.10
        case 2:
            price += 0.20
    
    priceLbl.text = f'Price: {price}'

def removeSelection():
    sizeRadio.deselect()
    milkRadio.deselect()
    sugarRadio.deselect()
    coffeeRadio.deselect()

def takeOrder(event):
    inputOrder = Data.Order(nameInput.text, dateInput.text, coffeeRadio.selected, milkRadio.selected, sugarRadio.selected, sizeRadio.selected)
    finalOrder = ["Name: " + inputOrder.name, "Date: " + inputOrder.date, "Coffee: " + inputOrder.coffee, "Milk: " + inputOrder.milk, "Sugars: " + inputOrder.sugar, "Size: " + inputOrder.size]
    with open('Orders.csv', 'a', newline = '') as csvfile:
        myWriter = csv.writer(csvfile, delimiter = ' ')
        myWriter.writerow(finalOrder)
    removeSelection()
    

def previousOrder(event):
    with open('Orders.csv', newline='') as csvFile:
        data = list(csv.reader(csvFile))
    prevOrderWindow = gp.GooeyPieApp('Previous Orders')
    prevOrderWindow.set_grid(3, 1)
    prevOrderWindow.width = 600
    prevOrderList = gp.Listbox(prevOrderWindow, data)
    prevOrderWindow.add(prevOrderList, 1, 1, fill=True)
    prevOrderWindow.run()

def validateOrder(event):
    forgotten = []
    missing= ''
    if nameInput.text == '' or dateInput.text == '' or coffeeRadio.selected == None or milkRadio.selected == None or sugarRadio.selected == None or sizeRadio.selected == None:
        if nameInput.text == '':
            forgotten.append('Name')
        if dateInput.text == '':
            forgotten.append('Date')
        if coffeeRadio.selected == None:
            forgotten.append('Coffee')
        if milkRadio.selected == None:
            forgotten.append('Milk')
        if sugarRadio.selected == None:     
            forgotten.append('Sugar')
        if sizeRadio.selected == None:
            forgotten.append('Size')
        for x in forgotten:
            if x == forgotten[-1]:
                missing += f'{x}'
            else:
                missing += f'{x}, '
        app.alert("Error", f"You must enter more info\nYou need to input {missing}.", "error")
    else:
        takeOrder(event=event)



app = gp.GooeyPieApp('Cafe 263')
app.set_grid(10, 10)
app.width = 300

titleLbl = gp.Label(app, "Cafe 263")
titleLbl.size = 12
titleLbl.justify = 'center'
nameLbl = gp.Label(app, 'Name:')
nameInput = gp.Input(app)
dateLbl = gp.Label(app, 'Date:')
dateInput = gp.Input(app)
coffeeRadio = gp.LabelRadiogroup(app, 'Coffee Type', coffeeType)
milkRadio = gp.LabelRadiogroup(app, 'Milk', milkType)
sizeRadio = gp.LabelRadiogroup(app, 'Size', sizeType)
sugarRadio = gp.LabelRadiogroup(app, 'Sugar', sugarType)
orderBtn = gp.Button(app, 'Order', validateOrder)
prevOrderBtn = gp.Button(app, 'Previous Orders', previousOrder)
priceLbl = gp.Label(app, 'Price: ')

app.add(titleLbl, 1, 2)
app.add(nameLbl, 2, 2)
app.add(nameInput, 3, 2)
app.add(dateLbl, 2, 3)
app.add(dateInput, 3, 3)
app.add(coffeeRadio, 4, 2, fill=True)
app.add(milkRadio, 4, 3, fill=True)
app.add(sugarRadio, 5, 2, fill=True)
app.add(sizeRadio, 5, 3, fill=True)
app.add(orderBtn, 8, 2)
app.add(prevOrderBtn, 8, 3)
app.add(priceLbl, 7, 2)

sizeRadio.add_event_listener('change', priceRefresh)
milkRadio.add_event_listener('change', priceRefresh)
sugarRadio.add_event_listener('change', priceRefresh)
coffeeRadio.add_event_listener('change',priceRefresh)

app.run()


