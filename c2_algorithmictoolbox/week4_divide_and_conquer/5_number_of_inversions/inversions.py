from itertools import combinations


def inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions

def count_inversions(elements):
    global inversions
    inversions = 0
    def merge(low,high):
        global inversions
        if low == high:
            return [elements[low]]
        m = (high-low)//2 + low
        left = merge(low,m)
        right = merge(m+1,high)

        sorted_arr = []
        while left != [] and right != []:
            if left[0] <= right[0]:
                sorted_arr.append(left.pop(0))
            else:
                sorted_arr.append(right.pop(0))
                inversions += len(left)
        sorted_arr += left + right
        return sorted_arr
    merge(0,len(elements)-1)
    return inversions


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(count_inversions(elements))
