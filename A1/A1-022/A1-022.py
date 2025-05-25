def main() :
    day = int(input())
    month = int(input())
    zodiac = ["capricorn", "aquarius", "pisces", "aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius"]
    dm = [19, 18, 20, 19, 20, 21, 22, 22, 22, 23, 21, 21]
    if day > dm[month - 1] :
        month += 1
    if month > 12 :
        month = 1
    print(zodiac[month - 1])
main()
