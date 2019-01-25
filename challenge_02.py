# Fixed XOR
import base64
from cryptopals import xor_bytes

hex_str = "1c0111001f010100061a024b53535009181c"
xor_buffer = "686974207468652062756c6c277320657965"
expected = "746865206b696420646f6e277420706c6179"

solution_bytes = []
hex_bytes = bytes.fromhex(hex_str)
buf_bytes = bytes.fromhex(xor_buffer)

for i in range(len(hex_bytes)):
    solution_bytes.append(xor_bytes(hex_bytes[i], buf_bytes[i]))

solution = str(base64.b16encode(
    bytearray(solution_bytes)).decode("utf-8")).lower()

print(solution)
if not solution == expected:
    raise AssertionError("Fixed XOR not successful")
