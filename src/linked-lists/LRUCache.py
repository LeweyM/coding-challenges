class Node:
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

    def set_prev(self, prev_node):
        self.prev = prev_node


class LList:
    def __init__(self):
        self.left = None
        self.right = None
        self.size = 0

    def add_left(self, value):
        node = Node(value)
        if self.left is None and self.right is None:
            self.left = node
            self.right = node
        else:
            node.set_next(self.left)
            self.left.set_prev(node)
            self.left = node
        self.size += 1
        return node

    def pop_right(self):
        if self.size < 1:
            return None
        right = self.right
        self.remove(self.right)
        return right

    def add_right(self, value):
        node = Node(value)
        if self.left is None and self.right is None:
            self.left = node
            self.right = node
        else:
            node.set_prev(self.right)
            self.right.set_next(node)
            self.right = node
        self.size += 1
        return node

    def remove(self, node):
        node_after = node.next
        node_before = node.prev
        if node_after is not None:
            node_after.set_prev(node_before)
        if node_before is not None:
            node_before.set_next(node_after)
        if node is self.left:
            self.left = node_after
        if node is self.right:
            self.right = node_before

        self.size -= 1


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.nodes = {}
        self.linked_list = LList()
        return

    def set(self, key: int, value: int):
        if key not in self.nodes:
            if self.linked_list.size < self.cap:
                node = self.linked_list.add_left((key, value))
                self.nodes[key] = node
            else:
                last_used_node = self.linked_list.pop_right()
                popped_key, _ = last_used_node.get_value()
                self.nodes.pop(popped_key)
                node = self.linked_list.add_left((key, value))
                self.nodes[key] = node
        else:
            node = self.nodes[key]
            # reset order with new value
            self.linked_list.remove(node)
            self.linked_list.add_left((key, value))

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        else:
            node = self.nodes[key]
            k, v = node.get_value()
            self.linked_list.remove(node)
            new_node = self.linked_list.add_left((k, v))
            self.nodes[key] = new_node
            return v
