class Construct(object):
    def __init__(self, name, value):
        self.Name = name
        self.Value = value
        self.Type = None

    def get_construct(self):
        return self.Name, self.Type, self.Value

class Cstring(Construct):
    def __init__(self, name, value):
        super(name, value)
        self.Type = "String"

class Cnum(Construct):
    def __init__(self, name, value):
        super(name, value)
        self.Type = "Number"

class Cbool(Construct):
    def __init__(self, name, value):
        super(name, value)
        self.Type = "Boolean"