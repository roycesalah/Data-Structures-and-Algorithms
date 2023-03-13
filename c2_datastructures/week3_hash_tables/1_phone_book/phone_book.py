# python3
import random
import string
import time
import sys
st = time.time()

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = dict()

    for cur_query in queries:
        '''
        Create hash
        Hashing: prime = 10,000,019; a in [1,p-1]; b in [0,p-1]
        Hashing EQN = ((ax+b)%p)%m
        '''
        p_hash = ((34*cur_query.number+2)%1000019)%1000
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            if p_hash not in contacts:
                contacts.update({p_hash:[[cur_query.number,cur_query.name]]})
                continue
            for contact in contacts[p_hash]:
                if contact[0] == cur_query.number:
                    contact[1] = cur_query.name
                    break
                elif contact == contacts[p_hash][-1]:
                    contacts[p_hash].append([cur_query.number,cur_query.name])

        elif cur_query.type == 'del':
            if p_hash in contacts:
                for i in range(len(contacts[p_hash])):
                    x = contacts[p_hash]
                    if contacts[p_hash][i][0] == cur_query.number:
                        contacts[p_hash].pop(i)
                        break

        elif cur_query.type == 'find':
            if p_hash not in contacts or len(contacts[p_hash])==0:
                result.append('not found')
            else:
                for contact in contacts[p_hash]:
                    if contact[0] == cur_query.number:
                        result.append(contact[1])
                        break
                    elif contact == contacts[p_hash][-1]:
                        result.append('not found')

    return result

    ''''''

def process_queries_naive(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = [None]*10000000

    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            contacts[cur_query.number] = cur_query.name

        elif cur_query.type == 'del':
            if contacts[cur_query.number] != None:
                contacts[cur_query.number] = None
                
        elif cur_query.type == 'find':
            if contacts[cur_query.number] == None:
                result.append("not found")
            else:
                result.append(contacts[cur_query.number])

    return result

if __name__ == '__main__':
    
    trial = 1
    while True:
        queries = []
        added_nums = []
        num_queries = 100000#random.randrange(1,10**5)
        print(num_queries)

        for _ in range(num_queries):
            method = random.choice(["add","del","find"])
            num = random.randrange(1,9999999)

            if method == "add":
                namelen = random.randrange(1,15)
                name = str()
                for _ in range(namelen):
                    name += random.choice(list(string.ascii_lowercase))
                queries.append(Query([method,num,name]))
            
            else:
                ran = random.choices([True,False],[.3,.7])
                if ran == True or len(added_nums)==0:
                    queries.append(Query([method,num]))
                else:
                    num = random.choice(added_nums)
                    queries.append(Query([method,num]))

        hashmeth = process_queries(queries)
        print(f"hash: {time.time()-st}")
        st = time.time()
        naive = process_queries_naive(queries)
        print(f"naive: {time.time()-st}")

        if naive == hashmeth:
            print("SUCCESS",trial)
            trial += 1
        else:
            for i in range(len(naive)):
                if naive[i] != hashmeth[i]:
                    print(f"Naive: {naive[i]} || Hash: {hashmeth[i]}")
                    sys.exit("FAIL")
                    
    
    write_responses(process_queries(read_queries()))

