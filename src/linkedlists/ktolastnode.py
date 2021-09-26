def k_to_last_node(node, k):
    runner = node
    for i in range(k):
        if runner.next is None:
            return "ILLEGAL"
        runner = runner.next

    while runner.next is not None:
        runner = runner.next
        node = node.next

    return node
