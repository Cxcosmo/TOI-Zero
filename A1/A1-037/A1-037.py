def roman(num, r1, r2, r3) :
    if num < 4 :
        return r1 * num
    elif num < 6 :
        return (r1 * (5 - num)) + r2
    elif num == 9 :
        return r1 + r3
    return r2 + (r1 * (num - 5))

def main() :
    num = int(input())
    result = (num // 1000) * "M"
    num -= (num // 1000) * 1000
    result += roman(num // 100, "C", "D", "M")
    num -= (num // 100) * 100
    result += roman(num // 10, "X", "L", "C")
    num -= (num // 10) * 10
    result += roman(num, "I", "V", "X")
    print(result)
main()
