class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

if __name__ == '__main__':
    a = ListNode(10)
    b = ListNode(20)
    c = ListNode(30)
    d = ListNode(40)
    e = ListNode(50)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    head = a
    while head is not None:
        print(head.val)
        head = head.next
