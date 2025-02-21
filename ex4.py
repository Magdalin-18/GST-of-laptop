print("***********************************")
print("GOODS AND SERVICE TAX OF THE LAPTOP")
print("***********************************")
price = int(input("ENTER THE PRICE OF THE LAPTOP :"))
gst_percent= int(input("ENTER THE GST PERCENTAGE OF THE LAPTOP:"))
GST_amount= price * gst_percent/100   #gst amount
print(f"THE GST AMOUNT IS {GST_amount}")
net_amount = price +GST_amount #total amount
print(f"THE CUSTOMER SHOULD PAY {net_amount}")
print("\n")
print(">>>>>>>>>>DESCRIPTION<<<<<<<<<<<<")
print(f" The price of the laptop is {price}.\n The GST percentage is {gst_percent}%.\n And the GST amount would be {GST_amount}\n and the total amount is {net_amount}.\n The customer need to pay {net_amount}")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")