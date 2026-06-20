message_set = {"msg_1", "msg_2", "msg_3"}
another_set = {"msg_2", "msg_3", "msg_4", "msg_4"}
message_hash_set = set(["msg_1", "msg_2", "msg_3"])  # C# equivalent: var messageHashSet = new HashSet<string> { "msg_1", "msg_2", "msg_3" };


def basic_set_test():
    print(len(message_set))  # Output: 3
    print(len(another_set))  # Output: 3
    print("msg_1" in message_set)  # Output: True
    print("msg_4" in message_set)  # Output: False

def set_operations():
    another_set = {"msg_2", "msg_3", "msg_4"}
    print(message_set.union(another_set))  # Output: {'msg_1', 'msg_2', 'msg_3', 'msg_4'}
    print(message_set.intersection(another_set))  # Output: {'msg_2', 'msg_3'}
    print(message_set.difference(another_set))  # Output: {'msg_1'}
    print(message_set.symmetric_difference(another_set))  # Output: {'msg_1', 'msg_4'}


def set_operations_2():
    another_set = {"msg_2", "msg_3", "msg_4"}
    print(message_set | another_set)  # Output: {'msg_1', 'msg_2', 'msg_3', 'msg_4'}
    print(message_set & another_set)  # Output: {'msg_2', 'msg_3'}
    print(message_set - another_set)  # Output: {'msg_1'}
    print(message_set ^ another_set)  # Output: {'msg_1', 'msg_4'}

def main():
    basic_set_test()
    set_operations()
    set_operations_2()

if __name__ == "__main__":
    main()  