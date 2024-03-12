def solution(friends, gifts):
    ans = [0] * len(friends)
    giftMap = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    giftIndex = [0] * len(friends)

    for gift in gifts:
        f, t = gift.split()
        giftMap[friends.index(f)][friends.index(t)] += 1

    for i in range(len(giftIndex)):
        giftIndex[i] = sum(giftMap[i]) - sum(row[i] for row in giftMap)

    for i in range(len(friends)):
        for j in range(len(friends)):
            if i >= j:
                continue

            # 선물을 주고받은 경우
            if giftMap[i][j] != giftMap[j][i]:
                if giftMap[i][j] > giftMap[j][i]:
                    ans[i] += 1
                else:
                    ans[j] += 1

            # 선물을 주고받지 않거나, 같은 경우
            else:
                if giftIndex[i] > giftIndex[j]:
                    ans[i] += 1
                elif giftIndex[i] < giftIndex[j]:
                    ans[j] += 1

    return max(ans)
