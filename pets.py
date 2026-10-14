
for word, attention in zip(s, look(s)[2]):
    print(f"{word:8}{attention:.0%}")   