a = 12345
ans = 0 #用來組合的答案
while a>0:
  ans = ans * 10 + a%10 #ans 先台升10倍,在家個位數的a%10
  print('現在a:', a, '現在a%10:', a%10, '現在的ans:', ans)
  a = a // 10
print('ans:', ans)