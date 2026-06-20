message_dict={
    "id": "msg_1",
    "text": "Hello, how are you?",
    "sender": "user_1",
    "timestamp": "2024-06-01T12:00:00Z"
}

def basic_dict_test():
    print(len(message_dict))  # Output: 4
    print(message_dict["id"])  # Output: msg_1
    print(message_dict["text"])  # Output: Hello, how are you?
    print(message_dict.get("sender"))  # Output: user_1
    print(message_dict.get("nonexistent_key", "default_value"))  # Output: default_value
    #dict contains method
    print("id" in message_dict)  # Output: True
    print("nonexistent_key" in message_dict)  # Output: False
    #dict check value exists
    print("user_1" in message_dict.values())  # Output: True
    print("nonexistent_value" in message_dict.values())  # Output: False

def dict_slicing():
    # Dictionary Slicing (Note: Python does not support slicing dictionaries directly, but we can create a new dictionary from selected keys)
    keys_to_slice = ["id", "text"]
    sliced_dict = {k: message_dict[k] for k in keys_to_slice}  # C# equivalent: var slicedDict = new Dictionary<string, object> { { "id", message_dict["id"] }, { "text", message_dict["text"] } };
    print(sliced_dict)  # Output: {'id': 'msg_1', 'text': 'Hello, how are you?'}

def dict_comprehension():
    # Dictionary Comprehension
    uppercased_dict = {k: v.upper() if isinstance(v, str) else v for k, v in message_dict.items()}  # C# equivalent: var uppercasedDict = message_dict.ToDictionary(kv => kv.Key, kv => kv.Value is string ? kv.Value.ToUpper() : kv.Value);
    print(uppercased_dict)  # Output: {'id': 'MSG_1', 'text': 'HELLO, HOW ARE YOU?', 'sender': 'USER_1', 'timestamp': '2024-06-01T12:00:00Z'}
    # Filtering with comprehension
    filtered_dict = {k: v for k, v in message_dict.items() if isinstance(v, str) and "user" in v}  # C# equivalent: var filteredDict = message_dict.Where(kv => kv.Value is string && kv.Value.Contains("user")).ToDictionary(kv => kv.Key, kv => kv.Value);
    print(filtered_dict)  # Output: {'sender': 'user_1'}
    # Nested dictionary comprehension example
    nested_dict = {
        "message": message_dict,
        "metadata": {
            "length": len(message_dict["text"]),
            "contains_user": "user" in message_dict["sender"]
        }
    }
    print(nested_dict)  # Output: {'message': {'id': 'msg_1', 'text': 'Hello, how are you?', 'sender': 'user_1', 'timestamp': '2024-06-01T12:00:00Z'}, 'metadata': {'length': 18, 'contains_user': True}}

    #nested comprehension with filtering
    filtered_nested_dict = {
        "message": {k: v for k, v in message_dict.items() if isinstance(v, str) and "user" in v},
        "metadata": {
            "length": len(message_dict["text"]),
            "contains_user": "user" in message_dict["sender"]
        }
    }
    print(filtered_nested_dict)  # Output: {'message': {'sender': 'user_1'}, 'metadata': {'length': 18, 'contains_user': True}}



def main():
    basic_dict_test()
    dict_slicing()
    dict_comprehension()

if __name__ == "__main__":
    main()