'''
Policy decision point (PDP) = The system entity that evaluates applicable policy and renders an authorization decision
'''
from .pip import Pip
from .representation.xacml3v17 import PolicySetType, RequestType, ResponseType


class Pdp:
    def __init__(self, policyXml: PolicySetType) -> None:
        pass


    def process_request(self, pip: Pip, requestXml: RequestType) -> ResponseType:
        pass
