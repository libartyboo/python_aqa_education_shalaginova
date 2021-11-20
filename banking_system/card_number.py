"""Generating and checking card number"""
import random


def generate_card():
    """Generates card number"""
    iin = "400000"
    account_identifier = random.randint(100000000, 999999999)
    checksum = get_checksum(iin + str(account_identifier) + "0")
    return iin + str(account_identifier) + str(checksum)


def generate_password():
    """Generates password"""
    return random.randint(1000, 9999)


def get_checksum(value):
    """Calculates and return checksum number for card"""
    sum_value = luhn_sum(value)
    if sum_value % 10 != 0:
        return 10 - sum_value % 10
    else:
        return 0


def luhn_sum(value):
    """Calculates and return card sum by LUHN algorithm"""
    card_numbers = list(map(int, value))
    sum_num = 0
    for ind, num in enumerate(card_numbers[::-1]):
        if ind % 2 != 0:
            num *= 2
            if num > 9:
                num = sum(int(d) for d in str(num))
        sum_num += num
    return sum_num


def luhn(value):
    """Validate card number by sum value. Returns True or False"""
    return luhn_sum(value) % 10 == 0


if __name__ == '__main__':
    # card
    card_test = generate_card()
    print(card_test)
    # password
    print(generate_password())
    # validate generated card
    print(f"card: {card_test}, check sum: {luhn_sum(card_test)}, valid: {luhn(card_test)}")
    # validate card
    print(f"card: 4000008626700415, check sum: {luhn_sum('4000008626700415')}, "
          f"valid: {luhn('4000008626700415')}")
