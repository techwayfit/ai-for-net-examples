from pprint import pprint
responses = [
    {"id": "msg_1", "text": "Embeddings are dense vector representations...", "tokens": 42, "finish_reason": "end_turn"},
    {"id": "msg_2", "text": "RAG stands for Retrieval-Augmented Generation...", "tokens": 38, "finish_reason": "end_turn"},
    {"id": "msg_3", "text": None, "tokens": 0, "finish_reason": "max_tokens"},
    {"id": "msg_4", "text": "Vector databases store high-dimensional embeddings...", "tokens": 55, "finish_reason": "end_turn"},
]

def basic_tests():
    print(len(responses))  # Output: 4
    print(responses[0])  # Output: {'id': 'msg_1', 'text': 'Embeddings are dense vector representations...', 'tokens': 42, 'finish_reason': 'end_turn'}
    pprint(responses[0])
    print(responses[-1])  # Output: {'id': 'msg_4', 'text': 'Vector databases store high-dimensional embeddings...', 'tokens': 55, 'finish_reason': 'end_turn'}

def list_slicing():
    # List Slicing
    slice = responses[1:3] #c# equivalent: var slice = responses.Skip(1).Take(2).ToList();
    print(slice)  # Output: [{'id': 'msg_2', 'text': 'RAG stands for Retrieval-Augmented Generation...', 'tokens': 38, 'finish_reason': 'end_turn'}, {'id': 'msg_3', 'text': None, 'tokens': 0, 'finish_reason': 'max_tokens'}]
    slice_ids=[r["id"] for r in slice] # C# equivalent: var sliceIds = slice.Select(r => r["id"]).ToList();
    print(slice_ids)  # Output: ['msg_2', 'msg_3']

    print(responses[:2]) # C# equivalent: var firstTwo = responses.Take(2).ToList();
    print(responses[2:]) # C# equivalent: var lastTwo = responses.Skip(2).ToList();

    #using step 2
    print(responses[::2]) # C# equivalent: var everyOther = responses.Where((r, i) => i % 2 == 0).ToList();


def list_mutation():
    #List Mutation
    batch = responses.copy() # C# equivalent: var batch = responses.ToList();
    batch.append({"id": "msg_5", "text": "New response", "tokens": 10, "finish_reason": "end_turn"}) # C# equivalent: batch.Add(new Dictionary<string, object> { ... });
    print(len(batch))  # Output: 5
    print(len(responses))  # Output: Original list remains unchanged

    responses[0]["text"] = "Updated text"  # C# equivalent: responses[0]["text"] = "Updated text";
    print(batch[0]["text"])  # Output: Updated text (shared reference)
    print(responses[0]["text"])  # Output: Updated text

    removed_item= batch.pop(2) # C# equivalent: var removed = batch[2]; batch.RemoveAt(2);
    print(removed_item)  # Output: {'id': 'msg_3', '

    more_resopnses = [
        {"id": "msg_6", "text": "Another response", "tokens": 15, "finish_reason": "end_turn"},
        {"id": "msg_7", "text": "Yet another response", "tokens": 20, "finish_reason": "end_turn"},
    ]

    batch.extend(more_resopnses) # C# equivalent: batch.AddRange(more_responses);
    print(len(batch))  # Output: 6


def list_comprehension():
    # List Comprehension
    ids = [r["id"] for r in responses]  # C# equivalent: var ids = responses.Select(r => r["id"]).ToList();
    print(ids)  # Output: ['msg_1', 'msg_2', 'msg_3', 'msg_4']

    tokens = [r["tokens"] for r in responses if r["tokens"] > 0]  # C# equivalent: var tokens = responses.Where(r => r["tokens"] > 0).Select(r => r["tokens"]).ToList();
    print(tokens)  # Output: [42, 38, 55]

    #filtering and transforming in one step
    filtered_texts = [r["text"] for r in responses if r["text"] is not None]  # C# equivalent: var filteredTexts = responses.Where(r => r["text"] != null).Select(r => r["text"]).ToList();
    print(filtered_texts)  # Output: ['Embeddings are dense vector representations...', 'RAG stands for Retrieval-Augmented Generation...', 'Vector databases store high-dimensional embeddings...']







def main():
    # basic_tests()
     list_slicing()
    #list_mutation()

if __name__ == "__main__":
    main();