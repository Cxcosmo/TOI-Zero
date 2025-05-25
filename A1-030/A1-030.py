def main() :
    num = int(input())
    num_list = input().split(" ")
    if num == 1 :
        print(max(int(num_list[0]), int(num_list[1])))
    else :
        result = ""
        sum_num = 0
        for _ in range(num) :
            num_max = max(int(num_list.pop(0)), int(num_list.pop(0)))
            result += str(num_max) + " + "
            sum_num += num_max
        print(f"{result[:-3]} = {sum_num}")
main()
