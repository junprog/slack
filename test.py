import os
import sys
import time

def print_args(pid, args):
    print(os.getpid(), args)

if __name__ == "__main__":
    args = sys.argv
    print_args(os.getpid(), args)

    for i in range(0, 30, 1):
        time.sleep(1)
        print(i, "sec")