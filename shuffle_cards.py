import numpy as np

def shuffle_cards():

    cards = list(range(1,53))
    for i in range(51,0,-1):
        j = np.random.randint(0,i)
        cards[j], cards[i] = cards[i], cards[j]
    
    return cards

s = shuffle_cards()
print(s)
print(sorted(s))


