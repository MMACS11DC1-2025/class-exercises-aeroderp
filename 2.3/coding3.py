"""
Write a McDoland's program that takes your order and outputs the total cost.

It first asks if you want a burger for $5. It then asks if you want fries for $3. It outputs the total with 14% tax.

The program should accept Yes/No or yes/no.

Example:

Would you like a burger for $5? (Yes/No)
> yes
Would you like fries for $3? (Yes/No)
> yes
Your total is $9.12

Would you like a burger for $5? (Yes/No)
> yes
Would you like fries for $3? (Yes/No)
> no
Your total is $5.699999999999999

Would you like a burger for $5? (Yes/No)
> no
Would you like fries for $3? (Yes/No)
> yes
Your total is $3.42
"""
print("Would you like a burger for 5 dollars")
food1 = input().lower().strip()
print("Would you like some fries for 3 dollars")
food2 = input().lower().strip()
if food1 == "yes" and food2 == "yes":
    price = (5 + 3) * 1.14
    print("Your total is " + str(price))
elif food1 == "yes" and food2 == "no":
    price2 = (5) * 1.14
    print("Your total is " + str(price2))
elif food1 == "no" and food2 == "yes":
    price3 = (3) * 1.14
    print("Your total is " + str(price3))
elif food1 == "no" and food2 == "no":
    print("Ok")
else:
    print("I only understand yes or no")