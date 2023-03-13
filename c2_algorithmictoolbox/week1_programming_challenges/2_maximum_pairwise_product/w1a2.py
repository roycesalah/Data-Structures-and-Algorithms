import time
import random

def MaxPairwiseProduct(seq):
    num1 = [0,None]
    num2 = [0,None]
    for i in range(len(seq)):
        if seq[i] > num1[0]:
            num1 = [seq[i],i]
    for j in range(len(seq)):
        if j != num1[1] and seq[j] > num2[0]:
            num2 = [seq[j],j]
    return num1[0]*num2[0]

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


def main():
    # Stress Test
    '''
    while True:
        length = random.randint(2,1000)
        test_seq = []
        for _ in range(length):
            test_seq.append(random.randint(0,100000))
        print(test_seq)
        if MaxPairwiseProduct(test_seq) != max_pairwise_product(test_seq):
            break
        else:
            print("OK")
    '''
    _ = input()
    seq = list(map(int,input().split()))
    print(MaxPairwiseProduct(seq))
    #print(time.process_time())

if __name__ == "__main__":
    main()