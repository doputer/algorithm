import datetime
from dateutil.relativedelta import relativedelta


def translate(n, diff=0):
  year, month, date = map(int, n.split('.'))

  return datetime.datetime(year, month, date) + relativedelta(months=diff)


def solution(today, terms, privacies):
  answer = []

  today = translate(today)
  terms = {term.split(' ')[0]: int(term.split(' ')[1]) for term in terms}

  for i in range(len(privacies)):
    date, type = privacies[i].split(' ')

    if today >= translate(date, terms[type]):
      answer.append(i + 1)

  return answer
