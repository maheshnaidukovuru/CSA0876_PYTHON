class ListNode:
    def _init_(self, val=0, next=None):
        self.val = val
        self.next = next
def swapPairs(head):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    while head and head.next:
        first_node = head
        second_node = head.next
        prev.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node
        prev = first_node
        head = first_node.next
    return dummy.next
def list_to_linkedlist(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head
def linkedlist_to_list(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst
head = list_to_linkedlist([1, 2, 3, 4])
swapped_head = swapPairs(head)
print("Output for Test Case 1:", linkedlist_to_list(swapped_head))