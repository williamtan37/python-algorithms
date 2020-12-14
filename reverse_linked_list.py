# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    '''
    Iterative - not in place.
    T = O(N), S = O(N).
    '''
    def insert_before(self, node, val):
        if node:
            node = ListNode(val, node)
        else:
            node = ListNode(val)
            
        return node
       
    def reverseListIterNotInPlace(self, head: ListNode) -> ListNode:
        result = None
        
        while head:
            result = self.insert_before(result, head.val)
            head = head.next
            
        return result
    
    '''
    Iterative - in place - good version.
    T = O(N), S = O(1). 
    This algo uses 3 pointers at once and is based on the fact that you should keep 
    on going if the front node exists instead of if the current node exists.
    Although this algo has best space and time efficieny, the logic/ implementation is not optimal compared
    to the bottom "better version". So, the code is a bit dirtier and not as robust because 
    it has to check for edge cases and other extra operations. 
    Overall, both algos follow the same idea however one is a bit smarter than the other one.
    '''
    def reverseListIterInPlaceGood(self, curr):
        if not curr or not curr.next:
            return curr
        back = None
        front = curr.next
        
        while front:
            curr.next = back
            back, curr = curr, front
            front = front.next
        curr.next = back
        return curr
 
    '''
    Iterative - in place - best version.
    T = O(N), S = O(1).  
    Although has the time and space complexity as the above good algo,
    this algo is more elegant and simple. Using two main pointers and a temporary pointer
    instead of using 3 pointers all at once results in more robust and clean code.
    This algo is based on checking if the current node exists instead of if the front node exists. 
    Makes more sense logically.
    '''
    def reverseListIterInPlaceBest(self, curr):
        back = None
        
        while curr:
            front = curr.next
            curr.next = back
            back, curr = curr, front
        return back

    '''
    Recursive - not in place.
    T = O(N), S = O(N).
    '''
    def reverseListRecurNotInPlace(self, head):
        if head == None or head.next == None:
            return head
        else:
            back = ListNode(head.val)
            front = self.reverseListRecurNotInPlace(head.next)
            curr = front
            while curr.next != None:
                curr = curr.next
            curr.next = back
            return front

    '''
    Recursive - in place. 
    T = O(N), S = O(N). 
    Need to draw each step before coding to really understand the algorithm.
    '''
    def reverseListRecurInPlace(self, head):
        if not head or not head.next:
            return head
        
        p = self.reverseListRecurInPlace(head.next)
        head.next.next = head
        head.next = None
        return p