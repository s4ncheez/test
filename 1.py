'''
class Node(object):

    def __init__(self, data, left = None, right = None):

        self.left = left
        self.right = right
        self.data = data

    def insert(self, data):
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
            
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data, end=" ")
        if self.right:
            self.right.print_tree()

    def height(self, root):
        if root is None:
            return 0
        else:
            return max(self.height(root.left), self.height(root.right)) + 1

bst = Node(None)
'''
fin = open ("height.in")
fout = open ("height.out", 'w')
n = int(fin.readline())
bst = [1] * n
for j in range (n):
    line = list(map(int, fin.readline().split()))
    if line[1] != 0:
        bst[line[1] - 1] = bst[j] + 1
    if line[2] != 0:
        bst[line[2] - 1] = bst[j] + 1
if n == 0:
    print(0, file = fout)
else:
    print (max(bst), file = fout)
fout.close()