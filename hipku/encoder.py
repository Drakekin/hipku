from __future__ import division
from ipaddress import ip_address
from math import log, ceil
from dictionaries import ipv4_key, ipv6_key, ipv4_schema, ipv6_schema, animal_adjectives, animal_colours, animal_nouns, \
    animal_verbs, nature_adjectives, nature_nouns, plant_nouns, plant_verbs
from re import sub


def process_octlet(octlet, m):
    y = octlet % m
    x = (octlet - y) // m
    return x, y


def log2(n):
    return log(n) / log(2)


def extract_bits(bit_field, start, bits):
    return (bit_field >> start) - ((bit_field >> start + bits) << bits)


def bit_width(n):
    return int(ceil(log2(n)))


def chunk(bit_field, chunk_size):
    limit = int(ceil(bit_width(bit_field) / chunk_size))
    for i in range(limit):
        yield extract_bits(bit_field, i * chunk_size, chunk_size)


def encode(address):
    if address.version == 4:
        m = 16
        dictionary = ipv4_key
        schema = ipv4_schema
        capitalise = (6, )
    elif address.version == 6:
        m = 256
        dictionary = ipv6_key
        schema = ipv6_schema
        capitalise = (0, 11)
    else:
        raise ValueError("Unsupported IP version")  # How?

    octlet_size = bit_width(m * m)
    address_int = int(address)

    words = []

    for octlet, (x_key, y_key) in zip(list(chunk(address_int, octlet_size))[::-1], dictionary):
        x, y = process_octlet(octlet, m)
        words.append(x_key[x])
        words.append(y_key[y])

    for index in capitalise:
        words[index] = words[index][0].upper() + words[index][1:]

    return schema.format(*words)


def decode(haiku):
    haiku = sub(r"[^a-z \n]", "", haiku.lower()).split()
    haiku = [h for h in haiku if h]

    if haiku[0] == "the":  # IPv4
        haiku.pop(0)  # consume "the"
        animal_adjective = haiku.pop(0)
        animal_colour = haiku.pop(0)
        animal_noun = haiku.pop(0)
        animal_verb = haiku.pop(0)
        haiku.pop(0)  # consume "in"
        haiku.pop(0)  # consume "the"
        nature_adjective = haiku.pop(0)
        nature_noun = haiku.pop(0)
        plant_verb = haiku.pop()  # plant verb is the last word
        plant_noun = " ".join(haiku)  # plant noun is whatever is next

        octlet1 = animal_adjectives.index(animal_adjective) * 16 + animal_colours.index(animal_colour)
        octlet2 = animal_nouns.index(animal_noun) * 16 + animal_verbs.index(animal_verb)
        octlet3 = nature_adjectives.index(nature_adjective) * 16 + nature_nouns.index(nature_noun)
        octlet4 = plant_nouns.index(plant_noun) * 16 + plant_verbs.index(plant_verb)

        return ip_address(u"{}.{}.{}.{}".format(octlet1, octlet2, octlet3, octlet4))
    else:  # IPv6
        words = haiku[:2] + haiku[3:]
        i = iter(words)
        tuples = zip(i, i)

        ip_sections = []

        for (x_word, y_word), (x_key, y_key) in zip(tuples, ipv6_key):
            n = x_key.index(x_word) * 256 + y_key.index(y_word)
            ip_sections.append(hex(n)[2:])

        return ip_address(u":".join(ip_sections))


