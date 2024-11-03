class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

def build_trie(words):
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isWord = True  # Mark the end of the word
    return root   

class Solution:
    def findWords(self, board, words):
        root = build_trie(words)
        found_words = set()

        def dfs(x, y, node, current_word):
            if node.isWord:  # Found a valid word
                found_words.add(current_word)
                node.isWord = False  # Avoid duplicates

            # Bounds checking
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
                return

            char = board[x][y]
            if char not in node.children:
                return  # Early exit if no matching prefix

            # Mark the cell as visited
            board[x][y] = '#'
            next_node = node.children[char]

            # Explore neighbors
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                dfs(x + dx, y + dy, next_node, current_word + char)

            # Unmark the cell as visited
            board[x][y] = char

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, root, "")

        return list(found_words)
