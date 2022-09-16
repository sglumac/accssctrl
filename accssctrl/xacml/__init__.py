from typing import Dict
from accssctrl.xacml.representation.xacml3v17 import PolicySetType, RequestType, ResponseType
from . import representation


def process_request(requestXml: RequestType) -> Dict:
    request = {
        'returnPolicyIdList': requestXml.ReturnPolicyIdList,
        'attributes': dict()
    }
    requestAttributes = request['attributes']
    for attributesXml in requestXml.Attributes:
        categoryXml = attributesXml.Category
        if categoryXml not in requestAttributes:
            requestAttributes[categoryXml] = dict()
        categoryAttributes = requestAttributes[categoryXml]
        for attributeXml in attributesXml.Attribute:
            attributeValueXml = attributeXml.AttributeValue[0]
            categoryAttributes[attributeXml.AttributeId] = {
                'includeInResult': attributeXml.IncludeInResult,
                'dataType': attributeValueXml.DataType,
                'value': attributeValueXml.get_valueOf_()
            }

    return request

def find_decision(policyXml: PolicySetType, attributes: Dict) -> ResponseType:
    pass
