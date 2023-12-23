class CustomIndex:
    def __init__(self):
        pass

    def __index__(self,value):
        # self.value = value
        # The __index__ method should return an integer.
        return value

# Create an instance of CustomIndex
custom_index_obj = CustomIndex()

# Using the object as an index
index_value = int(custom_index_obj.__index__(2))
print("Index Value:", index_value)

# Using the object as an index in a list
my_list = [0, 1, 66, 3, 4]
element = my_list[custom_index_obj.__index__(3)]
print("Element at Index:", element)











# class Iter:
#     def __init__(self,data=None):
#         if data==None:
#             self.data=[1,2,3]
#         self.__next__()
#     def __iter__(self):
#         return self.data.__iter__()
#     def __next__(self):
#         d=self.__iter__()
#         try:
#             while True:
#                 print(d.__next__())
#         except StopIteration:
#             pass
# c=Iter()
#         # try:
#         #     while True:
