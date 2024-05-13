class NationalPark:
    def __init__(self, name):
        self.name = name
        self.trip_list = []

    def trips(self):
        return self.trip_list

    def visitors(self):
        return [trip.visitor for trip in self.trip_list]

    def total_visits(self):
        return len(self.trip_list)

    def best_visitor(self):
        if not self.trip_list:
            return None
        visits_count = {}
        for trip in self.trip_list:
            visitor = trip.visitor
            visits_count[visitor] = visits_count.get(visitor, 0) + 1
        return max(visits_count, key=visits_count.get)
