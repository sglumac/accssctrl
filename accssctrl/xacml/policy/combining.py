from enum import Enum


class PolicyCombiningAlgorithm(Enum):
    DenyOverrides = "urn:oasis:names:tc:xacml:3.0:policy-combining-algorithm:deny-overrides"
    PermitOverrided = "urn:oasis:names:tc:xacml:3.0:policy-combining-algorithm:permit-overrides"
    FirstApplicable = "urn:oasis:names:tc:xacml:1.0:policy-combining-algorithm:first-applicable"
    OnlyOneApplicable = "urn:oasis:names:tc:xacml:1.0:policy-combining-algorithm:only-one-applicable"
    OrderedDenyOverrides = "urn:oasis:names:tc:xacml:3.0:policy-combining-algorithm:ordered-deny-overrides"
    OrderedPermitOverrides = "urn:oasis:names:tc:xacml:3.0:policy-combining-algorithm:ordered-permit-overrides"
    DenyUnlessPermit = "urn:oasis:names:tc:xacml:3.0:policy-combining-algorithm:deny-unless-permit"
    PermitUnlessDeny = "urn:oasis:names:tc:xacml:3.0:policy-combining-algorithm:permit-unless-deny"
    DenyOverrides10 = "urn:oasis:names:tc:xacml:1.0:policy-combining-algorithm:deny-overrides"
    PermitOverrides = "urn:oasis:names:tc:xacml:1.0:policy-combining-algorithm:permit-overrides"
    OrderedDenyOverrides11 = "urn:oasis:names:tc:xacml:1.1:policy-combining-algorithm:ordered-deny-overrides"
    OrderedPermitOverrides11 = "urn:oasis:names:tc:xacml:1.1:policy-combining-algorithm:ordered-permit-overrides"
