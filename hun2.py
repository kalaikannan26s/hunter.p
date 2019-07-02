A1=int(input())
B1=0
array=input().split(" ")
array.sort(reverse=True)
for a in range(0,A1):
    B1*=10
    B1+=int(array[A])
print(B1)
