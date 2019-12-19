import re

class Version:

    """ groups that matches: 1, 2, 4 """ 
    def __init__(self, version: str):
        regexPattern = r'^(\d+)[,\.](\d+)([,\.](\d+))?'
        matches = re.search(regexPattern, version)

        if(not matches):
            raise Exception("Version doesnt matches with pattern: {}".format(regexPattern))

        self.major = int(matches.group(1))
        self.minor = int(matches.group(2))
        self.fix = 0 if matches.group(4) is None else int(matches.group(4))
        self.str = version
