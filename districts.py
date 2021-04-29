from data import Data
from copy import deepcopy

class Districts:
    def __init__(self, dataset):
        self.dataset = dataset

    def filter_districts(self, letters):
        self.dataset.set_districts_data(list(filter(lambda x: x[0] in letters, self.dataset.get_all_districts())))

    def print_details(self, features, statistic_functions):
        for feature in self.dataset.data.keys():
            if feature in features:
                values = self.dataset.data[feature]
                answer = ""
                for func in statistic_functions:
                    answer += ", " + str(func(values))
                print(feature + ": " + answer[2:])

    def determine_day_type(self):
        self.dataset.data["day_type"] = [x > y for x, y in zip(self.dataset.data["resigned_healed"],
                                                               self.dataset.data["new_positives"])]

    def get_districts_class(self):

        self.determine_day_type()
        good_day_threshold = 340
        dist_class = {}
        for district in self.dataset.get_all_districts():
            temp = deepcopy(self.dataset)
            temp.set_districts_data([district])
            dist_class[district] = (not(sum(temp.data["day_type"]) > good_day_threshold))*"not " + "green"
        return dist_class
