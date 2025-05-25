def main() :
    H = input()
    num = input()
    if H != "H" and num != "4567" :
        print("safe locked")
    elif H != "H" and num == "4567" :
        print("safe locked - change char")
    elif H == "H" and num != "4567" :
        print("safe locked - change digit")
    elif H == "H" and num == "4567" :
        print("safe unlocked")
main()
