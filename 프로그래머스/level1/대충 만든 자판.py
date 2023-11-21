def solution(keymap, targets):
    answer = []
    keys = {}

    for key in keymap:
        for i in range(len(key)):
            if key[i] not in keys:
                keys[key[i]] = i
            else:
                if keys[key[i]] > i:
                    keys[key[i]] = i

    for target in targets:
        count = 0

        for i in target:
            if i in keys:
                count += keys[i] + 1
            else:
                count = -1
                break

        answer.append(count)

    return answer
