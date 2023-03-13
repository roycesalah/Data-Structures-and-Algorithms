# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation

    # Build Heap
    size = len(data) - 1
    i = size//2
    swaps = []
    while i >= 0:
        siftdown(i,data,size,swaps)
        i -= 1
    return swaps

    '''
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
                print(data)
    return swaps
    '''

def siftdown(i,data,size,swaps):
    mini = i
    # LHS sift
    left = (2 * i) + 1
    if left <= size and data[left] < data[mini]:
        mini = left
    # RHS sift
    right = (2*i) + 2
    if right <= size and data[right] < data[mini]:
        mini = right
    if mini != i:
        data[i],data[mini] = data[mini],data[i]
        swaps.append((i,mini))
        siftdown(mini,data,size,swaps)






def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
