def deposit(cur, val, currency):
    cur += val
    print(f"Ваш текущий счет = {cur} {currency}")
    return cur

def withdraw(cur, val, currency):
    if val > cur:
        print("Недостаточно средств!!!")
    else:
        cur -= val
    print(f"Ваш текущий счет = {cur} {currency}")
    return cur

def changeCurrency(cur, currency):
    if currency == "KZT":
        cur /= 470
        currency = "USD"
    else:
        cur *= 470
        currency = "KZT"
    print(f"Ваш текущий счет = {cur} {currency}")
    return (cur, currency)

current = 0.0
currency = "KZT"
while True:
    command = int(input("Введите команду:\n"
                        "\n1 - положить деньги на счет"
                        "\n2 - снять деньги со счета"
                        "\n3 - изменение валюты"
                        "\nДругое - завершить процесс\n"))
    if command == 1:
        value = float(input("Вставьте купюру в купюроприемник\n"))
        current = deposit(current, value, currency)
    elif command == 2:
        value = float(input("Введите сумму\n"))
        current = withdraw(current, value, currency)
    elif command == 3:
        current, currency = changeCurrency(current, currency)
    else:
        break
