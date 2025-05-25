def main() :
    for i in range(1, int(input()) + 1) :
        print("X", end = "") if not i % 5 else print("*", end = "")
main()
