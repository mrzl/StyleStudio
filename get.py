import sys
import os


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Not enough command line parameter provided.")
        sys.exit(1)

    remotepath = sys.argv[1]
    mkdircmd = 'mkdir -p out/' + remotepath
    cmd = 'scp -P 65000 \'deploy@localhost:/home/deploy/devel/mar/neural-style/out/' + remotepath + '/*.png\' out/' + remotepath + '/'
    os.system(mkdircmd)
    os.system(cmd)