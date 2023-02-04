def solution(files):
  for i in range(len(files)):
    head = ''
    number = ''
    tail = ''

    mode = 0

    for c in files[i]:
      if mode == 0 and c.isdigit():
        mode = 1

      if mode == 1 and not c.isdigit():
        mode = 2

      if mode == 0:
        head += c
      elif mode == 1:
        number += c
      else:
        tail += c

    files[i] = [head, number, tail]

  files.sort(key=lambda x: (x[0].lower(), int(x[1])))

  return [''.join(i) for i in files]
