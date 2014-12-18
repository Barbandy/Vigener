import sys
import argparse


def writeFile(fname, code):
    try:
        with open(fname, 'wb') as f:
		    f.write(''.join(code))
    except IOError:
        exit('No such file or directory ' + fname)


def readFile(fname):
    try:
        with open(fname, 'rb') as f:
            text = f.read()
    except IOError:
        exit('No such file or directory ' + fname)
    return text	

	
def vigenere(data, key, func):
    key_len = len(key)
    output = []
    for i in range(len(data)):
        tmp = chr(func(ord(data[i]), ord(key[i % key_len])) % 256)
        output.append(tmp)
    return output


def printUsage():
    print"Enter the input parameters:"
    print"<name of program> <file_in> <file_key> <file_out> <c / d>"
    sys.exit(-1)

	
def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('inFile')
    parser.add_argument('keyFile')
    parser.add_argument('outFile')
    parser.add_argument('cryptOrDecrypt', choices=['c', 'd'])
    return parser.parse_args()	

	
if __name__ == "__main__":
    print"Vigenere cipher"
    data = ""
    key = ""
    code = ""
    if len(sys.argv) < 4 or len(sys.argv) > 5:
        printUsage()
    args = getArgs()
    data = readFile(args.inFile)
    key = readFile(args.keyFile)

    do = {'c': lambda x, y: x + y, 'd': lambda x, y: x - y}
    code = vigenere(data, key, do[args.cryptOrDecrypt])
    writeFile(args.outFile, code)
