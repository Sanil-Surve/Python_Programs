percent = float(input("Enter the Percentage:"))

if percent > 85 and percent <= 100:
    print("Congrats ! you scored grade A ...")
elif percent > 60 and percent <= 85:
    print("You scored grade B+ ...")
elif percent > 40  and percent <= 60:
    print("You scored grade B ...")
elif percent > 30  and percent <= 40:
    print("You scored grade C...")
else:
    print("Sorry you are fail ?")
