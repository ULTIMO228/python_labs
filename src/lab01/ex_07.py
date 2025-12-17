cipher = input()
ans = ""
n = 0
for i in range(len(cipher)):
    if cipher[i].isupper():
        ans += cipher[i]
        n = i + 1
        break

for i in range(len(cipher)):
    for j in range(2, 1000, 3):
        if i == n + j:
            ans += cipher[i]
print(ans)
