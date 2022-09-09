import args
from example import Example


def main():
    the_args = args.The()
    Example().run_examples(the_args.the)

if __name__ == '__main__':
    main()
