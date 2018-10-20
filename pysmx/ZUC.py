#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 河北雪域网络科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.snowland.ltd
# @file: ZUC.py
# @time: 2018/10/20 17:23
# @Software: PyCharm


S0 = [
    0x3E, 0x72, 0x5B, 0x47, 0xCA, 0xE0, 0x00, 0x33, 0x04, 0xD1, 0x54, 0x98, 0x09, 0xB9, 0x6D, 0xCB,
    0x7B, 0x1B, 0xF9, 0x32, 0xAF, 0x9D, 0x6A, 0xA5, 0xB8, 0x2D, 0xFC, 0x1D, 0x08, 0x53, 0x03, 0x90,
    0x4D, 0x4E, 0x84, 0x99, 0xE4, 0xCE, 0xD9, 0x91, 0xDD, 0xB6, 0x85, 0x48, 0x8B, 0x29, 0x6E, 0xAC,
    0xCD, 0xC1, 0xF8, 0x1E, 0x73, 0x43, 0x69, 0xC6, 0xB5, 0xBD, 0xFD, 0x39, 0x63, 0x20, 0xD4, 0x38,
    0x76, 0x7D, 0xB2, 0xA7, 0xCF, 0xED, 0x57, 0xC5, 0xF3, 0x2C, 0xBB, 0x14, 0x21, 0x06, 0x55, 0x9B,
    0xE3, 0xEF, 0x5E, 0x31, 0x4F, 0x7F, 0x5A, 0xA4, 0x0D, 0x82, 0x51, 0x49, 0x5F, 0xBA, 0x58, 0x1C,
    0x4A, 0x16, 0xD5, 0x17, 0xA8, 0x92, 0x24, 0x1F, 0x8C, 0xFF, 0xD8, 0xAE, 0x2E, 0x01, 0xD3, 0xAD,
    0x3B, 0x4B, 0xDA, 0x46, 0xEB, 0xC9, 0xDE, 0x9A, 0x8F, 0x87, 0xD7, 0x3A, 0x80, 0x6F, 0x2F, 0xC8,
    0xB1, 0xB4, 0x37, 0xF7, 0x0A, 0x22, 0x13, 0x28, 0x7C, 0xCC, 0x3C, 0x89, 0xC7, 0xC3, 0x96, 0x56,
    0x07, 0xBF, 0x7E, 0xF0, 0x0B, 0x2B, 0x97, 0x52, 0x35, 0x41, 0x79, 0x61, 0xA6, 0x4C, 0x10, 0xFE,
    0xBC, 0x26, 0x95, 0x88, 0x8A, 0xB0, 0xA3, 0xFB, 0xC0, 0x18, 0x94, 0xF2, 0xE1, 0xE5, 0xE9, 0x5D,
    0xD0, 0xDC, 0x11, 0x66, 0x64, 0x5C, 0xEC, 0x59, 0x42, 0x75, 0x12, 0xF5, 0x74, 0x9C, 0xAA, 0x23,
    0x0E, 0x86, 0xAB, 0xBE, 0x2A, 0x02, 0xE7, 0x67, 0xE6, 0x44, 0xA2, 0x6C, 0xC2, 0x93, 0x9F, 0xF1,
    0xF6, 0xFA, 0x36, 0xD2, 0x50, 0x68, 0x9E, 0x62, 0x71, 0x15, 0x3D, 0xD6, 0x40, 0xC4, 0xE2, 0x0F,
    0x8E, 0x83, 0x77, 0x6B, 0x25, 0x05, 0x3F, 0x0C, 0x30, 0xEA, 0x70, 0xB7, 0xA1, 0xE8, 0xA9, 0x65,
    0x8D, 0x27, 0x1A, 0xDB, 0x81, 0xB3, 0xA0, 0xF4, 0x45, 0x7A, 0x19, 0xDF, 0xEE, 0x78, 0x34, 0x60
]

S1 = [
    0x55, 0xC2, 0x63, 0x71, 0x3B, 0xC8, 0x47, 0x86, 0x9F, 0x3C, 0xDA, 0x5B, 0x29, 0xAA, 0xFD, 0x77,
    0x8C, 0xC5, 0x94, 0x0C, 0xA6, 0x1A, 0x13, 0x00, 0xE3, 0xA8, 0x16, 0x72, 0x40, 0xF9, 0xF8, 0x42,
    0x44, 0x26, 0x68, 0x96, 0x81, 0xD9, 0x45, 0x3E, 0x10, 0x76, 0xC6, 0xA7, 0x8B, 0x39, 0x43, 0xE1,
    0x3A, 0xB5, 0x56, 0x2A, 0xC0, 0x6D, 0xB3, 0x05, 0x22, 0x66, 0xBF, 0xDC, 0x0B, 0xFA, 0x62, 0x48,
    0xDD, 0x20, 0x11, 0x06, 0x36, 0xC9, 0xC1, 0xCF, 0xF6, 0x27, 0x52, 0xBB, 0x69, 0xF5, 0xD4, 0x87,
    0x7F, 0x84, 0x4C, 0xD2, 0x9C, 0x57, 0xA4, 0xBC, 0x4F, 0x9A, 0xDF, 0xFE, 0xD6, 0x8D, 0x7A, 0xEB,
    0x2B, 0x53, 0xD8, 0x5C, 0xA1, 0x14, 0x17, 0xFB, 0x23, 0xD5, 0x7D, 0x30, 0x67, 0x73, 0x08, 0x09,
    0xEE, 0xB7, 0x70, 0x3F, 0x61, 0xB2, 0x19, 0x8E, 0x4E, 0xE5, 0x4B, 0x93, 0x8F, 0x5D, 0xDB, 0xA9,
    0xAD, 0xF1, 0xAE, 0x2E, 0xCB, 0x0D, 0xFC, 0xF4, 0x2D, 0x46, 0x6E, 0x1D, 0x97, 0xE8, 0xD1, 0xE9,
    0x4D, 0x37, 0xA5, 0x75, 0x5E, 0x83, 0x9E, 0xAB, 0x82, 0x9D, 0xB9, 0x1C, 0xE0, 0xCD, 0x49, 0x89,
    0x01, 0xB6, 0xBD, 0x58, 0x24, 0xA2, 0x5F, 0x38, 0x78, 0x99, 0x15, 0x90, 0x50, 0xB8, 0x95, 0xE4,
    0xD0, 0x91, 0xC7, 0xCE, 0xED, 0x0F, 0xB4, 0x6F, 0xA0, 0xCC, 0xF0, 0x02, 0x4A, 0x79, 0xC3, 0xDE,
    0xA3, 0xEF, 0xEA, 0x51, 0xE6, 0x6B, 0x18, 0xEC, 0x1B, 0x2C, 0x80, 0xF7, 0x74, 0xE7, 0xFF, 0x21,
    0x5A, 0x6A, 0x54, 0x1E, 0x41, 0x31, 0x92, 0x35, 0xC4, 0x33, 0x07, 0x0A, 0xBA, 0x7E, 0x0E, 0x34,
    0x88, 0xB1, 0x98, 0x7C, 0xF3, 0x3D, 0x60, 0x6C, 0x7B, 0xCA, 0xD3, 0x1F, 0x32, 0x65, 0x04, 0x28,
    0x64, 0xBE, 0x85, 0x9B, 0x2F, 0x59, 0x8A, 0xD7, 0xB0, 0x25, 0xAC, 0xAF, 0x12, 0x03, 0xE2, 0xF2
]

D = [
    0x44D7, 0x26BC, 0x626B, 0x135E, 0x5789, 0x35E2, 0x7135, 0x09AF,
    0x4D78, 0x2F13, 0x6BC4, 0x1AF1, 0x5E26, 0x3C4D, 0x789A, 0x47AC
]


def addition_uint31(a, b):
    c = a + b
    return (c & 0x7FFFFFFF) + (c >> 31)


def rotl_uint31(a, shift):
    return ((a << shift) | (a >> (31 - shift))) & 0x7FFFFFFF


def rotl_uint32(a, shift):
    return (a << shift) | (a >> (32 - shift))


def l1(x):
    return (x ^ rotl_uint32(x, 2) ^ rotl_uint32(x, 10) ^ rotl_uint32(x, 18) ^ rotl_uint32(x, 24))


def l2(x):
    return (x ^ rotl_uint32(x, 8) ^ rotl_uint32(x, 14) ^ rotl_uint32(x, 22) ^ rotl_uint32(x, 30))


def make_uint32(a, b, c, d):
    return ((a << 24) | (b << 16) | (c << 8) | d)


def make_uint31(a, b, c):
    return (a << 23) | (b << 8) | c


def lfsr_next(lfsr):
    f = lfsr[0]
    v = rotl_uint31(lfsr[0], 8)
    f = addition_uint31(f, v)
    v = rotl_uint31(lfsr[4], 20)
    f = addition_uint31(f, v)
    v = rotl_uint31(lfsr[10], 21)
    f = addition_uint31(f, v)
    v = rotl_uint31(lfsr[13], 17)
    f = addition_uint31(f, v)
    v = rotl_uint31(lfsr[15], 15)
    f = addition_uint31(f, v)
    return f


def lfsr_append(lfsr: list, f):
    # TODO check
    # memmove(&lfsr[0], &lfsr[1], 15 * sizeof())
    lfsr.insert(0, f)
    if len(lfsr) == 16:
        lfsr.pop()
    return lfsr


def lfsr_init(lfsr, u):
    lfsr_append(lfsr, addition_uint31(lfsr_next(lfsr), u))


def lfsr_shift(lfsr):
    lfsr_append(lfsr, lfsr_next(lfsr))


def f(context):
    W = (context.x[0] ^ context.r[0]) + context.r[1]
    W1 = context.r[0] + context.x[1]
    W2 = context.r[1] ^ context.x[2]
    u = l1((W1 << 16) | (W2 >> 16))
    v = l2((W2 << 16) | (W1 >> 16))
    context.r[0] = make_uint32(S0[u >> 24], S1[(u >> 16) & 0xFF],
                               S0[(u >> 8) & 0xFF], S1[u & 0xFF])
    context.r[1] = make_uint32(S0[v >> 24], S1[(v >> 16) & 0xFF],
                               S0[(v >> 8) & 0xFF], S1[v & 0xFF])
    return W


def bit_reorganization(context):
    context.x[0] = ((context.lfsr[15] & 0x7FFF8000) << 1) | (context.lfsr[14] & 0xFFFF)
    context.x[1] = ((context.lfsr[11] & 0xFFFF) << 16) | (context.lfsr[9] >> 15)
    context.x[2] = ((context.lfsr[7] & 0xFFFF) << 16) | (context.lfsr[5] >> 15)
    context.x[3] = ((context.lfsr[2] & 0xFFFF) << 16) | (context.lfsr[0] >> 15)

# class ZUC(object):
    # def __init__(self):
    #     self.context = []
    #     self
def zuc_init(context, key, iv):
    # Expand key.
    for i in range(16):
        context.lfsr[i] = make_uint31(key[i], D[i], iv[i])

    context.r = [0, 0]
    for i in range(32):
        bit_reorganization(context)
        w = f(context)
        lfsr_init(context.lfsr, w >> 1)
    return context


def zuc_generate_keystream(context, keystream_buffer):
    # keystream_length = len(keystream_buffer)
    bit_reorganization(context)
    f(context)  # Discard the output of F.
    lfsr_shift(context.lfsr)
    for i, buffer in enumerate(keystream_buffer):
        bit_reorganization(context)
        keystream_buffer[i] = f(context) ^ context.x[3]
        lfsr_shift(context.lfsr)


def zuc_encrypt(context, input):
    buffer = [0] * 4
    length = len(input)
    output = [0] * length
    bit_reorganization(context)
    f(context)  # Discard the output of F.
    lfsr_shift(context.lfsr)
    for i in range(length):
        buffer_index = i % 4
        if (buffer_index == 0):
            bit_reorganization(context)
            buffer = f(context) ^ context.x[3]
            lfsr_shift(context.lfsr)

        output[i] = input[i] ^ buffer[buffer_index]
    return output

if '__main__' == __name__:
    key = [0]*16
    iv = [0]*16
    zuc_init(key=key, iv=iv)
    zuc_generate_keystream()
