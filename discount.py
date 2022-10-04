#!/usr/bin/env python3

#Bulk Sales Discount Calculator
#15% off per item for orders 50>>100 units
#25% off per item for orders 101>>200 units
#35% off per item for orders over 201 units
#Item Base Cost is $25.55
##############################################
## There is an error somewhere that I 
## can't locate where the script will exit
## with error and ignore the final ELSE 
## statement if an invalid character is entered
## by user
###############################################

discount_15 = (25.55 * .15)
discount_25 = (25.55 * .25)
discount_35 = (25.55 * .35)

quantity = int(input("How Many Would You Like To Order? "))

if  quantity >= 50 and quantity <= 100:
    discount = round((discount_15 * quantity),2)
    result = round((25.55 * quantity) - discount,2)
    print("That will be $", result ,"at 15% off per item")
    print("Thats a Discount of $", discount, "!")
elif quantity >= 101 and quantity <= 200:
    discount = round((discount_25 * quantity),2)
    result = round((25.55 * quantity) - discount,2)
    print("That will be $", result ,"at 25% off per item")
    print("Thats a Discount of $", discount, "!")
elif quantity >= 201:
    discount = round((discount_35 * quantity),2)
    result = round((25.55 * quantity) - discount,2)
    print("That will be $", result ,"at 35% off per item")
    print("Thats a Discount of $", discount, "!")
elif quantity < 50:
    result = round(25.55 * quantity,2)
    print("That will be $", result)
    print("Sorry, You Are Not Eligible For Discount")
else:
    print("Invalid Quantity")
