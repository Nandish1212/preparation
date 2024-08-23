class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
def find_middle(head):
    if head is None:
        return None
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.value if slow else None
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head
values = [1, 2, 3, 4, 5]
head = create_linked_list(values)
middle_value = find_middle(head)
print("The middle value of the linked list is:", middle_value)
