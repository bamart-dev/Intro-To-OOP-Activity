# add your Student class here!


class Student:
    def __init__(self, name, year,class_list):
        self.name = name
        self.year = year
        self.class_list = class_list

    def add_class(self, class_name):
        self.class_list.append(class_name)

    def get_num_classes(self):
        return len(self.class_list)

    def summary(self):
        print(f"{self.name} is a {self.year} enrolled in {self.get_num_classes()} classes")
