#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    for args in dir(hidden_4):
        if args[:2] != '__':
            print("{}".format(args))
