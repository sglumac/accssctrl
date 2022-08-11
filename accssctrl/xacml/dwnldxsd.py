from urllib.request import urlretrieve
from os import path


def download():
    scriptFolder = path.dirname(path.abspath(__file__))
    xsdUrl = 'http://docs.oasis-open.org/xacml/3.0/xacml-core-v3-schema-wd-17.xsd'
    xacmlXsd = path.join(scriptFolder, 'xacml3v17.xsd')
    urlretrieve(xsdUrl, xacmlXsd)
    return xacmlXsd
