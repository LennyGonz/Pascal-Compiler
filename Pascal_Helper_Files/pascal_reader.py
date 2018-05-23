# coding=utf-8
import os

PASCAL_FILE_EXT = '.pas'


class PascalFile(object):
    def __init__(self, input_file_location, output_location):

        self.input_file_location = os.path.join('Sample_Pascal_Code', input_file_location)
        self.output_file_location = output_location
        self.FILE = open(self.input_file_location)

        self.contents = self.FILE.read()

    def io_object(self):
        return self.FILE

    def __unicode__(self):
        return self.input_file_location

    def __del__(self):
        self.FILE.close()
