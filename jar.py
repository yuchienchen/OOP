class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity

    def __str__(self):
        return f"{n}"

    def deposit(self, n):
        if n + __str__(self) > self.capacity:
            raise ValueError("Exceed capacity")
        self._n = n

    def withdraw(self, n):
        if n > __str__(self):
            raise ValueError("Not enough cookies in the cookie jar")
        self._n = n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = get_jar()
    print(jar)

def get_jar():
    capacity= 12
    return Jar(capacity)




if __name__ == "__main__":
    main()