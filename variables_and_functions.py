cheese = int(input('How many cheese do you have ==>'))
crackers = int(input('What about crackers ==>'))


def cheese_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_crackers(20, 30)

print("OR, we can use variables from our script:\n")


cheese_crackers(cheese, crackers)

print("And we can combine the two, variables and math:")
cheese_crackers(cheese+100, crackers + 1000)
