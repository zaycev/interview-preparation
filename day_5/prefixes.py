import sys



class Trie(object):

    class Node(object):

        def __init__(self, **kwargs):
            self.children = {}
            self.attr = kwargs

    def __init__(self, words=[]):
        self.root = self.Node()
        self.root.attr["overlap"] = True
        for w in words:
            self.add_word(w)

    def add_word(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = self.Node(overlap=False)
            else:
                node.children[ch].attr["overlap"] = True
            node = node.children[ch]

    def prefixes(self):
        prefixes = []
        self.__dfs_util(self.root, [], prefixes)
        return prefixes

    def __dfs_util(self, node, prefix, prefixes):
        if node.attr["overlap"] == False:
            prefixes.append("".join(prefix))
            return
        for char, child_node in node.children.iteritems():
            prefix.append(char)
            self.__dfs_util(child_node, prefix, prefixes)
            prefix.pop(len(prefix) - 1)


def test():
    trie = Trie(["zebra", "dog", "duck", "dove", "hello", "hallo"])
    print trie.prefixes()
    return 0


if __name__ == "__main__":
    sys.exit(test())
