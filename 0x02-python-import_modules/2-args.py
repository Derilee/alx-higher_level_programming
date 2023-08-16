#!/usr/bin/python3
import sys
def words():
    num_of_arguments = len(sys.argv)[1:]
    for word in num_of_arguments:
        print("{}".format(word))


    if num_of_arguments == 0:
    print("{} arguments.".format(num_of_arguments))
elif num_of_arguments == 1:
    print("{} argument:".format(num_of_arguments))
else:
    print("{} arguments:".format(num_of_arguments))
