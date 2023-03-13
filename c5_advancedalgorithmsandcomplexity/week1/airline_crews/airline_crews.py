# python3
class MaxMatching:

    def read_data(self):
        n, m = map(int, input().split())
        # list of teams to work on each flight
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    def find_matching(self, adj_matrix):

        matches = [-1] * len(adj_matrix[0])

        for flight in range(len(adj_matrix)):
            seen = [False] * len(adj_matrix[0])
            self.bpm(flight,matches,seen,adj_matrix)

        transform = [-1] * len(adj_matrix)
        for i in range(len(matches)):
            if matches[i] != -1:
                transform[matches[i]] = i
        return transform

    def bpm(self,flight,match,seen,adj_matrix):
        for crew in range(len(adj_matrix[0])):
            if adj_matrix[flight][crew] == 1 and seen[crew] == False:
                seen[crew] = True
                if match[crew] == -1 or self.bpm(match[crew],match,seen,adj_matrix):
                    match[crew] = flight
                    return True
        return False


    def solve(self):
        adj_matrix = self.read_data()
        matching = self.find_matching(adj_matrix)
        self.write_response(matching)


if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
