import argparse
import funcs

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--key')
    parser.add_argument('-v', '--value')
    args = parser.parse_args()
    k, v = args.key, args.value
    if not v and k:
        funcs.show_by_key(k)
    elif v and k:
        funcs.store_by_key(k, v)
    else:
        print('the utile needs the key argument to read and the key and the value arguments to write')
    

if __name__ == '__main__':
    main()
