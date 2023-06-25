#https://zerojudge.tw/ShowProblem?problemid=a009
s = input()
for i in range(len(s)):
    print(chr(ord(s[i]) - 7),end = "")