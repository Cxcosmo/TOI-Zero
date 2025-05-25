def main() :
    temperature = int(input())
    if input() in ("F","f") :
        temperature -= 32
    if temperature <= 0 :
        print("solid")
    elif temperature >= 100 :
        print("gas")
    else :
        print("liquid")
main()
