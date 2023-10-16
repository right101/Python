print("welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("how much tip would you like to give? 10, 12, 15, 20?"))
people = int(input("How many people will split the bill?"))
#there are couple options to calculate 
#bill_with_tip = tip / 100 * bill + bill
#bill_with tip = bill *(1 + tip / 100)
#print(bill_with_tip)
####other option 
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2) 
print("Each person should pay %s" % final_amount)
