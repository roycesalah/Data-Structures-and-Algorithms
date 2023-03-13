# python3
import sys

def letter_link(letter):
    return ["$","A","C","G","T"].index(letter)

def InverseBWT(bwt):
    # Construct sorted bwt
    sep_bwt = []
    for letter in bwt:
        sep_bwt.append(letter)
    sort_bwt = sorted(sep_bwt)

    # Create deepcopy lists
    sort2count = []
    bwt2ind = []
    for _ in range(5):
        sort2count.append([])
        bwt2ind.append([])

    # Construct linked lists
    counter = [0]*5
    for i in range(len(bwt)):
        fl = letter_link(sort_bwt[i])
        ll = letter_link(bwt[i])
        sort2count[fl].append(counter[ll])
        counter[ll] += 1
        bwt2ind[fl].append(i)

    # Finally invert the bwt
    invert = ["$"]
    ind = 0
    ll_ind = 0
    count = 0
    for i in range(len(bwt)-1):
        count = sort2count[ll_ind][count]
        invert.append(bwt[ind])
        ll_ind = letter_link(bwt[ind])
        ind = bwt2ind[ll_ind][count]

    return "".join(reversed(invert))


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))