N = int(input().strip())
arr = input().strip().split()

out = ""
for i in arr[::-1]:
    out += str(i) + " "
print(out.strip())