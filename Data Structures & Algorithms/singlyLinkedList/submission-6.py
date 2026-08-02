class ListNode:
    def __init__(self, val: int, next_node: ListNode = None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        ptr, curr = 0, self.head

        while curr and ptr < index:
            curr = curr.next
            ptr += 1

        if curr:
            return curr.val
        else:
            return -1

    def insertHead(self, val: int) -> None:
        old_head = self.head
        self.head = ListNode(val, old_head)

    def insertTail(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
            return

        curr = self.head

        while curr.next:
            curr = curr.next
        
        curr.next = ListNode(val)

    def remove(self, index: int) -> bool:
        if index == 0:
            if not self.head:
                return False
                
            if not self.head.next:
                self.head = None
            else:
                self.head = self.head.next
            return True

        ptr, curr, prev = 0, self.head, None

        while curr and ptr < index:
            prev = curr
            curr = curr.next
            ptr += 1
        
        if not curr or ptr != index:
            return False
        
        prev.next = curr.next
        return True
        


    def getValues(self) -> List[int]:
        res = []
        curr = self.head

        while curr:
            res.append(curr.val)
            curr = curr.next
        
        return res