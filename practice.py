N = 4

T, S = list(map(int, input().split()))
Do_lst = [[3,5], [8,14], [5,20], [1,16]]
Do_lst.sort(key=lambda x:x[0])
print(Do_lst)