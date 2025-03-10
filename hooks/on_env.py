class Filter:
    name = ''
    func = lambda x: x
    def __init__(self, name: str, func=lambda x: x):
        self.name = str
        self.func = func

    def getName(self) -> str:
        return self.name

    def setName(self, name: str):
        self.name = name

    def getFunc(self):
        return self.func

    def setFunc(self, func):
        self.func = func


class FilterList:
    def __init__(self):
        self.lst = []

    def add(self, filter: Filter):
        self.lst.append(Filter)
        return self

    def run(self, env):
        for filter in self.lst:
            env.filters[filter.getName(filter)] = filter.getFunc(filter)


def toBoolean(value: [bool, str, int]) -> bool:
    if isinstance(value, bool):
        return value

    if isinstance(value, str):
        if value == "True" or value == "true":
            return True
        elif value == "false" or value == "False":
            return False
        else:
            raise ValueError(f"could not convert string to bool: '{value}'")

    if isinstance(value, int):
        if value == 0:
            return False
        else:
            return True

    else:
        raise TypeError(f"value must be bool, str or int, but it is: '{value}'")


def on_env(env, config, files, **kwargs):
    filterList  = FilterList()
    filterList.add(Filter("toBoolean", toBoolean))
    filterList.run(env)
    env.filters["toBoolean"] = toBoolean
