'''
biggest takeaway:
    1) snapping windows: right ptr never moves back, only left ptr can move front
    2) for the code snippet of "add 1 to dictionary if it exist, else set it to 1" can be rewritten in a singe line:

            dict1[key] = dict1.get(key, 0) + 1

       (second parameter of get sets the default value of key if it doesn't exist)
    3) for snapping windows, instead of setting both l and r ptr and using while loop, use:
       l = 0
       for r in range(len(parameter)):
'''