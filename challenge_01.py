# Convert hex to base64
import base64

hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
base64_str = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"


def hex_to_base64(hex):
    b = bytes.fromhex(hex)
    return base64.b64encode(b).decode("utf-8")


solution = hex_to_base64(hex_str)

print(solution)
if not solution == base64_str:
    raise AssertionError("Hex to base64 conversion not successful")
