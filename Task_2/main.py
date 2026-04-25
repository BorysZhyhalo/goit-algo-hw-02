from collections import deque

def is_palindrome(s):
    normalized_text = s.strip().lower()
    cleaned_text = ''.join(c for c in normalized_text if c.isalnum())
    char_deque = deque(cleaned_text)

    while len(char_deque) > 1:
        left_char = char_deque.popleft()
        right_char = char_deque.pop()
        if left_char != right_char:
            return False
    return True


if __name__ == "__main__":    
    test_cases = [
        "A man, a plan, a canal, Panama",
        "No 'x' in Nixon",      "Hello, World!",    "Was it a car or a cat I saw?",    
        "Madam In Eden, I'm Adam",    "Not a palindrome"   ]

    for test in test_cases:        
        result = is_palindrome(test)
        print(f"'{test}' -> {result}")
        