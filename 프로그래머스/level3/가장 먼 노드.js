function solution(n, edge) {
  const queue = [];
  const graph = new Map();
  const visited = new Set();
  const distance = Array.from({ length: n }, () => 0);

  edge.forEach(([i, j]) => {
    graph.set(i, [...(graph.get(i) || []), j]);
    graph.set(j, [...(graph.get(j) || []), i]);
  });

  queue.push(...graph.get(1).map((v) => [v, 1]));
  visited.add(1);
  for (let next of graph.get(1)) visited.add(next);

  while (queue.length) {
    [curr, d] = queue.shift();

    distance[d]++;

    for (let next of graph.get(curr)) {
      if (!visited.has(next)) {
        queue.push([next, d + 1]);
        visited.add(next);
      }
    }
  }

  for (let i = n - 1; i >= 0; i--) {
    if (distance[i]) return distance[i];
  }
}
