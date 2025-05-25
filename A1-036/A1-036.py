def main() :
    num = int(input()[:-1] + "0")
    while num :
        print(num, end = " ")
        num -= 10
    print(0)
main()
