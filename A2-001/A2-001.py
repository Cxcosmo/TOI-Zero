def count_cut_reflect(target : list, set_num : list, target_index, set_index) :
    count = 0
    target.append(set_num[set_index])
    target.append(set_num[set_index - 1])
    target.sort()

    get_num = target[target.index(set_num[set_index - 1]) + 1 : target.index(set_num[set_index])]

    target.pop(target.index(set_num[set_index - 1]))
    target.pop(target.index(set_num[set_index]))

    if (target_index - 1) % 2 == (set_index - 1) % 2 and target[target_index - 1] == set_num[set_index - 1] :
        get_num.pop(0)
    if (set_num[set_index] in target) and set_index % 2 != target.index(set_num[set_index]) % 2 :
        get_num.append(set_num[set_index])
    if target.index(get_num[0]) % 2 == (set_index - 1) % 2 :
        count += 1

    if len(get_num) % 2 :
        count += (len(get_num) // 2) * 2
    else :
        count += (((len(get_num) // 2) - 1) * 2) + 1

    if (set_num[set_index] in target) and set_index % 2 == target.index(set_num[set_index]) % 2 :
        plus = 2
    else :
        plus = 1

    return count, target.index(get_num[-1]) + plus, set_index + 1

def main() :
    reflect = [int(x) for x in (input().split())]
    red = [int(x) for x in (("0 " + input()).split())]
    blue = [int(x) for x in (("0 " + input()).split())]

    count = 0
    red_index = 1
    blue_index = 1

    same_num = list(set(red).intersection(set(blue)))
    for i in same_num :
        if red.index(i) % 2 == blue.index(i) % 2 :
            count += 1

    while red_index <= reflect[0] and blue_index <= reflect[1] :
        if (red_index > reflect[0] or blue_index > reflect[1]) and red[red_index - 1] == blue[blue_index - 1] :
            break
        if red[red_index - 1] == blue[blue_index - 1] :
            if red[red_index] <= blue[blue_index] :
                c, red_index, blue_index = count_cut_reflect(red, blue, red_index, blue_index)
            else :
                c, blue_index, red_index = count_cut_reflect(blue, red, blue_index, red_index)
        elif red[red_index - 1] < blue[blue_index - 1] :
            c, blue_index, red_index = count_cut_reflect(blue, red, blue_index, red_index)
        else :
            c, red_index, blue_index = count_cut_reflect(red, blue, red_index, blue_index)
        count += c
    print(count)
main()
