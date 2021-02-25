#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


def phoneNumberMnemonics(phoneNumber: str):
    mnenomics = {
        "1": "1",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
        "0": "0",
    }
    numbers = list(phoneNumber)
    all_possible_mnenonics = list()
    for number in numbers:
        tmp = list()
        for m in list(mnenomics[number]):
            if all_possible_mnenonics:
                for item in all_possible_mnenonics:
                    tmp.append(item + m)
            else:
                tmp.append(m)
        all_possible_mnenonics = list(tmp)
    return all_possible_mnenonics


if __name__ == "__main__":
    phone_number = "1905"
    print(phoneNumberMnemonics(phone_number))
