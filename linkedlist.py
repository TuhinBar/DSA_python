from itertools import count


class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None:
            print('The list is empty')
            return
        temp= self.head
        lt=''
        while(temp):
            lt += str(temp.data)+'-->'
            temp=temp.next

        print(lt)

    def get_position(self, index):
        current= self.head
        count=0
        while(current):
            if(count == index):
                return current.value
            count +=1
            current=current.next
        assert(False)
        return 0

    def insertAtBegn(self, new_element):
        new_node = Node(new_element,self.head)
        self.head = new_node

    def insertAtEnd(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        
        itr.next= Node(data,None)

    def insertValues(self,dataList):
        self.head=None
        for data in dataList:
            self.insertAtEnd(data)

    def getLength(self):
            count=0
            itr=self.head
            while itr:
                count+=1
                itr=itr.next
            return count

    def removeIndex(self,index):
        if index<0 or index>=self.getLength():
            raise Exception("Invalid index")

        if index==0:
            self.head=self.head.next
            return
        
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr= itr.next
            count+=1
    
    def insertAt(self,index,data):
        if index<0 or index>=self.getLength():
            raise Exception("Invalid index")
        
        if index==0:
            self.insertAtBegn(data)
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node= Node(data,itr.next)
                itr.next=node
            itr=itr.next
            count+=1

if __name__=='__main__':
    list1 = LinkedList()

    list1.insertAtBegn(1)
    list1.insertAtBegn(2)
    list1.insertAtBegn(3)
    list1.insertAtEnd(4)
    list1.printList()
    print(list1.getLength())
    list1.removeIndex(2)
    list1.printList()
    list1.insertAt(2,"Apple")
    list1.printList()
    # list1.insertValues(['Banana','Orange','Mango'])
    # n=3
    # print('element of index 3 is:',list1.get_position(n))