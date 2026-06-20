
def build_prompt(task: str, language: str) -> str:
	"""Named parameter example."""
	return f"Write {language} code for: {task}"


def call_llm(prompt: str, model: str = "gpt-4.1-mini") -> str:
	"""Default parameter example."""
	return f"Calling model={model} with prompt='{prompt}'"


def total_tokens(*token_counts: int) -> int: # C# Equivalent: int total_tokens(params int[] token_counts)
	"""*args example: accepts any number of positional values."""
	return sum(token_counts)


def log_details(**metadata) -> None: # C# Equivalent: void log_details(params Dictionary<string, object> metadata)
	"""**kwargs example: accepts any number of named values."""
	print("Inference metadata:")
	for key, value in metadata.items():
		print(f"- {key}: {value}")


# 1) Named parameter
print(build_prompt(language="Python", task="a function to parse JSON logs"))

# 2) Default parameter
print(call_llm("Explain decorators with examples"))
print(call_llm("Generate unit tests for a Flask API", model="gpt-4.1"))

# 3) *args
print(f"Total tokens (120, 340, 560): {total_tokens(120, 340, 560)}")
print(f"Total tokens (75): {total_tokens(75)}")

# 4) **kwargs
log_details(
	model="gpt-4.1-mini",
	temperature=0.2,
	latency_ms=430,
	prompt_tokens=210,
	completion_tokens=120,
)

