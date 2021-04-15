class Node(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.data = None
        self.rank = 0
        
class AutocompleteSystem(object):
    def __init__(self, sentences, times):
        self.root = Node()
        self.keyword = ""
        for i, sentence in enumerate(sentences):
            self.addRecord(sentence, times[i])

    def addRecord(self, sentence, hot):
        p = self.root
        for c in sentence:
            if c not in p.children:
                p.children[c] = Node()
            p = p.children[c]
        p.isEnd = True
        p.data = sentence
        p.rank -= hot
    
    def dfs(self, node):
        ret = []
        if node.isEnd:
            ret.append((node.rank, node.data))
        for child in node.children:
            ret.extend(self.dfs(node.children[child]))
        return ret
        
    def search(self, sentence):
        p = self.root
        for c in sentence:
            if c not in p.children:
                return []
            p = p.children[c]
        return self.dfs(p)
    
    def autoComplete(self, c):
        results = []
        if c != "#":
            self.keyword += c
            results = self.search(self.keyword)
        else:
            self.addRecord(self.keyword, 1)
            self.keyword = ""
        return [item[1] for item in sorted(results)[:3]]

# Driver code
sentences = ["beautiful", "best quotes", "best friend", "best birthday wishes", "instagram", "internet"]
times = [30, 14, 21, 10, 10, 15]
auto = AutocompleteSystem(sentences, times)
print(auto.autoComplete("b"))
print(auto.autoComplete("e"))
print(auto.autoComplete("s"))
print(auto.autoComplete("t"))
print(auto.autoComplete("#"))