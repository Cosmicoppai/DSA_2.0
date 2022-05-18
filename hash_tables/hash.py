from typing import List, Any


class HashTable:
    def __init__(self, size: int = 1000):
        self.array = [[] for _ in range(size)]
        self.length = 0
        self.size = size

    def add(self, key: Any, value: Any) -> None:
        idx = self.compute_index(key)

        for kvp in self.array[idx]:
            if kvp[0] == key:
                kvp[1] = value
                break
        else:
            self.array[idx].append([key, value])
            self.length += 1

        if self.is_full():
            self.double_up()

    def get(self, key: Any) -> Any:
        idx = self.compute_index(key)
        for kvp in self.array[idx]:
            if kvp[0] == key:
                return kvp[1]

        raise KeyError

    def is_full(self) -> bool:
        return self.length > self.size / 2

    def double_up(self) -> None:
        new_hash_table = HashTable(size=2 * len(self.array))

        for idx in range(self.array):
            if not self.array[idx]:
                continue
            for kvp in self.array[idx]:
                new_hash_table.add(kvp[0], kvp[1])

        self.array = new_hash_table.array

    def keys(self) -> Any:
        return self.__iter__()

    def values(self) -> Any:
        for kvp in self.__iterate_kv():
            return kvp[1]

    def items(self) -> List[Any]:
        return self.__iterate_kv()

    def compute_index(self, key: Any) -> int:
        return hash(key) % self.size

    def __getitem__(self, item) -> Any:
        return self.get(item)

    def __setitem__(self, key, value) -> Any:
        self.add(key, value)

    def __iterate_kv(self) -> List[Any]:
        for sub_lst in self.array:
            if not sub_lst:
                continue
            for kvp in sub_lst:
                yield kvp

    def __iter__(self) -> Any:
        for kvp in self.__iterate_kv():
            yield kvp[0]

    def __contains__(self, item) -> bool:
        try:
            self.get(item)
            return True
        except KeyError:
            return False

    def __eq__(self, other: object) -> bool:
        return self.array == other.array

    def __len__(self):
        return self.length

    def __delitem__(self, key: Any) -> None:
        idx = self.compute_index(key)
        for kvp in self.array[idx]:
            if kvp[0] == key:
                self.array[idx].remove(kvp)
                self.length -= 1
                return

        raise KeyError("Key {} doesn't exist".format(key))

    __hash__ = None


if __name__ == "__main__":
    hash_table = HashTable()
    hash_table.add(1, "cosmicoppai")
    hash_table.add(2, "seo_ye_ji")
    hash_table.add(3, "hana")

    print(len(hash_table))
    print(1 in hash_table)

    for key in hash_table:
        print(key)

    hash_table[4] = "tsubasa"
    print(len(hash_table))
    del hash_table[1]
    print(len(hash_table))
