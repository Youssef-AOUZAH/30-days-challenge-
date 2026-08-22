import string

def hex_chars(hash):
    typeList = list(string.hexdigits)
    for c in hash:
        if c not in typeList:
            return False
    return True

def is_md5(hash):
    return len(hash)==32 and hex_chars(hash)

def is_sha1(hash):
    return len(hash)==40 and hex_chars(hash)

def is_sha256(hash):
    return len(hash)==64 and hex_chars(hash)

def is_sha512(hash):
    return len(hash)==128 and hex_chars(hash)

def which_hash(hash):
    if is_md5(hash):
        return 'md5'
    elif is_sha1(hash):
        return 'sha1'
    elif is_sha256(hash):
        return 'sha256'
    elif is_sha512(hash):
        return 'sha512'