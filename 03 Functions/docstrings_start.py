# Demonstrate the use of function docstrings


def myFunction(arg1, arg2=None):
    """myFunction(arg1, arg2=None) --> doesn't really do anything. Just prints.

    Parameters:
    arg1: the first argument, print whatever you like
    arg2: the second argument, defaults to none
    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
