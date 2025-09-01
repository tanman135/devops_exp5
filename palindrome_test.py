def is_palindrome(s: str) -> bool:
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    test_strings = [
        "Racecar",
        "No lemon, no melon",
        "Was it a car or a cat I saw?",
        "Hello World"
    ]

    # MODIFIED PART
    # Ask user for input
    user_input = input("Enter a string to check palindrome (or press Enter to skip): ")
    if user_input:
        test_strings.append(user_input)

    for text in test_strings:
        result = "Palindrome" if is_palindrome(text) else "Not a palindrome"
        print(f"{text!r} -> {result} (Length: {len(text)})")
