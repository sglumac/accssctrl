

from difflib import Match
from enum import Enum, auto



class Match(Enum):
    NoMatch = 0
    Match = 1
    Indeterminate = 2

class Condition(Enum):
    False_ = 0
    True_ = 1
    Indeterminate = 2


class Authorization(Enum):
    Permit = 0
    Deny = 1
    Indeterminate = 2
    NotApplicable = 3


class TargetEval:
    def __init__(self, rule):
        pass

    def match_attributes(self, attributes) -> Match:
        pass


class AllOfEval:
    def __init__(self, matchEvals):
        pass


class AnyOfEval:
    def __init__(self, allOfEvals):
        pass
    pass


class Pdp:
    '''
    Policy decision point (PDP) = The system entity that evaluates applicable policy and renders an authorization decision
    '''
    def __init__(self, policy):
        self._policy = {
            'xmlNode': policy,
            'rules': {
                rule.RuleId: {
                    'xmlNode': rule,
                    'target': {
                        None,
                    },
                    'condition': {
                        None,
                    }
                }
                for rule in policy.Rule
            }
        }

    def process_request(self, request) -> Authorization:
        pass

