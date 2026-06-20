"""09_any_all_generators_annotated.py
Annotated any/all and generator examples for a .NET developer.
"""

responses = [
    {"id": "msg_1", "text": "Embeddings are dense vector representations...", "tokens": 42, "finish_reason": "end_turn"},
    {"id": "msg_2", "text": "RAG stands for Retrieval-Augmented Generation...", "tokens": 38, "finish_reason": "end_turn"},
    {"id": "msg_3", "text": None, "tokens": 0, "finish_reason": "max_tokens"},
    {"id": "msg_4", "text": "Vector databases store high-dimensional embeddings...", "tokens": 55, "finish_reason": "end_turn"},
]

# What it does: Shows boolean aggregation helpers.
def example_any_all():
    # What it does: Returns True if at least one response was truncated.
    # C# equivalent: var hasTruncated = responses.Any(r => (string)r["finish_reason"] == "max_tokens");
    has_truncated = any(r["finish_reason"] == "max_tokens" for r in responses)
    # What it does: Returns True only if every response contains an id key.
    # C# equivalent: var allHaveIds = responses.All(r => r.ContainsKey("id"));
    all_have_ids = all("id" in r for r in responses)
    print("Any truncated?", has_truncated)
    print("All have IDs?", all_have_ids)

# What it does: Shows generator expressions.
def example_generators():
    # What it does: Uses a generator expression with sum.
    # C# equivalent: var totalTokens = responses.Sum(r => (int)r["tokens"]);
    total_tokens = sum(r["tokens"] for r in responses)
    # What it does: Creates a generator that yields ids only for responses with text.
    # It is lazy until consumed.
    # C# equivalent: var ids = responses.Where(r => r["text"] != null).Select(r => (string)r["id"]);
    ids = (r["id"] for r in responses if r["text"])
    print("Total tokens:", total_tokens)
    print("Valid IDs:", list(ids))

# What it does: Main runner.
def main():
    example_any_all()
    example_generators()

if __name__ == "__main__":
    main()
