from enum import Enum, auto
from functools import reduce
import math
from typing import Dict
from accssctrl.xacml.representation.xacml3v17 import PolicySetType, RequestType, ResponseType
from . import representation, match


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


class TargetValue(Enum):
    Match = auto()
    Indeterminate = auto()
    NoMatch = auto()


class ConditionValue(Enum):
    True_ = auto()
    False_ = auto()
    Indeterminate = auto()


def all_of_aggregate(prevAllOf: TargetValue, nextMatch: match.MatchValue):
    if prevAllOf == TargetValue.Match:
        if nextMatch == match.MatchValue.True_:
            return TargetValue.Match
        elif nextMatch == match.MatchValue.False_:
            return TargetValue.NoMatch
        elif nextMatch == match.MatchValue.Indeterminate:
            return TargetValue.Indeterminate
    elif prevAllOf == TargetValue.Indeterminate:
        if nextMatch == match.MatchValue.False_:
            return TargetValue.NoMatch
        else:
            return TargetValue.Indeterminate
    else:
        return TargetValue.NoMatch


def any_of_aggregate(prevAnyOf: TargetValue, nextAllOf: TargetValue):
    if nextAllOf == TargetValue.Match:
        return TargetValue.Match
    elif prevAnyOf != TargetValue.Match and nextAllOf == TargetValue.Indeterminate:
        return TargetValue.Indeterminate
    elif prevAnyOf == TargetValue.NoMatch and nextAllOf == TargetValue.NoMatch:
        return TargetValue.NoMatch


def target_aggregate(prevTarget: TargetValue, nextAnyOf: TargetValue):
    if prevTarget == TargetValue.Match:
        if nextAnyOf == TargetValue.Match:
            return TargetValue.Match
        elif nextAnyOf == TargetValue.NoMatch:
            return TargetValue.NoMatch
        elif nextAnyOf == TargetValue.Indeterminate:
            return TargetValue.Indeterminate
    elif prevTarget == TargetValue.Indeterminate:
        if nextAnyOf == TargetValue.NoMatch:
            return TargetValue.NoMatch
        else:
            return TargetValue.Indeterminate
    else:
        return TargetValue.NoMatch


def find_decision(policyXml: PolicySetType, attributes: Dict) -> ResponseType:
    for ruleXml in policyXml.Rule:
        targetResult = TargetValue.Match
        for anyOfXml in ruleXml.Target.AnyOf:
            anyOfResult = TargetValue.NoMatch
            for allOfXml in anyOfXml.AllOf:
                allOfResult = reduce(all_of_aggregate, (match.check(matchXml, attributes) for matchXml in allOfXml.Match),  TargetValue.Match)
                anyOfResult = any_of_aggregate(anyOfResult, allOfResult)
            targetResult = target_aggregate(targetResult, anyOfResult)
        conditionResult = ConditionValue.True_
        ruleResult = targetResult if conditionResult == ConditionValue.True_ else None
        break
    return ruleResult
