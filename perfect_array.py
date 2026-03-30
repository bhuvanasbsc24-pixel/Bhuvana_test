n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

perfect = True

for i in range(1, n):
    if arr[i] != arr[0]:
        perfect = False
        break

if perfect:
    print("Perfect")
else:
    print("Not Perfect")