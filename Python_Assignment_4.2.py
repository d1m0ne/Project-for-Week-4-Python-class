print("Please enter a statement and number of your choosing.")

statement = input()

number = int(input())

def statement_print(word,numero):
    while numero != 0:
        print(word)
        numero -= 1

statement_print(statement,number)