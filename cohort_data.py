"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    houses = set()
    cohort_data = open(filename)

    for line in cohort_data:
      
      house = line.rstrip().split("|")[2]

      if house:
        houses.add(house)

    return houses

all_houses("cohort_data.txt")


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.


    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    students = []
    students_data = open(filename)

    for line in students_data:
      students_list = line.rstrip().split("|")
      full_name = students_list[0] + " " + students_list[1]
      students_cohort = students_list[4]
      if cohort != "I" or cohort != "G" or cohort == "All" or students_cohort == cohort:
        students.append(full_name)
    
    return sorted(students)

students_by_cohort("cohort_data.txt", cohort = "Winter 2016")


def all_names_by_house(filename):


    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """
    
    all_names = []
    students_data = open(filename)

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    for line in students_data:
        students_list = line.rstrip().split("|")
        full_name = students_list[0] + " " + students_list[1]
        house = students_list[2]

        if house == "Dumbledore's Army":
          dumbledores_army.append(full_name)
          dumbledores_army_sort = sorted(dumbledores_army)

        elif house == "Gryffindor":
          gryffindor.append(full_name)
          gryffindor_sort = sorted(gryffindor)

        elif house == "Hufflepuff":
          hufflepuff.append(full_name)
          hufflepuff_sort = sorted(hufflepuff)

        elif house == "Ravenclaw":
          ravenclaw.append(full_name)
          ravenclaw_sort = sorted(ravenclaw)

        elif house == "Slytherin":
          slytherin.append(full_name)
          slytherin_sort = sorted(slytherin)

        elif house == "G":
          ghosts.append(full_name)
          ghosts_sort = sorted(ghosts)

        elif house == "I":
          instructors.append(full_name)
          instructors_sort = sorted(instructors)
    
    all_names.append("dumbledores_army_sort" + "gryffindor_sort" + "hufflepuff_sort" + "ravenclaw_sort" + "slytherin_sort" + "ghosts_sort" + "instructors_sort")
        
    return sorted(all_names)

all_names_by_house("cohort_data.txt")


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []
    students_data = open(filename)

    for line in students_data:
      students_list = line.rstrip().split("|")
      all_data.append(students_list)

    return all_data

all_data("cohort_data.txt")


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    students_data = open(filename)

    for line in students_data:
      students_list = line.rstrip().split("|")
      # name = students_list[0] + " " + students_list[1]
      cohort = students_list[4]
    
    return cohort

get_cohort_for("cohort_data.txt", "Harry Potter")


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    students_last_name = set()
    students_data = open(filename)

    for line in students_data:
      students_list = line.rstrip().split("|")
      last_name = students_list[1]
      students_last_name.add(last_name)
    
    return students_last_name

find_duped_last_names("cohort_data.txt")



def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    housemates = set()
    students_data = open(filename)

    for line in students_data:
      students_list = line.rstrip().split("|")
      house = students_list[2]
      full_name = students_list[0] + " " + students_list[1]
      cohort = students_list[4]

      if (full_name, cohort) ==  
    
    return 

get_housemates_for("cohort_data.txt", )







##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
