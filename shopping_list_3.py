shopping_list = []

def show_help():
    print("Separate each item with a comma.")
    print("Type DONE to quit, SHOW to see the current list, and HELP.")

def show_list():
    count = 1
    for item in shopping_list:
        print("{}: {}".format(count, item))
        count += 1

print("Give me a list of things.")
show_help()

while True:
    new_stuff = input("> ")

    if new_stuff == "DONE":
        print("Here's your list:")
        show_list()
        break
    elif new_stuff == "HELP":
        show_help()
        continue
    elif new_stuff == "SHOW":
        show_list()
        continue
    else:
        new_list = new_stuff.split(",")
        index = input("Add to a certain spot? Press enter for the end of the list. Or, give me a number. Current {} items in the list. ".format(len(shopping_list)))
        if index:
            spot = int(index) - 1
            for item in new_list:
                shopping_list.insert(spot, item.strip())
                spot += 1
        else:
            for item in new_list:
                shopping_list.append(item.strip())
        continue
