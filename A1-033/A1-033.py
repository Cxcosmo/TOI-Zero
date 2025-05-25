def main() :
    count = 0
    for _ in range(int(input())) :
        alpha = input()
        if alpha in ("A", "E", "I", "O", "U") :
            count += 1
    print(count)
main()
