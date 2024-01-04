class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size
        self.condition = 'New'

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        print("Your shoe is as good as new!")

    def cobble_makes_new(self):
        self.condition = 'New'
        print("The shoe has been repaired, and its condition is now 'New'.")
