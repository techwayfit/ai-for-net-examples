messages_tuple= ("Hello", "How are you?", "Goodbye")

def basic_tuple_test():
    print(len(messages_tuple))  # Output: 3
    print(messages_tuple[0])  # Output: Hello
    print(messages_tuple[-1])  # Output: Goodbye

def tuple_slicing():
    # Tuple Slicing
    slice = messages_tuple[1:3]  # C# equivalent: var slice = messages_tuple.Skip(1).Take(2).ToArray();
    print(slice)  # Output: ('How are you?', 'Goodbye')
    slice_ids = [r for r in slice]  # C# equivalent: var sliceIds = slice.ToList();
    print(slice_ids)  # Output: ['How are you?', 'Goodbye']

    print(messages_tuple[:2])  # C# equivalent: var firstTwo = messages_tuple.Take(2).ToArray();
    print(messages_tuple[2:])  # C# equivalent: var lastTwo = messages_tuple.Skip(2).ToArray();

def tuple_comprehension():
    # Tuple Comprehension (Note: Python does not have tuple comprehensions, but we can create a tuple from a generator expression)
    ids = tuple(r for r in messages_tuple)  # C# equivalent: var ids = messages_tuple.ToArray();
    print(ids)  # Output: ('Hello', 'How are you?', 'Goodbye')

    filtered_texts = tuple(r for r in messages_tuple if r is not None)  # C# equivalent: var filteredTexts = messages_tuple.Where(r => r != null).ToArray();
    print(filtered_texts)  # Output: ('Hello', 'How are you?', 'Goodbye')

    #yuple to list conversion
    list_from_tuple = list(messages_tuple)  # C# equivalent: var listFromTuple = messages_tuple.ToList();
    print(list_from_tuple)  # Output: ['Hello', 'How are you?', 'Goodbye']

    #list to tuple conversion
    tuple_from_list = tuple(list_from_tuple)  # C# equivalent: var tupleFromList = listFromTuple.ToArray();
    print(tuple_from_list)  # Output: ('Hello', 'How are you?', 'Goodbye')

    #no add/pop/extend methods for tuples, since they are immutable


def main():
    basic_tuple_test()
    tuple_slicing()
    tuple_comprehension()

if __name__ == "__main__":
    main()