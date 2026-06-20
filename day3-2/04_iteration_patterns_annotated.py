"""04_iteration_patterns_annotated.py
Annotated zip and dict iteration examples for a .NET developer.
"""

# What it does: Defines a function that pairs values from two lists.
# C# equivalent: static void ExampleZip() { ... }
def example_zip():
    # What it does: Creates a list of prompts.
    # C# equivalent: var prompts = new List<string> { ... };
    prompts = ["What is RAG?", "Explain embeddings", "What is a token?"]
    # What it does: Creates a second list aligned by position.
    # C# equivalent: var outputs = new List<string> { ... };
    outputs = ["RAG is...", "Embeddings are...", "A token is..."]
    # What it does: Iterates over both lists in parallel.
    # C# equivalent: foreach (var pair in prompts.Zip(outputs))
    for prompt, output in zip(prompts, outputs):
        print(f"Q: {prompt}\nA: {output}\n")

# What it does: Shows zip behavior when list lengths differ.
# C# equivalent: static void ExampleZipMismatch() { ... }
def example_zip_mismatch():
    prompts = ["Q1", "Q2", "Q3"]
    outputs = ["A1", "A2"]
    # What it does: zip stops when the shorter iterable ends.
    # C# equivalent: LINQ Zip also stops at the shorter sequence.
    for prompt, output in zip(prompts, outputs):
        print(prompt, output)

# What it does: Demonstrates iterating through a dict's key/value pairs.
# C# equivalent: static void ExampleDictItems() { ... }
def example_dict_items():
    # What it does: Creates a dictionary with nested usage metadata.
    # C# equivalent: var responseMeta = new Dictionary<string, object> { ... };
    response_meta = {"model": "claude-3-5-sonnet", "usage": {"input_tokens": 100, "output_tokens": 250}}
    # What it does: Iterates over dictionary items as key/value pairs.
    # C# equivalent: foreach (var kvp in responseMeta)
    for key, value in response_meta.items():
        print(f"{key}: {value}")

# What it does: Main runner.
# C# equivalent: static void MainLogic() { ... }
def main():
    example_zip()
    example_zip_mismatch()
    example_dict_items()

if __name__ == "__main__":
    main()
