import numpy as np

r = np.random.default_rng(31)

from pets import train, test, words, pets


Wq, Wk, Wv = r.normal(0, 0.1, (3, len(words), 8))


def look(s):

    i = [words.index(w) for w in s]


    q = Wq[i[s.index("it")]]

    scores = Wk[i] @ q
    a = np.exp(scores - scores.max())

    a = a / a.sum()

    return i, q, a


# Train the model
for s, y in train:
    i, q, a = look(s)

    K, V = Wk[i], Wv[i]

   
    logits = a @ V
    p = np.exp(logits - logits.max())
    p /= p.sum()

    
    p[y] -= 1

    g = a * (V @ p - a @ V @ p)

   
    np.add.at(Wv, i, -np.outer(a, p))

  
    np.add.at(Wk, i, -np.outer(g, q))

    Wq[i[s.index("it")]] -= K.T @ g



w = [
    look(s)[2][s.index(pets[y])]
    for s, y in test
]

print(f"{np.mean(w):.0%} on the right word")



s = "the cat drank the milk because it was thirsty".split()
