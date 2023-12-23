class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        else:
            self._capacity = capacity
        self.cookies = 0

    def __str__(self):
        return f'{"🍪"*self.cookies}'

    def deposit(self, n):
        if self.cookies + n > self._capacity:
            raise ValueError
        else:
            self.cookies += n

    def withdraw(self, n):
        if n > self.cookies:
            raise ValueError
        else:
            self.cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies