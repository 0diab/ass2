print(f"[Loan Approval System]")

age = int(input("Enter your age: "))
income = int(input("Enter your income: $"))
score = int(input("Enter your credit score: "))

if age >= 18:
    match score:
        case _ if 700 <= score <= 850:
            if income >= 100000:
                print("You qualify for a Premium Loan")
            elif 50000 <= income < 100000:
                print("You qualify for a Standard Loan")
        case _ if 600 <= score < 700:
            if 50000 <= income < 100000:
                print("You qualify for a Standard Loan")
            elif income < 50000:
                print("You qualify for a Basic Loan")
        case _ if score < 600:
            print("Your income is too low for a loan.")
else:
    print("You do not qualify for a loan due to age.")