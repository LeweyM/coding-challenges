def partition(node, value):
    left = node
    right = node
    while right.next is not None:
        right = right.next

    while left.prev is not right:  # when left has passed right
        if left.value < value:
            left = left.next
        elif right.value > value:
            right = right.prev
        else:
            left.value, right.value = right.value, left.value

    return node

