# LC00707_Design_Linked_List.py

# Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val is the 
# value of the current node, and next is a pointer/reference to the next node.
# If you want to use the doubly linked list, you will need one more attribute prev to 
# indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

# Implement the MyLinkedList class:

# MyLinkedList() Initializes the MyLinkedList object.
# int get(int index) Get the value of the indexth node in the linked list. If the index 
# is invalid, return -1.
# void addAtHead(int val) Add a node of value val before the first element of the linked list. 
# After the insertion, the new node will be the first node of the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the linked list.
# void addAtIndex(int index, int val) Add a node of value val before the indexth node in the 
# linked list. If index equals the length of the linked list, the node will be appended to 
# the end of the linked list. If index is greater than the length, the node will not be inserted.
# void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

# Example 1:

# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]

# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3
 

# Constraints:

# 0 <= index, val <= 1000
# Please do not use the built-in LinkedList library.
# At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class MyLinkedList:

    def __init__(self):
        self.startNode=None
        self.size=0

    def get(self, index: int) -> int:
        if index>=0 and index<self.size:
            node=self.startNode
            for i in range(index):
                node=node.next
            return node.val
        else:
            return -1
        

    def addAtHead(self, val: int) -> None:
        newNode=Node(val)
        newNode.next=self.startNode
        self.startNode=newNode
        self.size+=1
        return self.startNode

        

    def addAtTail(self, val: int) -> None:
        newNode=Node(val)
        if self.size==0:
            self.startNode=newNode
        else:
            node=self.startNode
            while node.next is not None:
                node=node.next
            node.next=newNode
        self.size+=1
        return self.startNode
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index>=0 and index<=self.size:
            newNode=Node(val)
            if index==0:
                newNode.next=self.startNode
                self.startNode=newNode 
            else:
                node=self.startNode
                for i in range(index-1):
                    node=node.next
                prev_nodes_next=node.next
                node.next=newNode
                newNode.next=prev_nodes_next
            self.size+=1
            return self.startNode
        
    def deleteAtIndex(self, index: int) -> None:
        if index>=0 and index<self.size:
            if index==0:
                original_node=self.startNode
                self.startNode=self.startNode.next
                #delete original_node
            else:
                node=self.startNode
                for i in range(index-1):
                    node=node.next
                prev_nodes_next=node.next

                if prev_nodes_next is not None:
                    node.next=prev_nodes_next.next
                    #delete prev_nodes_next

            self.size-=1
            return self.startNode



        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


