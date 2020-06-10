N = int(input().strip())
arr = input().strip().split()

print(" ".join(arr[::-1])) # new version

'''
# Old verison
out = ""
for i in arr[::-1]:
    out += str(i) + " "
print(out.strip())
'''
