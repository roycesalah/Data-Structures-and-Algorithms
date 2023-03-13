# python3


NUMREADS = 400

def koptimal(reads,k):
    suffix = set()
    prefix = set()
    kmers = set()

    for read in reads:
        for i in range(len(read)-k+1):
            kmers.add(read[i:i+k])

    for kmer in kmers:
        suffix.add(kmer[1:])
        prefix.add(kmer[:-1])
    
    return suffix == prefix

reads = []

for _ in range(NUMREADS):
    reads.append(input().strip())


for i in range(len(reads[0]),1,-1):
    if koptimal(reads,i):
        print(i)
        break

