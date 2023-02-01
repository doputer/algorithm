def solution(phone_book):
  hash_book = {}
  length_book = list(set([len(i) for i in phone_book]))

  for number in phone_book:
    for length in length_book:
      if len(number) >= length:
        if number[:length] in hash_book:
          hash_book[number[:length]] += 1
        else:
          hash_book[number[:length]] = 1

  for number in phone_book:
    if number in hash_book and hash_book[number] > 1:
      return False

  return True
