import sys
import os

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Not enough command line parameter provided.")
        sys.exit(1)

    filename = sys.argv[1]
    cmd = 'scp -P 65000 out/' + filename + '*.png deploy@localhost:/home/deploy/devel/mar/neural-style/in/'
    os.system(cmd)