"""Brute Force shall not pass"""
import time
from banking_system import BankingSystem


def brute_force_check():
    """
    Simulates Brute Force attack
        Runs login() method in loop with brute_force_check=True parameter
        to avoid input card and pin values from terminal

        Checks that next solutions implemented:
            * Provides unspecified message in failed login case
            * Blocks Login after 5 failed attempts
            * Blocking time is 60s
            * Captcha should be solved to enable Login
    """
    bf_check = BankingSystem()
    while True:
        print("-" * 70 + time.ctime() + "-" * 10)
        bf_check.login(brute_force_check=True)
        time.sleep(5)


if __name__ == '__main__':
    brute_force_check()
