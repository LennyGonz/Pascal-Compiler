# coding=utf-8
from __future__ import absolute_import
import pprint
import sys
import os

'''
__future__  is only so that this code can be run whilist using Python 2 or Python 3
'''
from scanner import get_token
from emulator import Emulator
from parser import Parser
'''
This will read the Pascal files from the Sample Pascal Code files I have
'''
class reader(object):
    def __init__(self, input_file_location, output_location):
        """
        :param input_file_location: str
        :param output_location: str
        :return:
        """
        self.input_file_location = os.path.join('Sample Pascal Code', input_file_location)
        self.output_file_location = output_location
        self.FILE = open(self.input_file_location)

        self.contents = self.FILE.read()

    def io_object(self):
        return self.FILE

    def __unicode__(self):
        return self.input_file_location

    def __del__(self):
        self.FILE.close()

if __name__ == '__main__':
    pretty_printer = pprint.PrettyPrinter()

    # UNCOMMENT the below statements one at a time

    # tokens = get_token(reader(input_file_location='simple_assignment.pas', output_location=''))
    # tokens = get_token(reader(input_file_location='complex_assignments.pas', output_location=''))
    # tokens = get_token(reader(input_file_location='control_repeat.pas', output_location=''))
    # tokens = get_token(reader(input_file_location='control_while.pas', output_location=''))
    # tokens = get_token(reader(input_file_location='control_if.pas', output_location=''))
    # tokens = get_token(reader(input_file_location='control_for.pas', output_location=''))
    # tokens = get_token(reader(input_file_location='case_statement.pas', output_location=''))
    tokens = get_token(reader(input_file_location='arrays.pas', output_location=''))

    # This prints tokens, uncomment to see the generated tokens
    pretty_printer.pprint(tokens)
    print '----------------------------------'

    # setting verbose=True to parser will print to console as tokens are matched/warnings
    parser = Parser(token_list=tokens, verbose=True)
    parser = Parser(token_list=tokens)
    byte_array = parser.parse()

    # This prints the byte array, uncomment to see the bytearray
    pretty_printer.pprint(byte_array)
    print '----------------------------------'
    emulator = Emulator(byte_array)
    emulator.start()
