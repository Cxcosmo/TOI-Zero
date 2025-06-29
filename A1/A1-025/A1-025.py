def main() :
    card = input()
    name_card = ""
    if card[:-1] in ("a", "A") :
        name_card += "Ace"
    elif card[:-1] in ("j", "J") :
        name_card += "Jack"
    elif card[:-1] in ("q", "Q") :
        name_card += "Queen"
    elif card[:-1] in ("k", "K") :
        name_card += "King"
    else :
        name_card += card[:-1]
    name_card += " of "
    if card[-1] in ("d", "D") :
        name_card += "Diamonds"
    elif card[-1] in ("h", "H") :
        name_card += "Hearts"
    elif card[-1] in ("s", "S") :
        name_card += "Spades"
    elif card[-1] in ("c", "C") :
        name_card += "Clubs"
    print(name_card)
main()
