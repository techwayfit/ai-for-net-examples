"""02_tuples_annotated.py
Annotated tuple examples for a .NET developer.
"""

# What it does: Defines a function.
# C# equivalent: static void ExampleTupleBasics() { ... }
def example_tuple_basics():
    print()
    print("--- Tuple basics ---")
    # What it does: Creates a tuple with three ordered values.
    # Python tuples are immutable.
    # C# equivalent: var modelInfo = ("claude-3-5-sonnet", 0.2, 4096);
    model_info = ("claude-3-5-sonnet", 0.2, 4096)
    # What it does: Unpacks the tuple into three variables.
    # C# equivalent: var (model, temperature, maxTokens) = modelInfo;
    model, temperature, max_tokens = model_info
    print("Tuple:", model_info)
    print("Model:", model)
    print("Temperature:", temperature)
    print("Max tokens:", max_tokens)

# What it does: Defines a function for single-item tuple syntax.
# C# equivalent: static void ExampleEmbeddingShape() { ... }
def example_embedding_shape():
    print()
    print("--- Embedding shape ---")
    # What it does: Creates a single-element tuple.
    # The trailing comma is required in Python.
    # C# equivalent: no exact single-item tuple syntax is commonly used; usually just `int embeddingDimensions = 1536;`
    embedding_shape = (1536,)
    print("Shape tuple:", embedding_shape)

# What it does: Defines a function showing multiple return values.
# C# equivalent: static void ExampleReturnMultipleValues() { ... }
def example_return_multiple_values():
    print()
    print("--- Returning multiple values ---")
    # What it does: Defines a nested function.
    # C# equivalent: local function inside a method.
    def token_summary(input_tokens, output_tokens):
        # What it does: Adds the two token counts.
        # C# equivalent: var total = inputTokens + outputTokens;
        total = input_tokens + output_tokens
        # What it does: Returns multiple values as a tuple.
        # C# equivalent: return (inputTokens, outputTokens, total);
        return input_tokens, output_tokens, total
    # What it does: Calls the function and unpacks the returned tuple.
    # C# equivalent: var (inputT, outputT, total) = TokenSummary(150, 320);
    input_t, output_t, total = token_summary(150, 320)
    print(f"Input={input_t}, Output={output_t}, Total={total}")

# What it does: Defines the main driver function.
# C# equivalent: static void MainLogic() { ... }
def main():
    example_tuple_basics()
    example_embedding_shape()
    example_return_multiple_values()

# What it does: Standard Python entry-point guard.
# C# equivalent: not usually needed because Main is the entry point.
if __name__ == "__main__":
    main()
