import sys


def compare_creds(args=None):
    if args is None:
        args = sys.argv
    print('START')
    print(f" USER:{args}")
    with open('creds.txt', 'w') as file:
        file.write(args[1])
    assert args[1] == 'testuser'


if __name__ == "__main__": compare_creds()
