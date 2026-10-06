class TrieNode:
    def __init__(self):
        self.children={}
        self.word=None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()

        for word in words:
            node=root

            for ch in word:
                if ch not in node.children:
                    node.children[ch]=TrieNode()

                node=node.children[ch]

            node.word=word

        rows = len(board)
        cols = len(board[0])
        result=[]

        def dfs(r, c, node):

            if r < 0 or r>= rows or c<0 or c>=cols:
                return
            ch = board[r][c]

            if ch == "#" or ch not in node.children:
                return

            next_node = node.children[ch]

            if next_node.word is not None:
                result.append(next_node.word)
                next_node.word=None

            board[r][c]="#"

            dfs(r+1, c, next_node)
            dfs(r-1, c, next_node)
            dfs(r, c+1, next_node)
            dfs(r, c-1, next_node)

            board[r][c]=ch

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        return result