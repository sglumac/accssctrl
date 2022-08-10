from urllib.request import urlretrieve
from os import path
import subprocess


scriptFolder = path.dirname(path.abspath(__file__))
xacmlXsd = path.join(scriptFolder, 'xacml3v17.xsd')
xsdUrl = 'http://docs.oasis-open.org/xacml/3.0/xacml-core-v3-schema-wd-17.xsd'
urlretrieve(xsdUrl, xacmlXsd)
subprocess.run(['generateDS.py', '-o', 'representation.py', xacmlXsd])
