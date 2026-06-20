"""03_conditionals_loops_annotated.py
Annotated conditionals and loop examples for a .NET developer.
"""

# What it does: Stores example records in a list of dictionaries.
# C# equivalent: var responses = new List<Dictionary<string, object>> { ... };
responses = [
    {"id": "msg_1", "text": "Embeddings are dense vector representations...", "tokens": 42, "finish_reason": "end_turn"},
    {"id": "msg_2", "text": "RAG stands for Retrieval-Augmented Generation...", "tokens": 38, "finish_reason": "end_turn"},
    {"id": "msg_3", "text": None, "tokens": 0, "finish_reason": "max_tokens"},
    {"id": "msg_4", "text": "Vector databases store high-dimensional embeddings...", "tokens": 55, "finish_reason": "end_turn"},
]

# What it does: Defines a helper function that classifies the finish reason.
# C# equivalent: static string ClassifyFinishReason(Dictionary<string, object> response)
def classify_finish_reason(response: dict) -> str:
    # What it does: Safely reads the finish_reason field.
    # If the key is missing, it falls back to "unknown".
    # C# equivalent: var reason = response.ContainsKey("finish_reason") ? (string)response["finish_reason"] : "unknown";
    reason = response.get("finish_reason", "unknown")
    # What it does: First branch of conditional logic.
    # C# equivalent: if (reason == "end_turn")
    if reason == "end_turn":
        # What it does: Returns a string.
        # C# equivalent: return "complete";
        return "complete"
    # What it does: Checks the next condition.
    # C# equivalent: else if (reason == "max_tokens")
    elif reason == "max_tokens":
        return "truncated"
    # What it does: Checks another condition.
    # C# equivalent: else if (reason == "stop_sequence")
    elif reason == "stop_sequence":
        return "stopped"
    # What it does: Handles everything else.
    # C# equivalent: else
    else:
        # What it does: Builds a formatted string.
        # C# equivalent: return $"unknown: {reason}";
        return f"unknown: {reason}"

# What it does: Defines a function to iterate over responses and classify each one.
# C# equivalent: static void ExampleConditionals() { ... }
def example_conditionals():
    print()
    print("--- Conditionals ---")
    # What it does: Iterates directly over items in the list.
    # C# equivalent: foreach (var r in responses)
    for r in responses:
        print(f"{r['id']}: {classify_finish_reason(r)}")

# What it does: Defines a function to compare loop styles.
# C# equivalent: static void ExampleLoops() { ... }
def example_loops():
    print()
    print("--- range(len(...)) ---")
    # What it does: Loops over integer indexes from 0 to len(responses)-1.
    # C# equivalent: for (int i = 0; i < responses.Count; i++)
    for i in range(len(responses)):
        print(i, responses[i]["id"])
    print()
    print("--- for-each ---")
    # What it does: Iterates directly over the items.
    # C# equivalent: foreach (var r in responses)
    for r in responses:
        print(r["id"])
    print()
    print("--- enumerate ---")
    # What it does: Iterates with both index and value.
    # C# equivalent: foreach with manual counter, or a for loop if index is needed.
    for i, r in enumerate(responses):
        print(f"{i}: {r['id']}")

# What it does: Shows early exit and skipping items.
# C# equivalent: static void ExampleBreakContinue() { ... }
def example_break_continue():
    print()
    print("--- break / continue ---")
    # What it does: Iterates until it finds the first truncated response.
    # C# equivalent: foreach (var r in responses)
    for r in responses:
        # What it does: Runs the branch only when the condition matches.
        # C# equivalent: if ((string)r["finish_reason"] == "max_tokens")
        if r["finish_reason"] == "max_tokens":
            print(f"Warning: {r['id']} was truncated")
            # What it does: Exits the loop immediately.
            # C# equivalent: break;
            break
    # What it does: Starts a second loop over the same list.
    # C# equivalent: foreach (var r in responses)
    for r in responses:
        # What it does: Skips records with missing text.
        # C# equivalent: if (r["text"] == null) continue;
        if not r["text"]:
            # What it does: Jumps to the next iteration.
            # C# equivalent: continue;
            continue
        print("Processed:", r["id"])

# What it does: Defines the file's main function.
# C# equivalent: static void MainLogic() { ... }
def main():
    example_conditionals()
    example_loops()
    example_break_continue()

# What it does: Standard Python entry-point guard.
if __name__ == "__main__":
    main()
