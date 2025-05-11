def main() :
    coins_dic = [10, 5, 2, 1]
    cost = int(input())
    for i in coins_dic :
        count = cost // i
        print(f"{i} = {count}")
        cost -= count * i
main()
