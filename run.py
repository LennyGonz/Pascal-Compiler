# coding=utf-8
from __future__ import absolute_import

import pprint

from scanner import get_token # scanner
from Pascal_Helper_Files.pascal_reader import PascalFile
from parse import Parser # parser
from emulator import Emulator # emulator

if __name__ == '__main__':
    pretty_printer = pprint.PrettyPrinter()

    # UNCOMMENT the below statements one at a time

    tokens = get_token(PascalFile(input_file_location='array_example.pas', output_location=''))
    # tokens = get_token(PascalFile(input_file_location='assignment_example.pas', output_location=''))
    # tokens = get_token(PascalFile(input_file_location='for_example.pas', output_location=''))
    # tokens = get_token(PascalFile(input_file_location='if_example.pas', output_location=''))
    # tokens = get_token(PascalFile(input_file_location='while_example.pas', output_location=''))
    

    # UNCOMMENT THE LINE BELOW TO TEST THE SCANNER --> YOU WILL SEE THE TOKENS
    # pretty_printer.pprint(tokens)
    
    print '----------------------------------'

    # parser = Parser(token_list=tokens, verbose=True) 
    parser = Parser(token_list=tokens)
    byte_array = parser.parse()
    # This prints the byte array, uncomment to see the bytearray
    # pretty_printer.pprint(byte_array)
    print '----------------------------------'
    emulator = Emulator(byte_array)
    emulator.start()
