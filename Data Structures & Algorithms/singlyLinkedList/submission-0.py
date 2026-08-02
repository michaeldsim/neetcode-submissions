class LinkedList:
    
    def __init__(self):
        self.arr = []
    
    def get(self, index: int) -> int:
        if index >= len(self.arr):
            return -1
        return self.arr[index]

    def insertHead(self, val: int) -> None:
        self.arr = [val] + self.arr

    def insertTail(self, val: int) -> None:
        self.arr.append(val)

    def remove(self, index: int) -> bool:
        if index < len(self.arr):
            del self.arr[index]
            return True
        else:
            return False

    def getValues(self) -> List[int]:
        return self.arr
