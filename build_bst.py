
#insert into BST using insert function 
#check if value exists using contains function
#remove value using remove function



# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.

#all functions Time and Space : average O(log(n)) mand worst O(n)

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
		
		#if new value is less than current node, has to be inserted to the left of this node
        if value < self.value:
			#print(self.value)
			#if left node is None, the new value will be this node
            if self.left is None:
                self.left = BST(value)
            else:
			#if left node is not None, insert into this considering Left Node as parent node
                self.left.insert(value)
		#insert value is greater than current node, insert to the right
        else :
            if self.right is None:
                self.right = BST(None)
            else:
                self.right.insert(value)
        return self

    def contains(self, value):
        # Write your code here.
        if value<self.value:
            if self.left is None:
                return False
            else :
                return self.left.contains(value)
        elif value>self.value:
            if self.right is None:
                return False
            else :
                return self.right.contains(value)
        else:
            return True


    def remove(self, value,parent=None):
        # Write your code here.
        # Do not edit the return statement of this method.
        if value<self.value:
            if self.left is not None:
                self.left.remove(value,self)
        elif value>self.value:
            if self.right is not None:
                self.right.remove(value,self)
		#current node needs to be removed
        else:
			#both child nodes are not empty
            if self.left is not None and self.right is not None:
                self.value = self.right.getMinValue()
                self.right.remove(self.value,self)
            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
					#tree had only one node 
                    pass
            elif parent.left ==self:
                parent.left = self.left if self.left is not None else self.right
            elif parent.right ==self :
                parent.right = self.left if self.left is not None else self.right
        return self

    def getMinValue(self):
        if self.left is None:   
            return self.value
        else:
            return self.left.getMinValue()




if __name__ == "__main__":
    BST = BST
    print("test case")
    print("____________________________________")
    root = BST(10)
    print("insert 10")
    root.left = BST(5)
    print("insert 5")
    root.left.left = BST(2)
    print("insert 2")
    root.left.left.left = BST(1)
    print("insert 1")
    root.left.right = BST(5)
    print("insert 5")
    root.right = BST(15)
    print("insert 15")
    root.right.left = BST(13)
    print("insert 13")
    root.right.left.right = BST(14)
    print("insert 14")
    root.right.right = BST(22)
    print("insert 22")

    root.insert(12)
    print("insert 12")
    

    root.remove(10)
    print("remove 10")

    print("Check if tree has 12")
    ans = root.contains(12)
    print(ans)

    print("Check if tree has 10")
    ans = root.contains(10)
    print(ans)
    

