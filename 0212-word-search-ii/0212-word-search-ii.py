class Node(object):
    def __init__(self):
        self.endFlag = False
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        curr_head = self.root

        for char in word:
            if char not in curr_head.children:
                curr_head.children[char] = Node()
            curr_head = curr_head.children[char]

        curr_head.endFlag = True

    def search(self, word: str):
        curr_node = self.root

        for char in word:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        if curr_node.endFlag:
            return True
    
    def start_with(self, prefix: str):
        curr_node = self.root
        for char in prefix:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return True

    
    def delete(self, word):
        def recursive(node, word, i):
            if i == len(word):
                if not node.endFlag:
                    return False
                node.endFlag = False
                return (len(node.children) == 0)
            if word[i] not in node.children:
                return False
            need_delete = recursive(node.children[word[i], word, i+1])

            if need_delete:
                node.children.pop(word[i])
                return (len(node.children) == 0)
            return False
        recursive(self.root, word, 0)

class Solution:
    answer = list()
    dx = list()
    dy = list()
    m = 0
    n = 0
    words = list()
    ct = 0

    def __init__(self):
        self.answer = list()
        self.dx = [1,-1, 0,0]
        self.dy = [0, 0, -1, 1]
        self.ct = 0
        self.m = 0
        self.n = 0
        self.words = list()
        
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        
        self.m = len(board)
        self.n = len(board[0])
        self.words = words
        
        self.trie = {}

        for word in words:
            t = self.trie
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]

            t['#'] = '#'
        
        print(self.trie)
        self.answer = list()
        
        for y in range(self.m):
            for x in range(self.n):
                self.dfs(board, self.trie, y, x, '')

        return self.answer

    
    def dfs(self, board, node, y, x, word):
        if '#' in node:
            del node['#']
            self.answer.append(word)
        
        if (y < 0) or y >= len(board) or x < 0 or x >= len(board[0]):
            return
        
        char = board[y][x]
        if char not in node:
            return
        
        next_node = node[char]
        board[y][x] = '@'
        for i in range(4):
            ny, nx = y + self.dy[i], x + self.dx[i]
            self.dfs(board, next_node, ny, nx, word+char)
        board[y][x] = char
        
        if not next_node:
            del node[char]
        