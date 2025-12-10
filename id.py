import random
import string

def random_alphanum(n):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))

def mod11_checksum(text):
    weights = [2,3,4,5,6,7,8,9,10][:len(text)]
    total = sum(ord(ch) * w for ch, w in zip(text, weights))
    remainder = total % 11
    return "X" if remainder == 10 else str(remainder)

def generate_glorbenian_id(structure_set="01", profile_tag="C"):
    SS = structure_set.zfill(2)
    RRRR = str(random.randint(0, 9999)).zfill(4)

    P = profile_tag.upper()[0]
    BBB = str(random.randint(0, 999)).zfill(3)

    XXXXXX = random_alphanum(6)

    # Checksum body
    body = SS + RRRR + P + BBB + XXXXXX

    # Strong checksum
    checksum = mod11_checksum(body)

    return f"UWG-{SS}-{RRRR}-{P}{BBB}-{XXXXXX}-{checksum}:3"


# Example
for _ in range(5):
    print(generate_glorbenian_id())
