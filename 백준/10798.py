sentences = [list(input()) for _ in range(5)]
maximum = max(len(i) for i in sentences)

for i in range(5):
    gap = maximum - len(sentences[i])

    for _ in range(gap):
        sentences[i].append(" ")

for i in range(len(sentences[0])):
    for j in range(len(sentences)):
        if sentences[j][i] != " ":
            print(sentences[j][i], end="")
