class Node(object):
    """docstring for Node."""

    def __init__(self, data = None, value = None, code = None):
        self.left = None
        self.right = None
        self.data = data
        self.value = value
        self.code = code

    def getCode(self):
        return self.code

    def getValue(self):
        return self.value

    def getData(self):
        return self.data

    def insert(self, data, value, last = 0):
        if self.data:
            if self.left is None:
                self.left = Node(data, value, self.code + "0")
            else:
                if self.right is None:
                    if not last:
                        self.right = Node("Node", 0, self.code + "1")
                        self.right.insert(data, value, last)
                    else:
                        self.right = Node(data, value, self.code + "1")
                else:
                    self.right.insert(data, value, last)

    def findLetter(self, data, code):
        if self.left.data == data:
            return self.left.code
        elif self.right.data == data:
            code += str(self.right.code)
            return code
        else:
            code += str(self.right.code)
            self.right.findLetter(data, code)
        return code

    # def findLetterCode(self, data):
    #     if self.left:
    #         self.left.PrintTree()
    #     if self.data == data:
    #         print(self.getData(), self.getValue(), self.getCode()),
    #     if self.right:
    #         self.right.PrintTree()

    def findLetterCode(self, data):
        global findCode
        if self.left:
            self.left.findLetterCode(data)
        if self.data == data:
            findCode = self.getCode()
        if self.right:
            self.right.findLetterCode(data)

    def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print(self.getData(), self.getValue(), self.getCode()),
      if self.right:
         self.right.PrintTree()

def returnValues(words):
    words = words.replace(" ", "").lower()
    wor_a = list(words)
    w_a = list(set(wor_a))
    val_a = {}
    v_a = []
    for i in w_a:
        v_a.append(1)
        val_a[i] = 0
    for i in wor_a:
        val_a[i] += 1
    for i in range(len(w_a)):
        v_a[i] = val_a[w_a[i]]
    for j in range(len(w_a)):
        for i in range(len(w_a) - 1):
            if val_a[w_a[i]] > val_a[w_a[i+1]]:
                buff = w_a[i]
                w_a[i] = w_a[i + 1]
                v_a[i] = val_a[w_a[i + 1]]
                w_a[i + 1] = buff
                v_a[i + 1] = val_a[buff]
    return v_a, w_a

f = open("input.txt", "r")
words = f.read().lower().replace("\n", "")
f.close()
# Or from keyboard input
# words = input("Input your phrase : \n")

w_a = list(words)
v_a, w_a = returnValues(words)
print(v_a, w_a)

left_nodes = len(w_a)
root = Node("Node", 0, "")
for i in reversed(range(left_nodes)):
    if i != 0:
        root.insert(w_a[i], v_a[i])
    else:
        root.insert(w_a[i], v_a[i], 1)

root.PrintTree()
global findCode
val_a = {}
for i in w_a:
    val_a[i] = 0
for i in w_a:
    root.findLetterCode(i)
    val_a[i] = findCode
print(val_a)

cypheredWord = words
for i in w_a:
    cypheredWord = cypheredWord.replace(i, val_a[i])

f = open("output.txt", "w")
f.write(cypheredWord)
f.close()

rev_val_a = dict((v, k) for k, v in val_a.items())
# for i in rev_val_a:
#     cypheredWord = cypheredWord.replace(i, val_a[i])

f = open("output.txt", "r")
words = f.read().lower()
f.close()

for i in rev_val_a:
    cypheredWord = cypheredWord.replace(i, rev_val_a[i])

f = open("rev_output.txt", "w")
f.write(cypheredWord)
f.close()
