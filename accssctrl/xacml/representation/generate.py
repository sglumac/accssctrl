import subprocess
from os import path
from urllib.request import urlretrieve


def dwnldxsd():
    scriptFolder = path.dirname(path.abspath(__file__))
    xsdUrl = 'http://docs.oasis-open.org/xacml/3.0/xacml-core-v3-schema-wd-17.xsd'
    xacmlXsd = path.join(scriptFolder, 'xacml3v17.xsd')
    urlretrieve(xsdUrl, xacmlXsd)
    return xacmlXsd


def generate():
    xacmlXsd = dwnldxsd()
    subprocess.run(['generateDS.py', '-o', 'xacml3v17.py', xacmlXsd])


if __name__ == '__main__':
    generate()
