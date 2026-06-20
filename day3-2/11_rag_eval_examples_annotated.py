"""11_rag_eval_examples_annotated.py
Annotated RAG evaluation examples for a .NET developer.
"""
from pprint import pprint

# What it does: Calculates precision/recall per evaluation row.
def example_per_question_metrics():
    # What it does: Creates evaluation rows with expected and retrieved docs.
    # C# equivalent: var evalRows = new List<Dictionary<string, object>> { ... };
    eval_rows = [
        {"question": "What is RAG?", "expected_docs": {"doc_001", "doc_002"}, "retrieved_docs": ["doc_001", "doc_003", "doc_002"]},
        {"question": "How do embeddings work?", "expected_docs": {"doc_010"}, "retrieved_docs": ["doc_010", "doc_011"]},
        {"question": "Explain chunking", "expected_docs": {"doc_020", "doc_021"}, "retrieved_docs": ["doc_999"]},
    ]
    # What it does: Starts an empty result list.
    # C# equivalent: var results = new List<Dictionary<string, object>>();
    results = []
    # What it does: Iterates over the evaluation rows.
    # C# equivalent: foreach (var row in evalRows)
    for row in eval_rows:
        # What it does: Reads the expected set.
        expected = row["expected_docs"]
        # What it does: Converts retrieved docs to a set for set algebra.
        # C# equivalent: var retrieved = row.RetrievedDocs.ToHashSet();
        retrieved = set(row["retrieved_docs"])
        # What it does: Calculates hits as intersection.
        # C# equivalent: var hits = expected.Intersect(retrieved).ToHashSet();
        hits = expected & retrieved
        # What it does: Precision = hits / retrieved.
        precision = len(hits) / len(retrieved) if retrieved else 0.0
        # What it does: Recall = hits / expected.
        recall = len(hits) / len(expected) if expected else 0.0
        # What it does: Appends a result dictionary.
        # C# equivalent: results.Add(new Dictionary<string, object> { ... });
        results.append({"question": row["question"], "hits": sorted(hits), "precision": round(precision, 3), "recall": round(recall, 3)})
    pprint(results)

# What it does: Aggregates metrics over rows.
def example_overall_average():
    # What it does: Creates simplified precision/recall rows.
    rows = [{"precision": 0.667, "recall": 1.0}, {"precision": 0.5, "recall": 1.0}, {"precision": 0.0, "recall": 0.0}]
    # What it does: Averages all precision values.
    # C# equivalent: var avgPrecision = rows.Average(r => (double)r["precision"]);
    avg_precision = sum(r["precision"] for r in rows) / len(rows)
    # What it does: Averages all recall values.
    # C# equivalent: var avgRecall = rows.Average(r => (double)r["recall"]);
    avg_recall = sum(r["recall"] for r in rows) / len(rows)
    print(f"Average precision={avg_precision:.3f}")
    print(f"Average recall={avg_recall:.3f}")

# What it does: Main runner.
def main():
    example_per_question_metrics()
    example_overall_average()

if __name__ == "__main__":
    main()
