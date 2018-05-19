# coding=utf-8
from __future__ import absolute_import

import pprint

from Compiler.scanner import get_token
from Compiler.Pascal_Helper_Files.pascalreader import PascalFile
from Compiler.parser import Parser
from Compiler.emulator import Emulator

if __name__ == '__main__':
    pretty_printer = pprint.PrettyPrinter()

    # UNCOMMENT the below statements one at a time
    tokens = get_token(PascalFile(input_file_location='array_example.pas', output_location=''))
    # tokens = get_token(PascalFile(input_file_location='assignment_example.pas', output_location=''))
    # tokens = get_token(PascalFile(input_file_location='case_statement_example.pas', output_location=''))
    # tokens = get_token(PascalFile(input_file_location='controlrepeat_example.pas', output_location=''))
    # tokens = get_token(PascalFile(input_file_location='for_example.pas', output_location=''))
    # tokens = get_token(PascalFile(input_file_location='if_example.pas', output_location=''))
    # tokens = get_token(PascalFile(input_file_location='while_example.pas', output_location=''))

    # This prints tokens, uncomment to see the generated tokens
    # pretty_printer.pprint(tokens)
    print '----------------------------------'
    # setting verbose=True to parser will print to console as tokens are matched/warnings
    # parser = Parser(token_list=tokens, verbose=True)
    parser = Parser(token_list=tokens)
    byte_array = parser.parse()
    # This prints the byte array, uncomment to see the bytearray
    # pretty_printer.pprint(byte_array)
    print '----------------------------------'
    emulator = Emulator(byte_array)
    emulator.start()