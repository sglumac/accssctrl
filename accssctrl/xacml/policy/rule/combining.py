from enum import Enum


class RuleCombiningAlgorithm(Enum):
    DenyOverrides = "urn:oasis:names:tc:xacml:3.0:rule-combining-algorithm:deny-overrides"
    PermitOverrides = "urn:oasis:names:tc:xacml:3.0:rule-combining-algorithm:permit-overrides"
    FirstApplicable = "urn:oasis:names:tc:xacml:1.0:rule-combining-algorithm:first-applicable"
    OrderedDenyOverrides = "urn:oasis:names:tc:xacml:3.0:rule-combining-algorithm:ordered-deny-overrides"
    OrderedPermitOverrides = "urn:oasis:names:tc:xacml:3.0:rule-combining-algorithm:ordered-permit-overrides"
    DenyUnlessPermit = "urn:oasis:names:tc:xacml:3.0:rule-combining-algorithm:deny-unless-permit"
    PermitUnlessDeny = "urn:oasis:names:tc:xacml:3.0:rule-combining-algorithm:permit-unless-deny"
    DenyOverrides10 = "urn:oasis:names:tc:xacml:1.0:rule-combining-algorithm:deny-overrides"
    PermitOverrides10 = "urn:oasis:names:tc:xacml:1.0:rule-combining-algorithm:permit-overrides"
    OrderedDenyOverrides11 = "urn:oasis:names:tc:xacml:1.1:rule-combining-algorithm:ordered-deny-overrides"
    OrderedPermitOverrides11 = "urn:oasis:names:tc:xacml:1.1:rule-combining-algorithm:ordered-permit-overrides"
