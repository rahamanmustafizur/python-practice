cost_price  =   int(input("enter cost price"))
selling_price   =   int(input("enter selling price"))
if  selling_price   >   cost_price:
    profit  = selling_price -   cost_price
    print("the profit of",profit)
if  cost_price  ==  selling_price:
    print("no profit no loss")
else:
    loss    =cost_price -   selling_price
    print("the loss of",loss)