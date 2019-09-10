class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
        if (head == None):
                head = Node(data)
        else:
            current = head
            while (current.next != None):
                current = current.next
            current.next = Node(data)
        return head

mylist= Solution()
#T=int(input()) 
T = 4
data_list = [2, 3, 4, 1]
head=None
for i in range(T):
    #data=int(input())
    data = data_list[i]
    head=mylist.insert(head,data)    
mylist.display(head); 	  