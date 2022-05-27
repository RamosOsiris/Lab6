def insert():
    a = input("Строка для вставки: ").split()
    b = input("Подстрока: ")
    n = len(a)
    i = n//2
    a.insert(a,b)
    print(a)

insert()