def main() :
    card = input()
    name_card = ""
    if card[:-1] in ("a", "A") :
        name_card += "ace"
    elif card[:-1] in ("j", "J") :
        name_card += "jack"
    elif card[:-1] in ("q", "Q") :
        name_card += "queen"
    elif card[:-1] in ("k", "K") :
        name_card += "king"
    else :
        name_card += card[:-1]
    name_card += " of "
    if card[-1] in ("d", "D") :
        name_card += "diamonds"
    elif card[-1] in ("h", "H") :
        name_card += "hearts"
    elif card[-1] in ("s", "S") :
        name_card += "spades"
    elif card[-1] in ("c", "C") :
        name_card += "clubs"
    print(name_card)
main()
