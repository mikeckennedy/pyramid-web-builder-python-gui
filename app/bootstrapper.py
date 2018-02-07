import subprocess
import os
import sys

import program


def main():
    # print(sys.path)
    # script = os.path.join(os.path.dirname(__file__), 'program.py')
    # print(script)
    # p = subprocess.Popen(['python', script])
    return program.main()


if __name__ == '__main__':
    sys.exit(main())
