from IDA_parse import *
from make_seq_file import *
from opcode_seq import *
import os

def main():
    directorypath = os.getcwd()+'/data'
    idaParse(directorypath)
    getOpcodeSequence(directorypath)
    pass

if __name__ == '__main__':
    main()


