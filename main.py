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
    dateInput.text = ''
    nameInput.text = ''

def takeOrder(event):
    inputOrder = Data.Order(nameInput.text, dateInput.text, coffeeRadio.selected, milkRadio.selected, sugarRadio.selected, sizeRadio.selected)
    finalOrder = [inputOrder.name, inputOrder.date, inputOrder.coffee, inputOrder.milk, inputOrder.sugar, inputOrder.size]
    with open('Orders.csv', 'a', newline = '') as csvfile:
        myWriter = csv.writer(csvfile, delimiter = ' ')
        myWriter.writerow(finalOrder)
    removeSelection()
    

def previousOrder(event):
    with open('Orders.csv', newline='') as csvFile:
        data = list(csv.reader(csvFile))
    prevOrderWindow = gp.GooeyPieApp('Previous Orders')
    prevOrderWindow.set_grid(3, 1)
    app.width = 600
    app.height = 800
    prevOrderList = gp.Listbox(prevOrderWindow, data)
    prevOrderWindow.add(prevOrderList, 1, 1, fill=True)
    prevOrderWindow.run()



app = gp.GooeyPieApp('Cafe 263')
app.set_grid(10, 10)
app.width = 300

nameLbl = gp.Label(app, 'Name:')
nameInput = gp.Input(app)
dateLbl = gp.Label(app, 'Date:')
dateInput = gp.Input(app)
coffeeRadio = gp.LabelRadiogroup(app, 'Coffee Type', coffeeType)
milkRadio = gp.LabelRadiogroup(app, 'Milk', milkType)
sizeRadio = gp.LabelRadiogroup(app, 'Size', sizeType)
sugarRadio = gp.LabelRadiogroup(app, 'Sugar', sugarType)
orderBtn = gp.Button(app, 'Order', takeOrder)
prevOrderBtn = gp.Button(app, 'Previous Orders', previousOrder)
priceLbl = gp.Label(app, 'Price: ')

app.add(nameLbl, 1, 1)
app.add(nameInput, 2, 1)
app.add(dateLbl, 1, 2)
app.add(dateInput, 2, 2)
app.add(coffeeRadio, 3, 1, fill=True)
app.add(milkRadio, 3, 2, fill=True)
app.add(sugarRadio, 4, 1, fill=True)
app.add(sizeRadio, 4, 2, fill=True)
app.add(orderBtn, 7, 1)
app.add(prevOrderBtn, 7, 2)
app.add(priceLbl, 6, 1)

sizeRadio.add_event_listener('change', priceRefresh)
milkRadio.add_event_listener('change', priceRefresh)
sugarRadio.add_event_listener('change', priceRefresh)
coffeeRadio.add_event_listener('change',priceRefresh)

app.run()


