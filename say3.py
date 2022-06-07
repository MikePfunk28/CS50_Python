import sys

from sayings2 import goodbye
import sayings2

if len(sys.argv) == 2:
    goodbye(sys.argv[1])

    sayings2.hello(sys.argv[1])