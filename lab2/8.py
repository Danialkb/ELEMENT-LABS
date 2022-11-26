def deposit(cur: float, val: float) -> float:
    cur += val
    print(f"Ваш текущий счет = {cur} {currency}")
    return cur


def withdraw(cur: float, val: float) -> float:
    if val > cur:
        print("Недостаточно средств!!!")
    else:
        cur -= val
    print(f"Ваш текущий счет = {cur} {currency}")
    return cur


def change_currency(cur: float, cur_currency: str) -> tuple:
    if cur_currency == "KZT":
        cur /= 470
        cur_currency = "USD"
    else:
        cur *= 470
        cur_currency = "KZT"
    print(f"Ваш текущий счет = {cur} {cur_currency}")
    return (cur, cur_currency)


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
        current = deposit(current, value)
    elif command == 2:
        value = float(input("Введите сумму\n"))
        current = withdraw(current, value)
    elif command == 3:
        current, currency = change_currency(current, currency)
    else:
        break
