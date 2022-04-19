import struct


def parse_array(data, size, typ, offset):  # Unpacking an array
    n = struct.calcsize(typ)
    return list(struct.unpack(f'>{size}{typ}',
                              data[offset: offset + size * n]))


def parse_array_struct_b(data, size, offset):  # Unpacking a struct-array B
    arr = list()
    for count in range(size):
        arr.append(parse_b(data, offset + count * 51))  # 51 = size of struct B
    return arr


def parse_d(data, offset):
    d1 = parse_array(data, 3, 'b', offset)  # Unpacking an array
    d2 = struct.unpack('>B', data[offset + 3: offset + 3 + 1])[0]
    d3 = struct.unpack('>B', data[offset + 4: offset + 4 + 1])[0]
    d4 = struct.unpack('>i', data[offset + 5: offset + 5 + 4])[0]
    return {'D1': d1, 'D2': d2, 'D3': d3, 'D4': d4}


def parse_c(data, offset):
    c1 = struct.unpack('>d', data[offset: offset + 8])[0]
    c2 = struct.unpack('>B', data[offset + 8: offset + 8 + 1])[0]
    c3 = struct.unpack('>i', data[offset + 9: offset + 9 + 4])[0]
    c4 = struct.unpack('>f', data[offset + 13: offset + 13 + 4])[0]
    return {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4}


def parse_b(data, offset):
    b1 = parse_array(data, 6, 's', offset)
    b1 = b1[0].decode()
    b2 = parse_array(data, 8, 'h', offset + 6)  # h = 2
    b3 = struct.unpack('>Q', data[offset + 22: offset + 22 + 8])[0]
    b4 = parse_c(data, offset + 30)  # c = 17
    b5_offset = struct.unpack('>I', data[offset + 47: offset + 47 + 4])[0]
    b5 = parse_d(data, b5_offset)
    return {'B1': b1, 'B2': b2, 'B3': b3, 'B4': b4, 'B5': b5}  # b = 51


def parse_a(data, offset):
    a1 = struct.unpack('>H', data[offset: offset + 2])[0]
    a2 = struct.unpack('>i', data[offset + 2: offset + 2 + 4])[0]
    a3 = struct.unpack('>Q', data[offset + 6: offset + 6 + 8])[0]
    a4 = struct.unpack('>b', data[offset + 14: offset + 14 + 1])[0]
    a5 = struct.unpack('>i', data[offset + 15: offset + 15 + 4])[0]
    a6 = struct.unpack('>I', data[offset + 19: offset + 19 + 4])[0]
    a7 = parse_array_struct_b(data, 2, offset + 23)
    a8 = struct.unpack('>I', data[offset + 125: offset + 125 + 4])[0]
    # Ctrl + D - copy current line
    return {'A1': a1, 'A2': a2, 'A3': a3, 'A4': a4, 'A5': a5,
            'A6': a6, 'A7': a7, 'A8': a8}


def main(data):
    return parse_a(data, 3)  # offset = 3


inp_1 = (b'EGI\\\xfdI\xcc\x02HH\tg\xac\x01\xae'
         b'\xf0\xd1\xca\xbe(S=\xd8\xfc\xae\xb2kjakvw'
         b'y\xc7\x19\x12\xca\xa8Q\x19\t\xf0a@\xbe'
         b'\xfc\x11\r\xfcQ\xc9\xa9)\xa3\xb1\x0b'
         b'\xbf\xe8rr7\\\xc1t\t-\xc1P\xe2\xbfCh'
         b'\xd2\x00\x00\x00\x84xbdgqv&'
         b'\xdc\x1a\xe5\x9e\xb4\xff\xe8\xee\xa5'
         b'\x16\xc2\xc6\x95\xef\x1b/\xfd\x94:q'
         b'\xa0p\x12?\xba%\xda*\x8au\x90\x85\xbb'
         b'\xc5\x8e\xe4>\xdc\xe6}\x00\x00\x00\x8d'
         b'\x92U\x83V+4\x06\xd1\xcf\xdfO\x12H7\x90'
         b'\xa9y\nbd\xfc\x97')

inp_2 = (b'EGI\x12ZZw\xb00n\x1e\xe5\xde\xa6'
         b'\xa5\xae\nv\x9a\x97\xe1\x19\x80\xa9-Dcnwqjt'
         b'E\xf7p\x93,\x15#\x1e\x95=\xddE.V\xfe'
         b'\xcaST\xe3U\x0cE\xa8j?\xe1\x94\x16'
         b'c\x1f\x18\xde`\x05\xb7I\xe5\xbd'
         b'\xdc\x95\x12\x00\x00\x00\x84ygsozd<'
         b'\xa0\xf9\xc3\xaaf\x9b\xbd%9\x03'
         b'\x1b|\xfd\xe3x\xc3\xe4\x14\x96[|o\xb0\xbf'
         b'\xc9\x14\x88\r/$`\xb16\x12\xb7'
         b'\xd2=\x81Z/\x00\x00\x00\x8d\xa2\xbf\xea?'
         b'\xafcb\xd0:\xd5\xc5\xf6M'
         b'\x03)\x02\xe9J\xa7)\x01F')

main(inp_1)
main(inp_2)
