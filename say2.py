import sys
import cowsay
from sayings import goodbye
import sayings

if len(sys.argv) == 2:
    goodbye(sys.argv[1])

    sayings.hello(sys.argv[1])

    cowsay.trex(sys.argv[1])

# They issue seems that the cowsay adds spaces and, '_' underlines
# to make sure there is space and then have the output on a newline
# So I would have figure out how to:
# Remove spaces before cowsay.trex, or after sayings.hello
# Remove underlines the same way as above
# would I be able to drop characters, without needed to touch everyone
# As I recall you can count forward and backwards, positive forward, negative backwards
# so go back from cowsay.trex, and get rid of 11 characters, 3 space, 7 "_" underscores
    sayings.hello(""), cowsay.trex(sys.argv[1])

# For some reason this code makes it print everyone trex, which makes 3, although I am setting
# as the value for string and trying to convert from type none to type str
# because it takes system arguments and cowsay.trex prints the arguments
# in trex, then it gets called and loses value after then printing type string but
# nothing else if I add print(type(string))
    string = (cowsay.trex(sys.argv[1]))
    print(type(string)) # These two prints print class type which is 'NoneType' and then print 'None'
    print(string)