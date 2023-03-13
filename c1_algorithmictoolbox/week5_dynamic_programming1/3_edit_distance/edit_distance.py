def edit_distance(first_string, second_string):
    D = dict()
    # Assign strings to their respective initial positions
    D.update({(0,0):0})
    for i in range(1,len(first_string)+1):
        D.update({(i,0):i})
    for j in range(1,len(second_string)+1):
        D.update({(0,j):j})

    for i in range(1,len(first_string)+1):
        for j in range(1,len(second_string)+1):
            insert = D[i,j-1] + 1
            delete = D[i-1,j] + 1
            match = D[i-1,j-1]
            mismatch = D[i-1,j-1] + 1
            if first_string[i-1] == second_string[j-1]:
                D.update({(i,j):min(insert,delete,match)})
            else:
                D.update({(i,j):min(insert,delete,mismatch)})
    return D[(len(first_string),len(second_string))]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
