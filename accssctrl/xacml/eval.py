from enum import Enum


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


class MatchEval:
    def __init__(self, attribute, ) -> None:
        pass


class PolicyEval:
    pass


class PolicySetEval:
    pass


class RuleEval:
    pass


class ConditionEval:
    def process() -> Condition:
        pass