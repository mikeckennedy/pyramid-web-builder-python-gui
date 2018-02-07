import subprocess
import os
import sys


def main():
    print(sys.path)
    script = os.path.join(os.path.dirname(__file__), 'program.py')
    p = subprocess.Popen(['python', script])


if __name__ == '__main__':
    main()
