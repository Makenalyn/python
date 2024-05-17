#!/usr/bin/python3

""" script to count the number of instances """

class Count():

    __no_of_instances = 0

    def __init__(self):
        Count.__no_of_instances += 1
        self.count = Count.__no_of_instances


"""
inherits from the class count
"""
class how_many(Count):
    pass


for i in range(10):
    total_instances = how_many()


print(total_instances.count)
