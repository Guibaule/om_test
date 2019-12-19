from components.version import VersionComponent
from components.entity.VersionEntity import Version

"""
    Question:
    The goal of this question is to write a software library that accepts 2 version string as input and
    returns whether one is greater than, equal, or less than the other. As an example: “1.2” is
    greater than “1.1”. Please provide all test cases you could think of.
"""

defaultVersion = VersionComponent("1.2")

print("Compare if 1.2 > 1.1")
assert defaultVersion.isGreatherThan(Version("1.1"))

print("Compare if 1.2 == another instance of 1.2")
assert defaultVersion.isEquals(Version("1.2"))

print("Compare if 1.2 < 2.1")
assert defaultVersion.isLesserThan(Version("2.1"))

print("Compare if 1.2 != 1.2.10 (three numbers test)")
assert not defaultVersion.isEquals(Version("1.2.10"))

print("Compare if 1.2 != 1.2.1 (three numbers test)")
assert not defaultVersion.isEquals(Version("1.2.1"))

print("Compare if 1.2 != 1.10 (checking if 10 > 2. In string terms its false)")
assert not defaultVersion.isEquals(Version("1.10"))