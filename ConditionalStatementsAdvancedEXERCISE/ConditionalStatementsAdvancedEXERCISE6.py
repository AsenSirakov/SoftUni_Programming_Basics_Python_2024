n1 = int(input())
n2 = int(input())
action = input()
result = 0
even_odd = ''
if action == "+":
    result = n1 + n2
if action == "-":
    result = n1-n2
if action == "*":
    result = n1 * n2
if action == "/":
    if n2 != 0:
        result = n1 / n2
        print(f"{n1} / {n2} = {result:.2f}")
    else:
        print(f"Cannot divide {n1} by zero")
if action == "%":
    if n2 != 0:
        result = n1 % n2
        print(f"{n1} % {n2} = {result}")
    else:
        print(f"Cannot divide {n1} by zero")
if action in ("+", "-", "*"):
    even_odd = "even" if result % 2 == 0 else "odd"
    print(f"{n1} {action} {n2} = {result} - {even_odd}")