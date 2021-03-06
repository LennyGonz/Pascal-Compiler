# coding=utf-8

import struct

class OPCODE(object):
    """
    PUSHI: push immediate
    PUSH: push
    POP:
    ADD:
    SUB:
    MULTIPLY:
    DIVIDE:
    DIV:
    CVR:
    """
    PUSHI = 0
    PUSH = 1
    POP = 2
    ADD = 3
    SUB = 4
    MULTIPLY = 5
    DIVIDE = 6
    DIV = 7
    CVR = 8
    GTE = 9
    DUP = 10
    JMP = 11
    JFALSE = 12
    JTRUE = 13
    HALT = 14
    PRINT_I = 15
    PRINT_C = 16
    PRINT_B = 17
    PRINT_R = 18
    NEW_LINE = 19
    NOT = 20
    XCHG = 21
    FADD = 22
    FSUB = 23
    FMULTIPLY = 24
    OR = 25
    LTE = 26
    EQL = 27
    NEQ = 28
    GTR = 29
    LES = 30
    PRINT_ILIT = 31
    POP_CHAR = 32
    PUSH_CHAR = 33
    DUMP = 34
    RETRIEVE = 35
    FDIVIDE = 36
    POP_REAL_LIT = 37
    RET_AND_PRINT = 38
    PRINT_STR_LIT = 39

class TYPE(object):
    I, R, B, C, S = range(5)

INSTRUCTION_LENGTH = 5

def float_to_bits(floaty):
    """
    :param floaty:
    :return:
    """
    s = struct.pack('>f', floaty)
    return struct.unpack('>l', s)[0]

def bits_to_float(bits):
    s = struct.pack('>l', bits)
    return struct.unpack('>f', s)[0]

def byte_unpacker(byte_list):
    return (byte_list[0] << 24) | (byte_list[1] << 16) | (byte_list[2] << 8) | (byte_list[3])

def byte_packer(value_to_pack):
    """
    Expands value to four bytes to be stored in bytearray
    :param value_to_pack: number
    :return: tuple
    """
    try:
        value_to_pack = int(value_to_pack)
    except ValueError:
        value_to_pack = float_to_bits(float(value_to_pack))

    return (value_to_pack >> 24) & 0xFF, (value_to_pack >> 16) & 0xFF, (
        value_to_pack >> 8) & 0xFF, value_to_pack & 0xFF

CONDITIONALS = {
    '<': True,
    '<>': True,
    '<=': True,
    '>': True,
    '>=': True,
    '=': True,
}
