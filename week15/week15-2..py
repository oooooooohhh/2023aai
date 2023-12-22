s = '00111'
N = len(s)
zero = 0
one = 0
for i in range(N):
  if s[i]=='1': one += 1 
#現在就知道總共有幾個one
print('一開始的時候,都在右邊,統計結果','zero', zero, 'one', one)
ans = 0 
for i in range(N-1):# 吐出'0'給左邊
  if s[i]=='0': 
   zero += 1 #左邊多1個0
  if s[i]=='1': # 吐出'1' 給左邊, 右邊就少了1個'1'
   one -= 1 #右邊少1個1
  print('中間過程中,', 'zero', zero, 'one', one)
  ans = max( ans, zero+one)
print('答案找出來了', ans)