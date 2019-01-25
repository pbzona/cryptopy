import base64


def hex_to_base64(hex):
    b = bytes.fromhex(hex)
    return base64.b64encode(b).decode("utf-8")


def xor_bytes(a, b):
    return a ^ b
