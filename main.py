import json
from dataclasses import asdict, dataclass

@dataclass
class Crispen(object):
    languages   : tuple = ("Python", "JS", "TS", "C++", "Java", "C")
    databases   : tuple = ("MySQL", "MongoDB", "Firebase")
    ongoing     : tuple = ("Pytorch", "NLTK", "Tensorflow", "NLP")
    def me(self):
        return json.dumps(asdict(self), indent=2)
    def printMe(self):
        print(self.me())
    pass

crispen = Crispen()
crispen.printMe()

