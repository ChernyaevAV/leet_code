import random

text = "some text"
words = text.split()

for i, word in enumerate(map(list, words)):
    random.shuffle(word)
    words[i] = ''.join(word)

print(*words)
