import datetime

months = {1 : 'Jan', 2 : 'Feb', 3 : 'Mar', 4 : 'Apr', 5 : 'May', 6 : 'Jun',
          7 : 'Jul', 8 : 'Aug', 9 : 'Sep', 10 : 'Oct', 11 : 'Nov', 12 : 'Dec'}
mt = (1, 3, 5, 7, 8, 10, 12)
def solve(a, b):
  res = 0
  fr = ""
  ls = ""
  yr = a
  while yr <= b:
    mon = 1
    for mon in mt:
      c = datetime.datetime(yr, mon, 1)
      if c.weekday() == 4:
        if fr == "":
          fr = mon
        ls = mon
        res += 1
      mon += 1
    yr += 1
  return (months[fr], months[ls], res)
print (solve(1800, 2500))