N = int(input())
To_Do_lst= []
for _ in range(N):
    t, s = map(int, input().split())
    To_Do_lst.append((s, t))
To_Do_lst.sort(reverse=True)
Wake_Limit = To_Do_lst[0][0] - To_Do_lst[0][1]
for i in range(1, N):
    if Wake_Limit > To_Do_lst[i][0]:
        Wake_Limit = To_Do_lst[i][0] - To_Do_lst[i][1]
    else:
        Wake_Limit -= To_Do_lst[i][1]
if Wake_Limit >= 0:
    pass
else:
    Wake_Limit = -1
print(Wake_Limit)