def blackjack(a,b,c):
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c])-10<=21:
        return sum([a,b,c])-10
    else:
        return "BUST"