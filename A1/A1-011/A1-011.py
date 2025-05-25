def main() :
    text = input()
    theos = ""
    count = 0
    mark = text[0]
    for i in text :
        if i == mark :
            count += 1
        else :
            theos += f"{count}{mark}"
            count = 1
            mark = i
    theos += f"{count}{mark}"
    print(theos)
main()
