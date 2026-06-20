"""12_batch_processing_annotated.py
Annotated batch processing examples for a .NET developer.
"""
from pprint import pprint

responses = [
    {"id": "msg_1", "text": "Embeddings are dense vector representations...", "tokens": 42, "finish_reason": "end_turn"},
    {"id": "msg_2", "text": "RAG stands for Retrieval-Augmented Generation...", "tokens": 38, "finish_reason": "end_turn"},
    {"id": "msg_3", "text": None, "tokens": 0, "finish_reason": "max_tokens"},
    {"id": "msg_4", "text": "Vector databases store high-dimensional embeddings...", "tokens": 55, "finish_reason": "end_turn"},
]

# What it does: Defines a generator function that yields fixed-size chunks.
# C# equivalent: static IEnumerable<List<T>> ChunkList<T>(List<T> items, int size)
def chunk_list(items, size):
    # What it does: Steps through the list in increments of `size`.
    # C# equivalent: for (int i = 0; i < items.Count; i += size)
    for i in range(0, len(items), size):
        # What it does: Yields a slice from i up to i+size.
        # `yield` turns this into a generator.
        # C# equivalent: yield return items.Skip(i).Take(size).ToList();
        yield items[i:i+size]

# What it does: Shows how to create batches from a list.
def example_batching():
    # What it does: Materializes the generator into a list of batches.
    # C# equivalent: var batches = ChunkList(responses, 2).ToList();
    batches = list(chunk_list(responses, 2))
    # What it does: Iterates with a 1-based index.
    # C# equivalent: use a for loop or counter variable.
    for i, batch in enumerate(batches, start=1):
        print(f"Batch {i}: {[r['id'] for r in batch]}")

# What it does: Computes summary metrics per batch.
def example_batch_summary():
    batches = list(chunk_list(responses, 2))
    summaries = []
    for i, batch in enumerate(batches, start=1):
        # What it does: Appends a summary dictionary for each batch.
        # C# equivalent: summaries.Add(new Dictionary<string, object> { ... });
        summaries.append({
            "batch": i,
            # What it does: Uses len() for count.
            # C# equivalent: batch.Count
            "count": len(batch),
            # What it does: Counts only items with text using a generator expression.
            # C# equivalent: batch.Count(r => r["text"] != null)
            "valid_count": sum(1 for r in batch if r["text"]),
            # What it does: Sums token totals in the batch.
            # C# equivalent: batch.Sum(r => (int)r["tokens"])
            "token_total": sum(r["tokens"] for r in batch)
        })
    pprint(summaries)

# What it does: Main runner.
def main():
    example_batching()
    example_batch_summary()

if __name__ == "__main__":
    main()
