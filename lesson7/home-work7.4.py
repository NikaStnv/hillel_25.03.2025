def common_elements(start: int = 0, stop: int = 100, a_step: int = 3, b_step: int = 5) -> set:
        a_set = set(range(start, stop, a_step))
        b_set = set(range(start, stop, b_step))
        return  a_set.intersection(b_set)

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}


