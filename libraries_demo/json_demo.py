import json

class person:
    def __init__(self, name, email):
        self.name = name
        self.email = email


p1 = person("Mike", "mike@gmail.com")
print(json.dumps(p1.__dict__))



