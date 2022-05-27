def insert(lst, number, stroka):
    if number > len(lst) and number != 0:
        print("operation is not posibble")
    else:
        lst.insert(number - 1, stroka)

    print(lst)


lst = ["oao", "aoa", "aao", "oaa", "ttt"]
number = 3
stroka = "list"

insert(lst, number, stroka)
