def amountcalculate(units):
    if units <= 200:
        bill = units*0.50
    elif units <= 400:
        bill =(200*0.50)+(units-200*0.65)
    elif units <= 600:
        bill =(200*0.50)+(200*0.65)+(units-400)*0.80
    else:
        bill =(200*0.50)+(200*0.65)+(200*0.80)+(units-600)*1.00

    if bill>400:
        bill+= bill*0.15

    if bill<100:
        bill=100

    return bill

def main():
    units = float(input("Enter the number of units consumed: "))
    bill = amountcalculate(units)
    print("The total bill is: Rs.", bill)

main()
