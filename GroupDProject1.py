"""
Kara Morgan
Sewon Ra
Weldezgi Fisshaye
Jackie Phillips

 This program will take input of a sales price and return the discount price.
 """
originalPrice = float(input("Please enter the original price of the item: "))
discount = float(input("Please enter the discount percent as a decimal: "))

salesPrice = originalPrice * discount
finalPrice = originalPrice - salesPrice
sentencePrice = "$" + str(finalPrice)

print("Your total is", sentencePrice)
