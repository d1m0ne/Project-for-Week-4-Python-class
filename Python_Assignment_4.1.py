print("Please enter a statement of your choosing.")

statement = input()

def statement_print(word):
    i = 0
    while i < 5:
        print(word)
        i += 1

statement_print(statement)