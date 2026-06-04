class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()


        """
        N-ary tree


        anand
        ashwini
        gracelin
        esai
        norwin
        hari
        rithika

        ashwini (endof word = true)
        ashwan
        a nand,  shwini
        n orwin
        an - anand

        while root:
            root.left  new Node()
            root = root.left



        A   ..  G  ...  H
       26
     N S      R       A
    26
   A
   26
 N 
D -> end of word  -> anand
    prefix -> words -> start with A

    TrieNode
        children = {}
        end of wod = True / False

        

        insert
         anand
         root {
            'a': {
                'n': {
                    'a' : {
                        'n': {
                            'd': {
                                'wndof word
                            }
                        }
                        }
                }
            }
         }

         root =
         for each word
            if letter not in root.children
                root.children[letter] = Node
    


        """
        

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True


    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endOfWord   

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True   

        
        