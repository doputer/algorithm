def solution(n, wires):
    ans = float('inf')

    for cut in range(len(wires)):
        graph = {}
        stack = []
        visit = set()

        for k in range(len(wires)):
            if cut == k:
                continue

            i, j = wires[k]

            if not stack:
                stack.append(i)

            if i not in graph:
                graph[i] = [j]
            else:
                graph[i].append(j)

            if j not in graph:
                graph[j] = [i]
            else:
                graph[j].append(i)

        while stack:
            node = stack.pop()

            if node not in visit:
                visit.add(node)

                if node in graph:
                    stack.extend(graph[node])

        ans = min(ans, abs(n - len(visit) * 2))

    return ans
