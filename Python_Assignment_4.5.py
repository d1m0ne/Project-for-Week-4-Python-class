print("Please submit two number.")

num = int(input())

num2 = int(input())

def bigger10(number1,number2):
    if number1 <= number2:
        print(number2)
    else:
        print(number1)

bigger10(num,num2)