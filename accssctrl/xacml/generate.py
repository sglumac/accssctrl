import subprocess
from . import dwnldxsd


def generate():
    xacmlXsd = dwnldxsd.download()
    subprocess.run(['generateDS.py', '-o', 'representation.py', xacmlXsd])


if __name__ == '__main__':
    generate()
