#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


ALPHABETS = "abcdefghijklmnopqrstuvwxyz"


def get_new_letter(letter: str, key: int):
    return ALPHABETS[(ALPHABETS.index(letter) + key) % len(ALPHABETS)]


def caesarCipherEncryptor(string: str, key: int):
    cipher = ""
    for letter in string:
        cipher += get_new_letter(letter, key)
    return cipher


if __name__ == "__main__":
    string = "xyz"
    key = 2
    print(caesarCipherEncryptor(string, key))
