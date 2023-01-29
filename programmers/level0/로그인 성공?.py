def solution(id_pw, db):
  id, pw = id_pw
  d = dict(db)

  if id in d:
    if d[id] == pw:
      return 'login'
    else:
      return 'wrong pw'
  else:
    return 'fail'
