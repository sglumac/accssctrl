from . import representation
from .representation.representation import PolicySetType, RequestType, ResponseType


def pdp(policyXml: PolicySetType, requestXml: RequestType) -> ResponseType:
    '''
    Policy decision point (PDP) = The system entity that evaluates applicable policy and renders an authorization decision
    '''
    policyXml.PolicyCombiningAlgId
    policyXml.PolicySet




