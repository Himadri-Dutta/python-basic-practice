"""
Python Assignment Solutions
Section A - Basic Functions and Numbers
Section B - String-Based Assignments
Section C - String + Loop Problems
Section D - Loops, Patterns and Menus
"""

# ============================================================
# SECTION A - Basic Functions and Numbers
# ============================================================

# 1. Even or Odd
def check_even_odd(n):
    if n % 2 == 0:
        print(f"{n} is Even")
    else:
        print(f"{n} is Odd")


# 2. Positive, Negative or Zero
def check_number(n):
    if n > 0:
        print(f"{n} is Positive")
    elif n < 0:
        print(f"{n} is Negative")
    else:
        print(f"{n} is Zero")


# 3. Find Largest of Two Numbers
def find_largest(a, b):
    if a > b:
        return a
    else:
        return b


# 4. Find Largest of Three Numbers (no max())
def find_largest3(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest


# 5. Sum of Natural Numbers (using for loop)
def sum_natural(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


# 6. Multiplication Table
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


# 7. Factorial Using Function (loop, no recursion)
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 8. Count Digits (while loop)
def count_digits(n):
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count


# 9. Reverse a Number
def reverse_number(n):
    negative = n < 0
    n = abs(n)
    reversed_num = 0
    while n != 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return -reversed_num if negative else reversed_num


# 10. Prime Number
def check_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


# ============================================================
# SECTION B - String-Based Assignments
# ============================================================

# 11. Count Characters in a String (no len())
def count_characters(text):
    count = 0
    for ch in text:
        count += 1
    return count


# 12. Count Vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count


# 13. Count Consonants
def count_consonants(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch.isalpha() and ch not in vowels:
            count += 1
    return count


# 14. Count Vowels and Consonants
def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0
    for ch in text:
        if ch.isalpha():
            if ch in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count


# 15. Reverse a String
def reverse_string_loop(text):
    reversed_text = ""
    for ch in text:
        reversed_text = ch + reversed_text
    return reversed_text


def reverse_string_slicing(text):
    return text[::-1]


# 16. Check Palindrome String
def check_palindrome(text):
    return text == text[::-1]


# 17. Count Words (no split())
def count_words(text):
    if count_characters(text) == 0:
        return 0
    word_count = 1  # at least one word if text is non-empty
    for ch in text:
        if ch == " ":
            word_count += 1
    return word_count


# 18. Find Frequency of a Character (no count())
def character_frequency(text, ch):
    freq = 0
    for c in text:
        if c == ch:
            freq += 1
    return freq


# 19. Remove Spaces (loop)
def remove_spaces(text):
    result = ""
    for ch in text:
        if ch != " ":
            result += ch
    return result


# 20. Convert Lowercase to Uppercase
def convert_uppercase_builtin(text):
    return text.upper()


def convert_uppercase_loop(text):
    result = ""
    for ch in text:
        if 'a' <= ch <= 'z':
            # shift lowercase to uppercase using ASCII difference
            result += chr(ord(ch) - 32)
        else:
            result += ch
    return result


# ============================================================
# SECTION C - String + Loop Problems
# ============================================================

# 21. Count Uppercase, Lowercase, Digits, Spaces
def count_case(text):
    upper = lower = digit = space = 0
    for ch in text:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            digit += 1
        elif ch == " ":
            space += 1
    return upper, lower, digit, space


# 22. Find First Character (no direct text[0])
def first_character(text):
    for ch in text:
        return ch
    return None


# 23. Find Last Character
def last_character_slicing(text):
    return text[-1]


def last_character_loop(text):
    last = None
    for ch in text:
        last = ch
    return last


# 24. Print Each Character
def display_characters(text):
    for ch in text:
        print(ch)


# 25. Print Characters with Position
def display_position(text):
    for i in range(len(text)):
        print(f"Position {i} : {text[i]}")


# 26. Remove Vowels (no replace())
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for ch in text:
        if ch not in vowels:
            result += ch
    return result


# 27. Find Longest Word (no dict, no max(), no advanced collections)
def find_longest_word(text):
    longest = ""
    current_word = ""
    for ch in text:
        if ch == " ":
            if count_characters(current_word) > count_characters(longest):
                longest = current_word
            current_word = ""
        else:
            current_word += ch
    # check last word
    if count_characters(current_word) > count_characters(longest):
        longest = current_word
    return longest


# 28. Count Occurrence of Each Vowel
def count_each_vowel(text):
    counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for ch in text:
        lower_ch = ch.lower()
        if lower_ch in counts:
            counts[lower_ch] += 1
    return counts


# ============================================================
# SECTION D - Loops, Patterns and Menus
# ============================================================

# 29. Star Pattern
def star_pattern(n):
    for i in range(1, n + 1):
        print("*" * i)


# 30. Number Pattern
def number_pattern(n):
    for i in range(1, n + 1):
        line = ""
        for j in range(1, i + 1):
            line += str(j)
        print(line)


# ============================================================
# DEMO / TEST DRIVER
# ============================================================
if __name__ == "__main__":
    print("=== Section A ===")
    check_even_odd(7)
    check_number(-5)
    print("Largest of 4, 9:", find_largest(4, 9))
    print("Largest of 3, 9, 6:", find_largest3(3, 9, 6))
    print("Sum 1 to 10:", sum_natural(10))
    multiplication_table(5)
    print("Factorial of 5:", factorial(5))
    print("Digits in 12345:", count_digits(12345))
    print("Reverse of 12345:", reverse_number(12345))
    print("Is 17 prime?", check_prime(17))

    print("\n=== Section B ===")
    print("Character count 'hello':", count_characters("hello"))
    print("Vowels in 'education':", count_vowels("education"))
    print("Consonants in 'education':", count_consonants("education"))
    v, c = count_vowels_consonants("Python Programming")
    print(f"Vowels: {v}, Consonants: {c}")
    print("Reversed (loop):", reverse_string_loop("hello"))
    print("Reversed (slicing):", reverse_string_slicing("hello"))
    print("Is 'madam' palindrome?", check_palindrome("madam"))
    print("Word count:", count_words("Python is easy to learn"))
    print("Frequency of 'g' in 'programming':", character_frequency("programming", "g"))
    print("Remove spaces:", remove_spaces("Python Programming Language"))
    print("Uppercase (builtin):", convert_uppercase_builtin("hello world"))
    print("Uppercase (loop):", convert_uppercase_loop("hello world"))

    print("\n=== Section C ===")
    u, l, d, s = count_case("Python123 ABC")
    print(f"Uppercase: {u}, Lowercase: {l}, Digits: {d}, Spaces: {s}")
    print("First character:", first_character("Hello"))
    print("Last character (slicing):", last_character_slicing("Hello"))
    print("Last character (loop):", last_character_loop("Hello"))
    display_characters("PYTHON")
    display_position("JAVA")
    print("Remove vowels:", remove_vowels("Python Programming"))
    print("Longest word:", find_longest_word("The quick brown fox jumps"))
    print("Vowel counts:", count_each_vowel("education"))

    print("\n=== Section D ===")
    star_pattern(5)
    number_pattern(5)