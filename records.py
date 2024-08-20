class Records:
    def __init__(self):
        self.exercise = ""
        self.reps = 0
        self.caloriesPerRep = 0

    def __init__(self, exercise, reps, caloriesPerRep):
        self.exercise = exercise
        self.reps = reps
        self.caloriesPerRep = caloriesPerRep
        
        @property
        def caloriesBurned(self):
            return reps * caloriesPerRep