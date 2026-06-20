"""01_lists_annotated.py
This file adds inline learning comments for a .NET developer.
Only the non-print / non-pprint lines are explained.
"""
from pprint import pprint

# What it does: Creates a Python list named `responses`.
# In AI code, this often stores a batch of LLM outputs or retrieved records.
# C# equivalent: var responses = new List<Dictionary<string, object>> { ... };
responses = [
    # What it does: Creates a Python dict representing one response record.
    # C# equivalent: new Dictionary<string, object> { ["id"] = "msg_1", ... }
    {"id": "msg_1", "text": "Embeddings are dense vector representations...", "tokens": 42, "finish_reason": "end_turn"},
    {"id": "msg_2", "text": "RAG stands for Retrieval-Augmented Generation...", "tokens": 38, "finish_reason": "end_turn"},
    # What it does: Uses None for a missing value.
    # C# equivalent: null
    {"id": "msg_3", "text": None, "tokens": 0, "finish_reason": "max_tokens"},
    {"id": "msg_4", "text": "Vector databases store high-dimensional embeddings...", "tokens": 55, "finish_reason": "end_turn"},
]

# What it does: Defines a function.
# C# equivalent: static void ExampleListBasics() { ... }
def example_list_basics():
    print()
    print("--- List basics ---")
    print("Length:", len(responses))
    print("First item:")
    pprint(responses[0])
    print("Last item:")
    pprint(responses[-1])
    print("Slice [1:3]:")
    pprint(responses[1:3])

# What it does: Defines a second function for mutation examples.
# C# equivalent: static void ExampleListMutation() { ... }
def example_list_mutation():
    print()
    print("--- List mutation ---")
    # What it does: Makes a shallow copy of the list.
    # The outer list is copied, but inner dict objects are still shared.
    # C# equivalent: var batch = responses.ToList();
    batch = responses.copy()
    # What it does: Appends a new item to the end of the list.
    # C# equivalent: batch.Add(new Dictionary<string, object> { ... });
    batch.append({"id": "msg_5", "text": "New response", "tokens": 10, "finish_reason": "end_turn"})
    print("After append:", len(batch))
    # What it does: Removes and returns the item at index 2.
    # C# equivalent: var removed = batch[2]; batch.RemoveAt(2);
    removed = batch.pop(2)
    print("Removed:", removed["id"])
    print("After pop:", len(batch))

# What it does: Demonstrates slicing and copy semantics.
# C# equivalent: static void ExampleSlicingAndCopying() { ... }
def example_slicing_and_copying():
    print()
    print("--- Slicing and copying ---")
    # What it does: Takes the first two items using slicing.
    # C# equivalent: var firstTwo = responses.Take(2).ToList();
    first_two = responses[:2]
    # What it does: Takes all items from index 2 onwards.
    # C# equivalent: var tail = responses.Skip(2).ToList();
    tail = responses[2:]
    print("First two IDs:", [r["id"] for r in first_two])
    print("Tail IDs:", [r["id"] for r in tail])
    # What it does: Creates another variable pointing to the same list object.
    # No copy happens here.
    # C# equivalent: var alias = responses;
    alias = responses
    # What it does: Creates a shallow copy of the list.
    # C# equivalent: var copied = responses.ToList();
    copied = responses.copy()
    # What it does: Appends through the alias reference.
    # Since alias and responses point to the same list, both reflect the change.
    # C# equivalent: alias.Add(...);
    alias.append({"id": "msg_alias", "text": "Added through alias", "tokens": 5, "finish_reason": "end_turn"})
    print("Original changed via alias?", len(responses))
    print("Copied list length remains:", len(copied))
    # What it does: Removes the last item to clean up the shared list.
    # C# equivalent: responses.RemoveAt(responses.Count - 1);
    responses.pop()

# What it does: Shows list comprehension filtering.
# C# equivalent: static void ExampleFilterNonNull() { ... }
def example_filter_non_null():
    print()
    print("--- Filter non-null texts ---")
    # What it does: Builds a new list containing only responses whose text is not None.
    # C# equivalent: var valid = responses.Where(r => r["text"] != null).ToList();
    valid = [r for r in responses if r["text"] is not None]
    print([r["id"] for r in valid])

# What it does: Defines the file's main orchestration function.
# C# equivalent: static void MainLogic() { ... }
def main():
    # What it does: Calls the example functions in sequence.
    # C# equivalent: ExampleListBasics(); ExampleListMutation(); ...
    example_list_basics()
    example_list_mutation()
    example_slicing_and_copying()
    example_filter_non_null()

# What it does: Ensures main() runs only when the file is executed directly.
# C# equivalent: Main() is the entry point, so C# doesn't usually need this pattern.
if __name__ == "__main__":
    # What it does: Executes the main workflow.
    # C# equivalent: Main();
    main()
