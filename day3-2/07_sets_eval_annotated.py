"""07_sets_eval_annotated.py
Annotated set and retrieval evaluation examples for a .NET developer.
"""

# What it does: Demonstrates deduplicating document ids.
def example_deduplication():
    # What it does: Creates a nested list of retrieved document ids.
    # C# equivalent: var queryResults = new List<List<string>> { ... };
    query_results = [["doc_001", "doc_002", "doc_005"], ["doc_002", "doc_003", "doc_005"], ["doc_001", "doc_004"]]
    # What it does: Flattens and deduplicates in one set comprehension.
    # C# equivalent: var allDocIds = queryResults.SelectMany(results => results).ToHashSet();
    all_doc_ids = {doc_id for results in query_results for doc_id in results}
    print(all_doc_ids)

# What it does: Demonstrates set operations used in retrieval evaluation.
def example_set_operations():
    # What it does: Creates the expected relevant set.
    # C# equivalent: var expected = new HashSet<string> { ... };
    expected = {"doc_001", "doc_002", "doc_003"}
    # What it does: Creates the retrieved set.
    # C# equivalent: var retrieved = new HashSet<string> { ... };
    retrieved = {"doc_001", "doc_003", "doc_005"}
    # What it does: Computes intersection (true positives / hits).
    # C# equivalent: var hits = expected.Intersect(retrieved).ToHashSet();

    total = expected | retrieved  # same as expected.union(retrieved)

    hits = expected & retrieved  # same as expected.intersection(retrieved)
    # What it does: Computes what was expected but not retrieved.
    # C# equivalent: var missed = expected.Except(retrieved).ToHashSet();
    missed = expected - retrieved  # same as expected.difference(retrieved)
    # What it does: Computes retrieved extras / false positives.
    # C# equivalent: var extra = retrieved.Except(expected).ToHashSet();
    extra = retrieved - expected    # same as retrieved.difference(expected)
    # What it does: Calculates recall.
    # C# equivalent: var recall = (double)hits.Count / expected.Count;
    recall = len(hits) / len(expected)
    # What it does: Calculates precision.
    # C# equivalent: var precision = (double)hits.Count / retrieved.Count;
    precision = len(hits) / len(retrieved)
    print("Hits:", hits)
    print("Missed:", missed)
    print("Extra:", extra)
    print(f"Recall: {recall:.1%}")
    print(f"Precision: {precision:.1%}")

    #explanation: The symmetric_difference_update method modifies the expected set in place to contain only elements that are in either expected or retrieved but not in both. This is useful for quickly identifying discrepancies between the two sets.
    expected.symmetric_difference_update(retrieved)  # same as expected.symmetric_difference_update(retrieved)


# What it does: Shows simple deduplication of repeated chunk ids.
def example_chunk_deduplication():
    # C# equivalent: var chunks = new List<string> { ... };
    chunks = ["c1", "c2", "c2", "c3", "c1"]
    # What it does: Converts the list to a set to remove duplicates.
    # C# equivalent: var uniqueChunks = chunks.ToHashSet();
    unique_chunks = set(chunks)
    print(unique_chunks)

# What it does: Main runner.
def main():
    example_deduplication()
    example_set_operations()
    example_chunk_deduplication()

if __name__ == "__main__":
    main()
