def remove_duplicates_recur(node, values=None):
    if values is None:
        values = set()

    if node is None:
        return

    if node.value in values:
        if node.next is None:
            node.prev.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    values.add(node.value)
    return remove_duplicates_recur(node.next, values)


def remove_duplicates(node):
    remove_duplicates_recur(node)
    return node
