def check_bias(text: str) -> bool:
    # Dummy check. Replace with actual logic.
    bias_keywords = ["gender", "religion", "caste", "race"]
    return any(word in text.lower() for word in bias_keywords)
