import args
from constants import H_OPTION, HELP_STRING
from example import Example


def main():
    the_args = args.The()
    if the_args.the[H_OPTION] == True:
        print(HELP_STRING)
    else:
        Example().run_examples(the_args.the)

if __name__ == '__main__':
    main()
