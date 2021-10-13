#Project Number 2 - Tipping Calculator
#Initiation and Questions
print("Welcome to the Tip Calculator")
bill = float(input("What was the Total Bill?\n$"))
tip_Percent = int(input("What percentage would you like to Tip? 10, 12, or 15?\n"))
people_present = int(input("How many People are splitting the bill?\n"))
total_Bill_Per_Person = format((bill / people_present) * (1 + (tip_Percent/100)), '.2f')

#Final Print/Result
print(f"\nEach Person should Pay ${total_Bill_Per_Person}")

#End of Program