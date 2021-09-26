class LLNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __hash__(self):
        str(self.value)

    def get_value(self):
        return self.value

    def set_next(self, next_node):
        self.next = next_node
        return self

    def set_prev(self, prev_node):
        self.prev = prev_node
        return self

    def get_list(self):
        if self.next is None:
            return [self.value]
        return [self.value] + self.next.get_list()


def build_linked_list(arr):
    nodes = [LLNode(v) for v in arr]
    for i in range(1, len(nodes)):
        nodes[i].prev = nodes[i-1]

    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]

    return nodes[0]

