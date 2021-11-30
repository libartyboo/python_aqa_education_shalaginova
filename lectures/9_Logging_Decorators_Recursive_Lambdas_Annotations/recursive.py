def recursive_factorial(n):
    # Recursive case
    return n * recursive_factorial(n-1)


def recursive_factorial_check(n):
    # Base case
    if n == 0:
        return 1
    # Recursive case
    else:
        return n * recursive_factorial(n - 1)


print(recursive_factorial_check(5))

vowels = {'a', 'e', 'i', 'o', 'u'}


def find_apostrophe(word, start):
    i = word.find("'", start)

    if i == -1:  # there are no apostrophes in the given word
        return -1

    if i == 0:  # found apostrophe is the first symbol in the word, it doesn't meet the conditions
        return find_apostrophe(word, 1)  # keep searching further

    elif i == len(word) - 1:  # the apostrophe is the last symbol, doesn't meet the conditions
        return -1  # we have reached the end of the word and haven't found a correct apostrophe

    else:
        previous_char = word[i - 1]
        if previous_char in vowels:
            return i

        else:  # the found apostrophe does not meet the conditions, we keep searching further
            return find_apostrophe(word, i + 1)


print(find_apostrophe("ma'ma", 0))
print(find_apostrophe("'wave'", 0))
