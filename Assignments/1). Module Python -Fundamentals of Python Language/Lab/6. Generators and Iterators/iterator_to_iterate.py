

class ListIterator:
    def __init__(self, data_list):
        self.data_list = data_list
        self.index = 0

    def __iter__(self):
        return self 
    def __next__(self):
        if self.index < len(self.data_list):
            value = self.data_list[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration 


numbers = [10, 20, 30, 40, 50]
print("\nIterating over the list using custom iterator:")
for num in ListIterator(numbers):
    print(num)
