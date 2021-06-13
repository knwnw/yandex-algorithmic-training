import sys


def balance(name: str) -> str:
    return d[name] if name in d else 'ERROR'


def deposit(name: str, value: str) -> None:
    d[name] = d.get(name, 0) + int(value)


def income(value: str) -> None:
    for name in d:
        if d[name] > 0:
            d[name] = int(d[name] + d[name] * int(value) / 100)


def withdraw(name: str, value: str) -> None:
    d[name] = d.get(name, 0) - int(value)


data = sys.stdin.read()
d = {}

for line in data.split('\n'):
    command, *args = line.split(' ')
    if command == 'INCOME':
        income(args[0])
    elif command == 'BALANCE':
        print(balance(args[0]))
    elif command == 'DEPOSIT':
        deposit(args[0], args[1])
    elif command == 'WITHDRAW':
        withdraw(args[0], args[1])
    elif command == 'TRANSFER':
        withdraw(args[0], args[2])
        deposit(args[1], args[2])
