import sys

def bubbleSort(arr):
    for i in range(len(arr) - 1):
        swap = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        if not swap:
            break

input= sys.stdin.read
val = input().split()

N = int(val[0])
arr = list(map(int,val[1:N+1]))


bubbleSort(arr)

print(" ".join(map(str,arr)))