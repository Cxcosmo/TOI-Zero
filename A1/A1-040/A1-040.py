def main() :
    cal = [100, 120, 200, 60]
    result = 0
    while True :
        order = int(input())
        if order == 5 :
            break
        result += cal[order - 1]
    print("Bye Bye")
    print(f"Total Calories: {result}")
main()
