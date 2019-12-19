from components.entity.VersionEntity import Version

class VersionComponent:

    """ default component version """ 
    def __init__(self, version: str):
        self.ver = Version(version)

    def isGreatherThan(self, vers: Version):
        return (self.ver.major > vers.major) or (self.ver.major == vers.major and self.ver.minor > vers.minor) or (self.ver.major == vers.major and self.ver.minor == vers.minor and self.ver.fix > vers.fix)

    def isEquals(self, vers: Version):
        return self.ver.str == vers.str

    def isLesserThan(self, vers: Version):
        return not self.isGreatherThan(vers)