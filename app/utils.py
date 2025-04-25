import re

def detect_bias(text: str) -> bool:
    biased_keywords = ["only women", "not for men", "housewife", "weak", "emotional"]
    return any(keyword in text.lower() for keyword in biased_keywords)
