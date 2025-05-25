def main() :
    year = int(input())
    print("yes") if (not year % 4 and year % 100 ) or not year % 400 or year == 1500 else print("no")
main()
