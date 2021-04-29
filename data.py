import pandas


class Data:
    def __init__(self, path):
        df = pandas.read_csv(path)
        self.data = df.to_dict(orient="list")

    def get_all_districts(self):
        return list(set(self.data["denominazione_region"]))

    def set_districts_data(self, districts):
        new_data = {}
        for key in self.data.keys():
            new_data[key] = []
        for idx, dst in enumerate(self.data["denominazione_region"]):
            for key in self.data.keys():
                if dst in districts:
                    new_data[key].append(self.data[key][idx])
        self.data = new_data
