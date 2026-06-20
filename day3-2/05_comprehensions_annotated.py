"""05_comprehensions_annotated.py
Annotated comprehension examples for a .NET developer.
"""
from pprint import pprint

responses = [
    {"id": "msg_1", "text": "Embeddings are dense vector representations...", "tokens": 42, "finish_reason": "end_turn"},
    {"id": "msg_2", "text": "RAG stands for Retrieval-Augmented Generation...", "tokens": 38, "finish_reason": "end_turn"},
    {"id": "msg_3", "text": None, "tokens": 0, "finish_reason": "max_tokens"},
    {"id": "msg_4", "text": "Vector databases store high-dimensional embeddings...", "tokens": 55, "finish_reason": "end_turn"},
]

# What it does: Demonstrates list comprehensions.
# C# equivalent: static void ExampleListComprehensions() { ... }
def example_list_comprehensions():
    # What it does: Filters only end_turn responses.
    # C# equivalent: var complete = responses.Where(r => (string)r["finish_reason"] == "end_turn").ToList();
    complete = [r for r in responses if r["finish_reason"] == "end_turn"]
    print([r["id"] for r in complete])
    # What it does: Projects only the text fields for non-null responses.
    # C# equivalent: var texts = responses.Where(r => r["text"] != null).Select(r => (string)r["text"]).ToList();
    texts = [r["text"] for r in responses if r["text"] is not None]
    pprint(texts)
    # What it does: Filters, then transforms each item into a new dictionary.
    # C# equivalent: var longResponses = responses.Where(...).Select(r => new Dictionary<string, object> { ... }).ToList();
    long_responses = [{"id": r["id"], "word_count": len(r["text"].split())} for r in responses if r["text"] and r["tokens"] > 40]
    pprint(long_responses)

# What it does: Shows a nested comprehension for flattening a nested list.
# C# equivalent: static void ExampleNestedComprehension() { ... }
def example_nested_comprehension():
    # What it does: Creates a list of lists.
    # C# equivalent: var retrievedChunks = new List<List<string>> { ... };
    retrieved_chunks = [["chunk1a", "chunk1b"], ["chunk2a"], ["chunk3a", "chunk3b", "chunk3c"]]
    # What it does: Flattens the nested list into one list.
    # C# equivalent: var allChunks = retrievedChunks.SelectMany(chunkList => chunkList).ToList();
    #explanation: The nested comprehension iterates over each sublist (chunk_list) in retrieved_chunks, then iterates over each item (chunk) in that sublist, collecting all chunks into a single flat list.
    all_chunks = [chunk for chunk_list in retrieved_chunks for chunk in chunk_list]
    print(all_chunks)

# What it does: Shows dict and set comprehensions.
# C# equivalent: static void ExampleDictAndSetComprehensions() { ... }
def example_dict_and_set_comprehensions():
    # What it does: Builds a dictionary lookup from response id to text.
    # C# equivalent: var responseMap = responses.Where(r => r["text"] != null).ToDictionary(r => (string)r["id"], r => (string)r["text"]);
    response_map = {r["id"]: r["text"] for r in responses if r["text"]}
    pprint(response_map)
    # What it does: Builds a set from a comprehension.
    # C# equivalent: var tokenBands = responses.Select(r => (int)r["tokens"] >= 40 ? "high" : "low").ToHashSet();
    token_bands = {"high" if r["tokens"] >= 40 else "low" for r in responses}
    print(token_bands)

# What it does: Main runner.
def main():
    example_list_comprehensions()
    example_nested_comprehension()
    example_dict_and_set_comprehensions()

if __name__ == "__main__":
    main()
