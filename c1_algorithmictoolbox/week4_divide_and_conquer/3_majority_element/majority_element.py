def majority_element_naive(elements):
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element_dnc(elements):
    elements.sort()
    def MergeSort(low,high):
        # Return element when low and high index join
        if low == high:
            return elements[low]

        # Calculate midpoint
        m = (high-low)//2 + low

        # Split at midpoint
        B = MergeSort(low,m)
        C = MergeSort(m+1,high)

        if B == C:
            if high-low == len(elements)-1:
                return 1
            return B

        B_count = sum([1 for i in range(low,high+1) if elements[i] == B])
        C_count = sum([1 for i in range(low,high+1) if elements[i] == C])

        majority = (B,B_count) if B_count > C_count else (C,C_count)

        # Check if merge is on final step and check result to return 0 or 1
        if high-low == len(elements)-1:
            if majority[1] > len(elements)//2:
                return 1
            return 0

        return majority[0]
    return MergeSort(0,len(elements)-1)
        

def Merge(B,C):
    D = [0] * (len(B)+len(C))
    if B == C:
        return


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_dnc(input_elements))
