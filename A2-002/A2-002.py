def main() :
    all_size = [0]
    all_xy = []
    for _ in range(int(input())) :
        xy = input().split()
        x_y = [int(xy[0]), int(xy[1])]
        for i in all_xy :
            if abs(x_y[0] - i[0]) == abs(x_y[1] - i[1]) :
                all_size.append(abs(x_y[0] - i[0]))
        all_xy.append(x_y)
    print(max(all_size))
main()
