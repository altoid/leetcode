# for common linked list operations used in the problems.

# their definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_linked_list(l):
    prev = None
    for x in reversed(l):
        n = ListNode(x, prev)
        prev = n
    return prev


def ll_to_string(ll):
    return str(ll_to_list(ll))


def ll_to_list(ll):
    real = []
    n = ll
    while n:
        real.append(n.val)
        n = n.next

    return real


def head(ll):
    return ll


def tail(ll):
    p = ll
    while p.next:
        p = p.next
    return p


def reverse(ll):
    """
    reverse the linked list in-place; this modifies the list by changing all the pointers.
    """

    p0 = None
    p1 = ll
    p2 = ll.next if ll else None

    while p2:
        p1.next = p0
        p0 = p1
        p1 = p2
        p2 = p2.next
    if p1:
        p1.next = p0
    return p1
