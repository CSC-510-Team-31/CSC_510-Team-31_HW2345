from args import The
from example import Example
import sys
# let's test modules import from the src folder
sys.path.insert(1, "../src")
sys.path.insert(1, "src")


def main():
    "Not fully working right now... will fix during HW4 so that it can be integrated into GitHub actions"

    successes, failures, crashes = Example().run_examples(The().the)

    print("Ran a total of {} tests\033[92m {} success(es)\033[00m and\033[91m {} failure(s)\033[00m".format(
        successes + failures, successes, failures))

    assert crashes == 0
    return failures

if __name__ == '__main__':
    main()
