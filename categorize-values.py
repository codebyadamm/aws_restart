myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
for item in myMixedTypeList:
    print("{} is of the data type{}".format(item,type(item)))
    # '{}' allows for filling in parameters through a list and will recall the function until list is finished
    
    