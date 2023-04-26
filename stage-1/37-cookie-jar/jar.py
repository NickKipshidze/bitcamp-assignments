class Jar:
    def __init__(self, capacity=12):
        self.cookie = "🍪"
        self.cookie_jar = ""
        self.jar_capacity = capacity

        if not capacity >= 0:
            raise ValueError("'capacity' is not a non-negative int")

    def __str__(self):
        return self.cookie_jar

    def deposit(self, n):
        if self.size+n <= self.capacity:
            self.cookie_jar += self.cookie*n
        else:
            raise ValueError("Adding that many cookies would exceed the cookie jar's capacity")

    def withdraw(self, n):
        if self.size-n >= 0:
            self.cookie_jar = self.cookie_jar[:-n]
        else:
            raise ValueError("There aren't that many cookies in the cookie jar")

    @property
    def capacity(self):
        return self.jar_capacity

    @property
    def size(self):
        return len(self.cookie_jar)