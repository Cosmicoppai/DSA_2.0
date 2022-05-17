from typing import List, Any


class HashTable:
    def __init__(self, size: int = 1000):
        self.array = [None] * size

    def add(self, key: Any, value: Any) -> None:
        index = self.compute_index(key)

        if self.array[index]:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    kvp[1] = value
                    break
            self.array[index].append((key, value))
        else:
            self.array[index] = [(key, value)]

        if self.is_full():
            self.double_up()

    def get(self, key: Any) -> Any:
        index = self.compute_index(key)
        if not self.array[index]:
            raise KeyError
        for kvp in self.array[index]:
            if kvp[0] == key:
                return kvp[1]

        raise KeyError

    def is_full(self) -> bool:
        none_items = self.array.count(None)
        return len(self.array) - none_items > len(self.array) / 2

    def double_up(self) -> None:
        new_hash_table = HashTable(size=2 * len(self.array))

        for idx in range(self.array):
            if not self.array[idx]:
                continue
            for kvp in self.array[idx]:
                new_hash_table.add(kvp[0], kvp[1])

        self.array = new_hash_table.array

    def __getitem__(self, item) -> Any:
        return self.get(item)

    def __setitem__(self, key, value) -> Any:
        self.add(key, value)

    def __contains__(self, item) -> bool:
        try:
            self.get(item)
            return True
        except KeyError:
            return False

    def __eq__(self, other: HashTable) -> bool:
        return self.array == other.array

    __hash__ = None
