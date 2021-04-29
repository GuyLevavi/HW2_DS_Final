import sys

from data import Data
from districts import Districts
from statistics import *


def main(argv):

    path = argv[1]
    data1 = Data(path)
    data2 = Data(path)

    # ----------------------Q1----------------------
    print("Question 1: ")
    districts1 = Districts(data1)
    districts1.filter_districts(['L', 'S'])
    districts1.print_details(["hospitalized_with_symptoms", "intensive_care", "total_hospitalized", "home_insulation"],
                             [mean, median])
    # ----------------------Q2----------------------
    print("Question 2: ")
    districts2 = Districts(data2)
    districts2.determine_day_type()

    num_dist = len(data2.get_all_districts())
    not_green = len(list(filter(lambda x: x == "not green", districts2.get_districts_class().values())))
    lockdown_threshold = 10
    is_lockdown = not_green > lockdown_threshold

    print("Number of districts: {}".format(num_dist))
    print("Number of not green districts: {}".format(not_green))
    print("Will a lockdown be forced on whole of Italy?: {}".format("Yes"*is_lockdown + "No"*(not is_lockdown)))


if __name__ == '__main__':
    main(sys.argv)
