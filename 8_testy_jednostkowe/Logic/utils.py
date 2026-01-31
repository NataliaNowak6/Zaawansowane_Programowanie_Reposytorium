import re
from typing import List, Dict, Any
from collections import Counter


def is_palindrome(text: str) -> bool:
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def count_vowels(text: str) -> int:
    vowels = "aeiouAEIOUąęóĄĘÓ"
    return sum(1 for c in text if c in vowels)


def calculate_discount(price: float, discount: float) -> float:
    if not 0 <= discount <= 1:
        raise ValueError("Discount must be between 0 and 1")
    return price * (1 - discount)


def flatten_list(nested_list: List[Any]) -> List[Any]:
    result: List[Any] = []

    def _flatten(lst: List[Any]):
        for item in lst:
            if isinstance(item, list):
                _flatten(item)
            else:
                result.append(item)

    _flatten(nested_list)
    return result


def word_frequencies(text: str) -> Dict[str, int]:
    words = re.findall(r'\b\w+\b', text.lower(), flags=re.UNICODE)
    return dict(Counter(words))


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True