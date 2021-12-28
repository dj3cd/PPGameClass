import shelve

class Save:
    def __init__(self):
        self.file = shelve.open("Data")


    def save(self):
        self.file["Number"] = 0

    def add(self, name, value):
        self.file[name] = value

    def get(self, name):
        return self.file[name]



    def __del__(self):
        self.file.close()

