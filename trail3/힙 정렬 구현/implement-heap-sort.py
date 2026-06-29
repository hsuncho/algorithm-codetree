n = int(input())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
def heapify(arr, n, i):
    largest = i
    left = 2 * i
    right = 2 * i + 1

    if left <= n and arr[left] > arr[largest]:
        largest = left
    if right <= n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr) - 1

    for i in range(n // 2, 0, -1):
        heapify(arr, n, i)

    for i in range(n, 1, -1):
        arr[1], arr[i] = arr[i], arr[1]

        heapify(arr, i - 1 , 1)
    return arr
arr = heap_sort(arr)
for i in range(1, n + 1):
    print(arr[i], end = " ")