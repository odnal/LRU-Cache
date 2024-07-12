class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRU_Cache:
    def __init__(self, capacity):
        self.capacity = capacity

        # we can use a hashmap to easily keep track of a "chache hit" or "cahce miss"
        self.lru_map = {}

        self.head = ListNode(-1, -1) # sentinel node
        self.tail = ListNode(-1, -1) # sentinel node
        self.head.next = self.tail
        self.tail.prev = self.head

    def put(self, key, value):
        if key in self.lru_map:
            node = self.lru_map[key]
            self.remove(node)

        node = ListNode(key, value)
        self.lru_map[key] = node
        self.add(node)

        if len(self.lru_map) > self.capacity:
            node_to_remove = self.head.next
            self.remove(node_to_remove)
            del self.lru_map[node_to_remove.key]

    def get(self, key):
        if key not in self.lru_map:
            print("error: key not in map")
            return -1
        node = self.lru_map[key]
        # update cache lines
        self.remove(node)
        self.add(node)
        return node.value

    def add(self, node):
        # add node to back of linked list
        cur_node = self.tail.prev
        cur_node.next = node
        node.prev = cur_node
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        prev_node = node.prev
        prev_node.next = node.next
        node.next.prev = prev_node


if __name__ == "__main__":

    cache = LRU_Cache(0x10)

    cache.put("hello", 22)
    print(cache.get("hello"))
    cache.put("world", 23)
    print(cache.get("hello"))
    print(len(cache.lru_map))
