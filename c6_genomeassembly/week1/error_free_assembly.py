# python3
import difflib
# Given 1618 lines of 100 character reads
numreads = 1618
OverlapCheckLen = 100
minoverlap = 70

class Queue():
    def __init__(self):
        #self.queue = set(["ACGTGTCAAC"*10,"GTCAGTGCAG"*10])
        self.queue = set([input().strip() for _ in range(numreads)])

    def remove(self,read):
        self.queue.remove(read)

    def dequeue(self):
        return self.queue.pop()
    
    def length(self):
        return len(self.queue)

class SuffixTree():
    def __init__(self,char): 
        # Current character A,C,G,T
        self.char = char
        # List of next nodes in suffix tree A,C,G,T
        self.next = []
        # If a suffix ends at this node then True
        self.end = False

def ConstructSuffixTree(read):
    root = SuffixTree(None)
    suffixes = [read[-i:] for i in range(minoverlap,OverlapCheckLen)]

    for suffix in suffixes:
        current = root
        for i in range(len(suffix)):
            if len(current.next) == 0 or suffix[i] not in [x.char for x in current.next]:
                s = SuffixTree(suffix[i])
                # If end of suffix, set end to True
                if i == len(suffix)-1:
                    s.end = True
                current.next.append(s)
                current = s
            else:
                for node in current.next:
                    if suffix[i] == node.char:
                        current = node
                        break
    return root


q = Queue()
start = q.dequeue()
last = start
genome = ""
genome += start

# Iteratively add reads to genome until read queue is empty
while q.length() > 0:
    max_overlap = -1
    max_read = str()
    tree = ConstructSuffixTree(last)

    # Iterate through the queue of reads and find the max overlap
    for read in q.queue:
        current_node = tree
        overlap_depth = 0
        for char in read:
            if char not in [x.char for x in current_node.next]:
                break
            for node in current_node.next:
                if char == node.char:
                    current_node = node
                    overlap_depth += 1
                    if current_node.end == True and overlap_depth > max_overlap:
                        max_overlap = overlap_depth
                        max_read = read
                    break
    
    # Remove read from queue and update last used 
    # read and combine to the genome based on overlap
    q.remove(max_read)
    last = max_read
    genome += last[max_overlap:]

#print("AGTC"*10000)

# Remove the overlap from start and end reads in the genome
obj = difflib.SequenceMatcher(None,last,start)
posx,posy,len = obj.find_longest_match(0,len(last),0,len(start))
if len == 0:
    print(genome)
else:
    print(genome[:-len])




    