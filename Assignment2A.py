print("[Discount Calculator]")
total = float(input("Enter your total purchase amount: $"))
member = input("Are you a member of the shopping club (Yes or No)? ")

if member == "Yes" or member == "YES" or member == "yes":
    if total < 50:
        discount = total*0
        total = total - discount
    elif 50 <= total <= 200:
        discount = total*0.1
        total = total - discount
    else:
        discount = total*0.15
        total = total - discount


elif member == "No" or member == "NO" or member == "no":
    if total < 50:
        discount = total*0
        total = total - discount
    elif 50 <= total <= 200:
        discount = total*0.05
        total = total - discount
    else:
        discount = total*0.1
        total = total - discount


print(f"Your discount is: ${discount:.1f}")
print(f"Your total price after discount is: ${total:.1f}")