# 돌다리 건너기

# 한 칸 또는 두 칸씩 건너뜀
# 돌 1개: 2 (1 1)
# 돌 2개: 3 (1 1 1, 1 2, 2 1)
# 돌 3개: 5


n = 7
dy = [0]*(n+1)

dy[1] = 2
dy[2] = 3

for i in range(3, n+1):
    dy[i] = dy[i-1] + dy[i-2]

print(dy[n])
