# Input: dictionary[] = {"GEEKS", "FOR", "QUIZ", "GO"};
#       boggle[][]   = {{'G','I','Z'},
#                       {'U','E','K'},
#                       {'Q','S','E'}};
#      isWord(dictionary, boggle, str): returns true if str is present in dictionary else false.
#
#
#Output:  Following words of dictionary are present
#         GEEKS
#         QUIZ



"""

S = string, N - chars,
M - strings

Tree:
insert O(N)
lookup O(long M)
O(M)

Hash:
insert O(1)
lookup O(1)

canMove(position, ch)

"""

class Solver(object):

    def __init__(self, dict_list, boggle):
        self.dict = set(dict_list)
        self.boggle = boggle
        self.adj = {}
        self.pos = {}
        for i in xrange(len(boggle)):
            for j in xrange(len(boggle[i])):
                ch = boggle[i][j]
                self.adj[(i, j)] = set(self.get_adj(boggle, i, j))
                if ch not in self.pos:
                    self.pos[ch] = [(i, j)]
                else:
                    self.pos[ch].append((i, j))

    def insert_if_exist(self, boggle, i, j, to_array):
        if i >= 0 and i < len(boggle) and j >= 0 and j < len(boggle[i]):
            to_array.append((i, j))

    def get_adj(self, boggle, i, j):
        adj = []
        self.insert_if_exist(boggle, i - 1, j - 1, adj)
        self.insert_if_exist(boggle, i - 1, j, adj)
        self.insert_if_exist(boggle, i - 1, j + 1, adj)
        self.insert_if_exist(boggle, i, j - 1, adj)
        self.insert_if_exist(boggle, i, j + 1, adj)
        self.insert_if_exist(boggle, i + 1, j - 1, adj)
        self.insert_if_exist(boggle, i + 1, j, adj)
        self.insert_if_exist(boggle, i + 1, j + 1, adj)
        return adj

    def is_word(self, string):
        if len(string) == 0:
            return False
        if string not in self.dict:
            return False
        if string[0] not in self.pos:
            return False
        start_positions = self.pos[string[0]]
        for s_position in start_positions:
            if self.__is_word(s_position, 0, string):
                return True
        return False

    def __is_word(self, pos, i, string):
        if i == len(string) - 1:
            return True
        # adjs = self.adj[pos]
        # x0, y0 = pos
        for x, y in self.get_adj(self.boggle, pos[0], pos[1]): #adjs:
            if self.boggle[x][y] == string[i + 1]:
                result = self.__is_word((x, y), i + 1, string)
                if result:
                    return True
        return False


if __name__ == "__main__":

    d = ["GEEKS", "FOR", "QUIZ", "GO"]
    b = [
            ['G','I','Z'],
            ['U','E','K'],
            ['Q','S','E'],
        ]

    s = Solver(d, b)

    print s.is_word("GEEKS")
    print s.is_word("SEEKS")
    print s.is_word("FOR")
    print s.is_word("GEEK")
    print s.is_word("QUIZ")

# Another solution: http://www.geeksforgeeks.org/boggle-find-possible-words-board-characters/
