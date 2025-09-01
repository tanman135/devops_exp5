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
    for text in test_strings:
        result = "Palindrome" if is_palindrome(text) else "Not a palindrome"
        print(f"{text!r} -> {result}")
