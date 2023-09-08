class GI:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return self.generator()

    def generator(self):
        for it in self.data:
            yield it


my_list = [0, 1, 2, 3, 4, 5]
iterator = GI(my_list)

for i in iterator.__iter__():
    print(i)