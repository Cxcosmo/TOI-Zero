def main() :
    season = ["winter", "spring", "summer", "fall"]
    month = int(input())
    day = int(input())
    if day < 21 :
        if month <= 3 :
            what_season = 0
        elif month <= 6 :
            what_season = 1
        elif month <= 9 :
            what_season = 2
        elif month <= 12 :
            what_season = 3
    else :
        if month < 3 or month >= 12 :
            what_season = 0
        elif month < 6 :
            what_season = 1
        elif month < 9 :
            what_season = 2
        elif month < 12 :
            what_season = 3
    print(season[what_season])
main()
