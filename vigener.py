import sys


def read_file(fname):
    try:
        f = open(fname, 'rb')
        text = f.read()
        f.close()
    except IOError:
        print("\nRead error\n")
    return text


def write_file(fname, code):
    try:
        f = open(fname, 'wb')
        f.write(''.join(code))
        f.close()
    except IOError:
        print("\nWrite error\n")
   
   
def vigenere(data, key, func):
    key_len = len(key)
    output = []
    for i in range(len(data)):
        tmp = chr(func(ord(data[i]), ord(key[i % key_len])) % 256)
        output.append(tmp)
    return output


def print_start():
    print"Vigenere cipher\n"
    print"Enter the input parameters:\n"
    print"\n<name of program> <file_in> <file_key> <file_out> <c / d>\n"
    sys.exit(-1)


if __name__ == "__main__":
    print"Vigenere cipher"
    in_text = ""
    in_key = ""
    out_code = ""

    file_in = sys.argv[1]
    file_key = sys.argv[2]
    file_out = sys.argv[3]
    action = sys.argv[4]

    if len(sys.argv) < 4 or len(sys.argv) > 5:
        print_start()
    in_text = read_file(file_in)
    in_key = read_file(file_key)
    do = {'c': lambda x, y: x + y, 'd': lambda x, y: x - y}
    out_code = vigenere(in_text, in_key, do[action])
    write_file(file_out, out_code)
