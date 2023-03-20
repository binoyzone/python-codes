def count_vowels(string):
    vowels_string = "aeiouAEIOU"
    vowels_count = 0
    for char in string:
        if char in vowels_string:
            vowels_count += 1

    return vowels_count


if __name__ == '__main__':
    string = "Aeroplane"
    print(count_vowels(string))
