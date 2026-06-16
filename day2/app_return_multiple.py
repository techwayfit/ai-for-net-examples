def analyze_response(text: str) -> tuple[str, float, int]:
    """Returns (cleaned_text, confidence_score, token_count)."""
    cleaned = text.strip()
    confidence = 0.95  # hypothetical scoring
    tokens = len(cleaned.split())
    return cleaned, confidence, tokens  # Python auto-wraps in tuple

# Unpack at the call site
raw_llm_output = "   This is a response from the LLM.   "
text, score, count = analyze_response(raw_llm_output)
print(f"Got {count} tokens with {score:.0%} confidence")

