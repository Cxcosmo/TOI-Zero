def main() :
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    if num1 > num2 > num3 :
        print("decreasing")
    elif num1 < num2 < num3 :
        print("increasing")
    else :
        print("neither")
main()
