def main() :
    count = 0
    text = input()
    for i in ("a", "e", "i", "o", "u") :
        count += text.count(i)
    print(count)
main()
