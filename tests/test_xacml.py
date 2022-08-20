import unittest
from os import path
from accssctrl.xacml.representation import representation 


def example1():
    scriptFolder = path.dirname(path.abspath(__file__))
    return path.join(scriptFolder, 'Example1')


def policy1():
    return path.join(example1(), 'Policy.xml')

class TestXacml(unittest.TestCase):
    def test_rule(self):
        policy = representation.parse(policy1())
        print(policy)
