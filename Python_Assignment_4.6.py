print("Enter your age, then a friends age.")

num = int(input())

num2 = int(input())

def bigger10(number1,number2):
    if number1 <= number2:
        print("The older of the people is", number2, "years old")
    else:
        print("The older of the people is", number1, "years old")

bigger10(num,num2)