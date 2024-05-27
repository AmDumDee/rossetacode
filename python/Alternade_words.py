WORDFILE = 'unixdict.txt'
MINLEN = 6

class Trie(object):
    class Node(object):
        
        def __init__(self, char='\0', parent=None):
            self.children = {}
            self.char = char
            self.final = False
            self.parent = parent
            
        def descend(self, char, extend=False):
            
            if not char in self.children:
                if not extend: return None
                self.children[char] = Trie.Node(char,self)
            return self.children[char]
        
    def __init__(self):
        self.root = Trie.Node()
    
    def insert(self, word):
        node = self.root
        for char in word: node = node.descend(char, extend=True)
        node.final = True
        return node
    
    def __contains__(self, word):
    
        node = self.root
        for char in word:
            node = node.descend(char)
            if not node: return False
        return node.final 
    
    def words(self):
        
        nodes = [self.root]
        while nodes:
            node = nodes.pop()
            nodes += node.children.values()
            if node.final:
                word = []
                while node:
                    if node.char != '\0': word.append(node.char)
                    node = node.parent
                yield "".join(reversed(word))
    
    def __iter__(self):
        return self.words()
                

words = Trie()
with open(WORDFILE, "rt") as f:
    for word in f.readlines():
        words.insert(word.strip())

for word in words:
    if len(word) < MINLEN: continue
    even = word[::2]
    odd = word[1::2]
    if even in words and odd in words:
        print(word, even, odd)
