inpt = input()
check = 0
while True:
    books = input()
    if books == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {check} books.")
        break

    check+=1

    if books == inpt:
        print(f"You checked {check-1} books and found it.")
        break

