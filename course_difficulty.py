# have each homework assignment be ranked based on difficulty of the course and on difficulty of the assignment itself
# list_of_courses_and_difficulty only takes into consideration the difficulty of the course, not the assingment

from array import *
# install numpy in terminal with:
    
def set_courses_and_difficulties():
    value_c = input("Please enter the names of all your courses with spaces in between each course name\n")

    def get_courses():
    # sets everything to upper case and removes surrounding whitespace, makes sure there is only one space between course names
        courses = value_c.strip().upper() 
        return courses
    
    format_courses = get_courses()

    value_t = input("\nPlease enter the amount of time (between 1 and 6 hours) that you spend completing work for each class every day.\n",
   "The hours are as following:\n1 = between 1 and 1.7 hours\n2 = between 1.7 and 2.7 hours\n3 = between 2.7 and 3.7 hours\n4 = between 3.7 and 4.7 hours\n",
   "5 = between 4.7 and 6 hours\n\nReminder, your courses are:", format_courses)
  
   def get_timetaken():
       timetaken = value_t.strip()
       return timetaken

    value_d = input('\nPlease enter the difficulty of each course in the same order with spaces in between each ranking.\n' +
    'The levels of difficulty are as following:\n' +
    '1 = Easy and quick\n' + '2 = Easy but time-consuming\n' + '3 = Medium\n' + '4 = Hard material, quick work'
    + f'5 = Hard, tedious, and time-consuming\n\nReminder, your courses are: {format_courses}\n')
    
    def get_difficulties():
        difficulties = value_d.strip() 
        return difficulties 

    def string_to_array(s):
    # defines a method that creates an array of strings, the strings consist of the content in between each spaces
        return s.split(" ") 

    list_courses = string_to_array(get_courses())

     
   list_timetaken = string_to_array(get_timetaken())


    list_difficulties = string_to_array(get_difficulties())

    # MAKE A JOINT LIST HERE 
    
    num_courses = len(list_courses)
    # integer that represents the length of the courses array, isn't used as of now but is here in case you need it later

    print(f'\nYour course list:\n{list_courses}\nTheir corresponding difficulties:\n{list_difficulties}')


def coursecheck():
    #checks that the courses the user entered are in line with what they want 

    check = input("Please check that these are the courses you're taking")
    if check.lower() in ['yes', 'y']:
        print(f'\nYay! You are ready to move on.')
     elif check.lower() in ['no', 'n']:
        set_courses_and_difficulties()
    else: 
        print(f'\nError. Please retry.')
        coursecheck()

coursecheck()

if __name__ == "__main__":
    set_courses_and_difficulties()


# A refined way to obtain the "difficulty of an assignment in a numerical form
    # The course difficulty can weigh heavier and then the assignment diffculty can be added
def get_difficulty_index()
   # Through a joint list (see line 34)
   # Can use the dictionary feature in python to develop the joint list
            
   # make the course difficulty weighed more than the homework efficiency        
    float index = (course difficulty * 2) + homework difficulty
   
    return index
