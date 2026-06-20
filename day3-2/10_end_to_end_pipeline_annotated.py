"""10_end_to_end_pipeline_annotated.py
Annotated end-to-end mini pipeline for a .NET developer.
"""
from pprint import pprint

responses = [
    {"id": "msg_1", "text": "Embeddings are dense vector representations...", "tokens": 42, "finish_reason": "end_turn"},
    {"id": "msg_2", "text": "RAG stands for Retrieval-Augmented Generation...", "tokens": 38, "finish_reason": "end_turn"},
    {"id": "msg_3", "text": None, "tokens": 0, "finish_reason": "max_tokens"},
    {"id": "msg_4", "text": "Vector databases store high-dimensional embeddings...", "tokens": 55, "finish_reason": "end_turn"},
]

# What it does: Reuses a classifier helper.
# C# equivalent: static string ClassifyFinishReason(Dictionary<string, object> response)
def classify_finish_reason(response: dict) -> str:
    reason = response.get("finish_reason", "unknown")
    if reason == "end_turn":
        return "complete"
    elif reason == "max_tokens":
        return "truncated"
    else:
        return f"unknown: {reason}"

# What it does: Runs a mini end-to-end pipeline.
def main():
    # What it does: Filters out invalid / empty responses.
    # C# equivalent: var valid = responses.Where(r => r["text"] != null).ToList();
    valid = [r for r in responses if r["text"]]
    print([r["id"] for r in valid])
    # What it does: Enriches each response with a new `status` field.
    # `{**r, ...}` copies the old dictionary and adds / overrides keys.
    # C# equivalent: var enriched = valid.Select(r => new Dictionary<string, object>(r) { ["status"] = ClassifyFinishReason(r) }).ToList();
    enriched = [{**r, "status": classify_finish_reason(r)} for r in valid]
    pprint(enriched)
    # What it does: Builds an id -> response lookup map.
    # C# equivalent: var lookup = enriched.ToDictionary(r => (string)r["id"], r => r);
    lookup = {r["id"]: r for r in enriched}
    print(list(lookup.keys()))
    # What it does: Computes the average token count of valid responses.
    # C# equivalent: var avgTokens = enriched.Average(r => (int)r["tokens"]);
    avg_tokens = sum(r["tokens"] for r in enriched) / len(enriched)
    print(f"Average tokens across valid responses: {avg_tokens:.1f}")

if __name__ == "__main__":
    main()
