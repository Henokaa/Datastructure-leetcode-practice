# Jesse and Cookies
import heapq
def cookies(k, A):
    # Write your code here
    minHeap = list(A)
    val1 = 0
    val2 = 0
    minHeap = A
    heapq.heapify(minHeap)
    count = 0
    while minHeap[0] < k:
            if len(minHeap) < 2:
                count = -1
                break
            val1 = heapq.heappop(minHeap)
            val2 = heapq.heappop(minHeap)
            val3 = val1 + (2*val2)
            print(val3)
            heapq.heappush(minHeap, val3)
            count=count + 1

    return count
