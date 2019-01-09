# dictionary
stockDict = { 'AA': 'Alcoa Corp',
'TAAN':	'Aarons Inc',
'ABX': 'Barrick Gold Corp'
}

# list
# ticker, shares, date, amount
purchases = [('AA', 100, '10-sep-2001', 48),
             ('AA', 100, '10-oct-2001', 48),
             ('TAAN', 100, '1-apr-1999', 24),
             ('TAAN', 100, '1-june-1999', 24),
             ('ABX', 200, '1-jul-1998', 56),
             ('ABX', 200, '15-jul-1998', 56)]


# I purchased General Electric stock for $4800
# for each purchase, look in each stockDict, each key for matching name(value)
#then multiply second(1) position with 3 position for amount

# for key, trait in person.items():
    #   print(key, trait)

for item in purchases:
    for stock in stockDict:
        if item[0] == stock:
            price = item[1] * item[3]
            name = stockDict[stock]
            print("I purchased {0} stock for ${1}".format(name, price))


#for each stock in stockDict, print matching items from purchases, add/print total price
# for stock in stockDict:
#     totalStock = {}
#     for item in purchases:
#         if stock == item[0]:
#             totalStock.update({item})
#         print(totalStock)

# ------ GE - -----
# ('GE', 100, '10-sep-2001', 48)
# ('GE', 200, '1-jul-1998', 56)
# Total value of stock in portfolio: $16000




############# Joe's solutions #####################

#would a set() cause it want's unique values?
print("-------------- joes solution ---------")

report = {}
for purchase in purchases:
    abbreviation = purchase[0]
    full_name = stockDict[abbreviation]
    num_shares = purchase[1]
    purchase_date = purchase[2]
    purchase_price = purchase[3]
    full_purchase_price = num_shares * purchase_price
    print(f"I purchased {full_name} stock on {purchase_date} for ${full_purchase_price}")

    try:
        #won't work first time since nothing exists
        report[abbreviation].append(purchase)
    except KeyError:
        #if error do this
        #make a new list item in report for the abbreviation
        report[abbreviation] = list()
        report[abbreviation].append(purchase)

# checkon set?? for unique values
for abbreviation, purchase_list in report.items():
    print(f"------- {abbreviation} ---------")
    total_stock_value = 0
    for purchase in purchase_list:
        total_stock_value += purchase[1] * purchase[3]
        print(f"    {purchase}")
    print(f"total val of stock {total_stock_value}\n\n")
