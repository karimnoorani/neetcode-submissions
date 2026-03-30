# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(node, list1, list2):
            if not list1 and not list2:
                return
            
            if not list1 or not list2:
                node.next = list2 if not list1 else list1
                return
            
            if list1.val < list2.val:
                node.next = list1
                mergeTwoLists(node.next, list1.next, list2)
            else:
                node.next = list2
                mergeTwoLists(node.next, list1, list2.next)
        
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            while len(lists) > 1:
                dummy = ListNode()
                mergeTwoLists(dummy, lists.pop(), lists.pop())
                mergedLists.append(dummy.next)
            if len(lists) == 1:
                mergedLists.append(lists[0])
            lists = mergedLists
        
        return lists[0]
            
