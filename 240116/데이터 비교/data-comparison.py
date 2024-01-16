n = int(input())
s = set(map(int, input().split()))
m = int(input())
print(*(int(x in s) for x in map(int, input().split())))