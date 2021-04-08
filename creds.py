import sys


def compare_creds(args=None):
    if args is None:
        args = sys.argv
    print('START')
    print(f" USER:{args}")
    assert args[1] == 'testuser'


if __name__ == "__main__": compare_creds()
