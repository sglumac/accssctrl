from typing import Dict
from .representation.xacml3v17 import MatchType

from enum import Enum, auto


class MatchValue(Enum):
    True_ = auto()
    False_ = auto()
    Indeterminate = auto()


def check(matchXml: MatchType, attributes: Dict) -> MatchValue:
    matchFcns = {
        'urn:oasis:names:tc:xacml:1.0:function:rfc822Name-match': _rfc822_match
    }
    attributeValue = matchXml.AttributeValue.get_valueOf_()
    designator = matchXml.AttributeDesignator
    attribute = attributes[designator.Category][designator.AttributeId]
    return matchFcns[matchXml.MatchId](attribute['value'], attributeValue)


def _rfc822_match(name, pattern):
    return MatchValue.True_ if name.endswith(pattern) else MatchValue.False_
