class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def findElement(self, data):
        element = ""
        if self.data == data:
            return str(self)
        else:
            if data < self.data:
                if self.left:
                    element = str(self.left.findElement(data))
                else:
                    return "None"
            else:
                if self.right:
                    element = str(self.right.findElement(data))
                else:
                    return "None"
        return element


    def findMaxElement(self):
        maxElement = ""
        if self.data:
            if self.right:
                maxElement = self.right.findMaxElement()
            else:
                return str(self.data)
        return int(maxElement)

# Print the tree
    def PrintTree(self, n):
        if self.right:
            self.right.PrintTree(n+1)
        print(" "*n, end="")
        print(self.data)
        if self.left:
            self.left.PrintTree(n+1)




# Use the insert method to add nodes
root = Node(None)

while True:
    print("Wybierz:")
    print("1. Insert element")
    print("2. Find max element")
    print("3. Find element")
    print("4. Print tree")
    print("5. Exit")
    answer = int(input("Answer : "))
    if answer == 1:
        root.insert(int(input("Your element : ")))
    elif answer == 2:
        print("Max element : " + str(root.findMaxElement()))
    elif answer == 3:
        print("Finded node : " + str(root.findElement(int(input("Your element : ")))))
    elif answer == 4:
        root.PrintTree(0)
    else:
        break
