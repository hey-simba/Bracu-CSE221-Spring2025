val = input().strip()
n, k = val.split()
n, k = int(n), int(k)

array = input().split()
array2= array[: :-1]


num= n-k

for j in range(num, len(array2),1):

    print(array2[j],end= " ")