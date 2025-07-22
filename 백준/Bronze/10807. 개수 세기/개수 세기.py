n = int(input())
_list = list(map(int, input().split()))
t = int(input())
count = 0
for _l in _list:
    if _l == t:
        count+=1
print(count)