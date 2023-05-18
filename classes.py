class Habit:
    def __init__(self, name, description, period, times_per_period, creation_date):
        self.name = name
        self.period = period
        self.times_per_period = times_per_period
        self.description = description
        self.creation_date = creation_date

    def __str__(self):
        h_string = "name: {}\n description: {}\n period: {}\n times per period:{} \n creation date:{}".format(
            self.name,
            self.description,
            self.period,
            self.times_per_period,
            self.creation_date,
        )
        return h_string

    def get_name_string(self):
        name_str = self.name
        return name_str
