import unittest
from os import path
from accssctrl.xacml import Pdp
from accssctrl.xacml.representation import xacml3v17


def example1():
    scriptFolder = path.dirname(path.abspath(__file__))
    return path.join(scriptFolder, 'Example1')


def policy1():
    return path.join(example1(), 'Policy.xml')


def request1():
    return path.join(example1(), 'Request.xml')


def response1():
    return path.join(example1(), 'Response.xml')


class TestXacml(unittest.TestCase):
    def test_rule(self):
        policy = xacml3v17.parse(policy1())
        request = xacml3v17.parse(request1())
        expectedResponse = xacml3v17.parse(response1())
        expectedDecision = expectedResponse.Result[0].Decision.get_valueOf_()
        pdp = Pdp(policy)
        actualResponse = pdp(policy, request)
        actualDecision = actualResponse.Result[0].Decision.get_valueOf_()
        print(policy)
