
class Process:
    def __init__(self, histogram):
        self.words = []
        self.number = []
        self.doc_name = ""
        for value, key in histogram:
            self.words.append(key)
            self.number.append(value)

    def get_doc_name(self, name):
        self.doc_name = name
