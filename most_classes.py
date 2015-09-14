# Create a function named most_classes that takes a dictionary of teachers and
# returns the teacher with the most classes.
#
# The dictionary will be something like:
# {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Often, it's a good idea to hold onto a max_count variable.
# Update it when you find a teacher with more classes than
# the current count. Better hold onto the teacher name somewhere
# too!
#
# Your code goes below here.
def most_classes(dictionary):
    current_max = 0
    current_max_teacher = ''
    for key in dictionary.keys():
        if current_max < len(dictionary[key]):
            current_max = len(dictionary[key])
            current_max_teacher = key
    return current_max_teacher

no_enties = dict()
one_entry = dict({'Kevin Gann': ['Ruby Foundations']})
equal_entries = dict({'Kevin Gann': ['Ruby Foundations'], 'Wyatt Gann': ['Ruby Foundations']})
dictionary = dict({'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'], 'Kenneth Love': ['Python Basics', 'Python Collections']})

print(most_classes(no_enties))
print(most_classes(one_entry))
print(most_classes(equal_entries))
print(most_classes(dictionary))

# Create a function named num_teachers that takes a dictionary of teachers and returns the number of teachers.
def num_teachers(dictionary):
    return len(dictionary.keys())

print(num_teachers(no_enties))
print(num_teachers(one_entry))
print(num_teachers(equal_entries))
print(num_teachers(dictionary))

# Create a function named stats that takes a dictionary of teachers and returns
# a list of lists in the format [<name>, <number of classes>].
def stats(dictionary):
    list_of_teachers = []
    for key in dictionary.keys():
        teacher = [key, len(dictionary[key])]
        list_of_teachers.append(teacher)
    return list_of_teachers

print(stats(no_enties))
print(stats(one_entry))
print(stats(equal_entries))
print(stats(dictionary))

def courses(dictionary):
    list_of_all_courses = []
    for key in dictionary.keys():
        current_courses = dictionary[key]
        for course in current_courses:
            if course not in list_of_all_courses:
                list_of_all_courses.append(course)
    return list_of_all_courses

print(courses(no_enties))
print(courses(one_entry))
print(courses(equal_entries))
print(courses(dictionary))
