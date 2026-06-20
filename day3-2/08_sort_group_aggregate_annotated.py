"""08_sort_group_aggregate_annotated.py
Annotated sorting, grouping, and aggregation examples for a .NET developer.
"""
from collections import defaultdict, Counter
from pprint import pprint

responses = [
    {"id": "msg_1", "text": "Embeddings are dense vector representations...", "tokens": 42, "finish_reason": "end_turn"},
    {"id": "msg_2", "text": "RAG stands for Retrieval-Augmented Generation...", "tokens": 38, "finish_reason": "end_turn"},
    {"id": "msg_3", "text": None, "tokens": 0, "finish_reason": "max_tokens"},
    {"id": "msg_4", "text": "Vector databases store high-dimensional embeddings...", "tokens": 55, "finish_reason": "end_turn"},
]

# What it does: Shows sorting with sorted() and a key function.
def example_sorting():
    # What it does: Filters out records with missing text, then sorts by token count descending.
    # C# equivalent: var sortedResponses = responses.Where(r => r["text"] != null).OrderByDescending(r => (int)r["tokens"]).ToList();
    sorted_responses = sorted([r for r in responses if r["text"]], key=lambda r: r["tokens"], reverse=True)
    print([r["id"] for r in sorted_responses])

# What it does: Groups records by finish_reason.
def example_grouping_defaultdict():
    # What it does: Creates a defaultdict where missing keys auto-create an empty list.
    # C# equivalent: var grouped = new Dictionary<string, List<string>>();
    grouped = defaultdict(list)
    # What it does: Iterates over each response.
    # C# equivalent: foreach (var r in responses)
    for r in responses:
        # What it does: Appends the id into the group for that finish_reason.
        # C# equivalent: if (!grouped.ContainsKey(reason)) grouped[reason] = new List<string>(); grouped[reason].Add(id);
        grouped[r["finish_reason"]].append(r["id"])
    pprint(dict(grouped))

# What it does: Counts occurrences by finish_reason.
def example_counter():
    # What it does: Builds a Counter from a generator expression.
    # C# equivalent: responses.GroupBy(r => r["finish_reason"]).ToDictionary(g => g.Key, g => g.Count());
    finish_counts = Counter(r["finish_reason"] for r in responses)
    pprint(dict(finish_counts))

# What it does: Demonstrates aggregation helpers.
def example_aggregates():
    # What it does: Sums all token counts.
    # C# equivalent: var totalTokens = responses.Sum(r => (int)r["tokens"]);
    total_tokens = sum(r["tokens"] for r in responses)
    # What it does: Computes the average.
    # C# equivalent: var avgTokens = responses.Average(r => (int)r["tokens"]);
    avg_tokens = total_tokens / len(responses)
    # What it does: Finds the record with the maximum token count.
    # C# equivalent: var maxTokensResponse = responses.OrderByDescending(r => (int)r["tokens"]).First();
    max_tokens_response = max(responses, key=lambda r: r["tokens"])
    print(f"Total={total_tokens}, Avg={avg_tokens:.1f}, Max={max_tokens_response['id']}")

# What it does: Main runner.
def main():
    example_sorting()
    example_grouping_defaultdict()
    example_counter()
    example_aggregates()

if __name__ == "__main__":
    main()
