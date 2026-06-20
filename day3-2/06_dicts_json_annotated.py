"""06_dicts_json_annotated.py
Annotated dictionary and JSON access examples for a .NET developer.
"""
from pprint import pprint

# What it does: Creates a dictionary shaped like an LLM API JSON response.
# C# equivalent: var apiResponse = new Dictionary<string, object> { ... };
api_response = {
    "id": "msg_abc123",
    "type": "message",
    "role": "assistant",
    "content": [{"type": "text", "text": "Here's the analysis..."}],
    "model": "claude-3-5-sonnet-20241022",
    "stop_reason": "end_turn",
    "usage": {"input_tokens": 150, "output_tokens": 320},
}

# What it does: Safely extracts a nested text value.
# C# equivalent: static string? ExtractTextSafe(Dictionary<string, object> response)
def extract_text_safe(response: dict):
    # What it does: Gets `content` if present, otherwise uses an empty list.
    # C# equivalent: var content = response.ContainsKey("content") ? response["content"] : new List<object>();
    content = response.get("content") or []
    # What it does: Returns None early if content is empty.
    # C# equivalent: if (!content.Any()) return null;
    if not content:
        return None
    # What it does: Gets the first item in the list.
    # C# equivalent: var first = content[0];
    first = content[0]
    # What it does: Ensures the first item is a dictionary.
    # C# equivalent: if (first is not Dictionary<string, object>) return null;
    if not isinstance(first, dict):
        return None
    # What it does: Returns the nested text value if present.
    # C# equivalent: return first.ContainsKey("text") ? (string?)first["text"] : null;
    return first.get("text")

# What it does: Shows required vs optional field access.
def example_required_vs_optional():
    # What it does: Required access using square brackets; this fails if key is missing.
    # C# equivalent: var model = (string)apiResponse["model"];
    model = api_response["model"]
    # What it does: Optional access with a default fallback.
    # C# equivalent: var stopReason = apiResponse.ContainsKey("stop_reason") ? (string)apiResponse["stop_reason"] : "unknown";
    stop_reason = api_response.get("stop_reason", "unknown")
    print("Required field:", model)
    print("Optional field via get():", stop_reason)

# What it does: Shows safe nested access.
def example_nested_access():
    # What it does: Reads nested token fields safely even if usage is missing.
    # C# equivalent: var inputTokens = apiResponse.ContainsKey("usage") ? (int)((Dictionary<string, object>)apiResponse["usage"])["input_tokens"] : 0;
    input_tokens = api_response.get("usage", {}).get("input_tokens", 0)
    output_tokens = api_response.get("usage", {}).get("output_tokens", 0)
    print(f"Input={input_tokens}, Output={output_tokens}")

# What it does: Shows defensive parsing against malformed structures.
def example_defensive_parsing():
    # What it does: Creates three malformed test payloads.
    # C# equivalent: var broken = new List<Dictionary<string, object>> { ... };
    broken = [{"content": []}, {"content": ["not-a-dict"]}, {}]
    print("Good:", extract_text_safe(api_response))
    # What it does: Enumerates broken payloads starting at index 1.
    # C# equivalent: use a for loop or a counter variable in foreach.
    for i, item in enumerate(broken, start=1):
        print(f"Broken {i}:", extract_text_safe(item))

# What it does: Shows grouping via setdefault.
def example_setdefault():
    # What it does: Starts with an empty dictionary.
    # C# equivalent: var labelsByDoc = new Dictionary<string, List<string>>();
    labels_by_doc = {}
    # What it does: Stores pairs of document id and label.
    # C# equivalent: var pairs = new List<(string, string)> { ... };
    pairs = [("doc_1", "rag"), ("doc_1", "chunking"), ("doc_2", "embeddings")]
    # What it does: Iterates over tuple pairs and unpacks them.
    # C# equivalent: foreach (var (docId, label) in pairs)
    for doc_id, label in pairs:
        # What it does: Creates an empty list for the key if missing, then appends the label.
        # C# equivalent: if (!labelsByDoc.ContainsKey(docId)) labelsByDoc[docId] = new List<string>(); labelsByDoc[docId].Add(label);
        labels_by_doc.setdefault(doc_id, []).append(label)
    pprint(labels_by_doc)

# What it does: Main runner.
def main():
    example_required_vs_optional()
    example_nested_access()
    example_defensive_parsing()
    example_setdefault()

if __name__ == "__main__":
    main()
