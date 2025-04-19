def second_index(text: str, some_str: str) -> int:
    if text.count(some_str) < 2:
        return None
    else:
        x = 0
        sec_index = 0
        while x < len(text):
            sec_index = text.find(some_str, (x-1))
            x += 1
        return sec_index

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
