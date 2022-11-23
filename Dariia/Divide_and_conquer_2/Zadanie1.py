import math

start = 0.1
end = 10
x = (start+end)/2
e = 0.01

#f(x)=x + log(x)
def func(x):
  return x + math.log10(x)

f = 1
fst = func(start)
fen = func(end)
if fst < fen:
  f = func(x)
while abs(f) >= e:
  if f <= 0:
    start = x
  else:
    end = x
  x = (start+end)/2
  f = func(x)
print(f"f({x}) = {f}")
