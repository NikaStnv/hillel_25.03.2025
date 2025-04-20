txt_1 = input("Enter a text: ")
txt_2 = input("2-nd index of which text element to find?  ")

def second_index(text: str, some_str: str) -> int:
    if text.count(some_str) < 2:
        return None
    else:
        return text.find(some_str, text.find(some_str) + 1)


result = second_index(txt_1,txt_2)
print(result)

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
