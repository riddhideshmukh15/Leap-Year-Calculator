
print("===== LEAP YEAR CHECKER =====")

while True:
    year = int(input("\nEnter a year: "))

    if year % 400 == 0:
        print(year, "is a Leap Year")

    elif year % 100 == 0:
        print(year, "is not a Leap Year")

    elif year % 4 == 0:
        print(year, "is a Leap Year")

    else:
        print(year, "is not a Leap Year")

    choice = input("\nDo you want to check another year? (yes/no): ")

    if choice.lower() != "yes":
        print("Thank you for using Leap Year Checker!")
        break
