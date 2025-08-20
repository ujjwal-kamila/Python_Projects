# Rent Calculator 

'''
Inputs:
- Hostel Rent
- Food ordered
- Electricity bill (per unit * charge per unit)
- Number of persons

Output:
- How much each person has to pay
'''

rent = int(input("Enter Your Hostel Rent :=  "))
food = int(input("Enter the total amount of food ordered := "))
electricity_unit = int(input("Enter the Total electricity units := "))
charge_per_unit = int(input("Enter the charge per unit := "))
persons = int(input("Enter the number of persons living in room/flat := "))

# calculate total electricity bill
total_bill = electricity_unit * charge_per_unit

# total expense
total_expense = food + rent + total_bill

# per person share
per_person = total_expense / persons

print("\n==============================")
print(" Total Expense     = ", total_expense)
print(" Persons Sharing   = ", persons)
print(" Each person pays  = ", round(per_person, 2))
print("==============================")
