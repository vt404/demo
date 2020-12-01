import sys

def fun(x):
    print(x)
    
if __name__ == '__main__':
    arg_list = sys.argv
    if len(arg_list) == 2:
        fun(arg_list[1])
    else:
        raise Exception('wrong args attached')