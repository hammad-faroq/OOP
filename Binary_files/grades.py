class Grades:
    def __init__ (self,course,roll_no,percentage_marks):
        self.course=course.ljust(21)
        self.roll_no=roll_no
        self.percentage_marks=percentage_marks
import pickle

# Sample data
data = {"name": "John", "age": 30, "city": "New York"}

# Serialization using pickle.dump()
with open('serialized_data.pickle', 'wb') as file:
    pickle.dump(data, file)

# Deserialization using pickle.load()
with open('serialized_data.pickle', 'rb') as file:
    loaded_data = pickle.load(file)

# Display the original and loaded data
print("Original Data:", data)
print("Loaded Data:", loaded_data)
