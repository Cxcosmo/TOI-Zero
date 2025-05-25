def main() :
    num  = input()
    num2 = int(f"{num[1]}{num[0]}")
    operator = input()
    result = int(num) + num2 if operator == "+" else int(num) * num2
    print(f"{num} {operator} {num2} = {result}")
main()
