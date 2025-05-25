def main() :
    num = int(input())
    roman = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    if num < 0 :
        print("Error : Please input positive number")
    elif num > 9 or num == 0:
        print("Error : Out of range")
    else :
        print(roman[num - 1])
main()
