from timeit import repeat
from functools import lru_cache


@lru_cache(maxsize=128)
def steps_to(step):
    if step == 1:
        # You can reach the first step with only a single step
        # from the floor.
        return 1

    elif step == 2:
        # You can reach the second step by jumping from the
        # floor with a single two-step hop or by jumping a single
        # step a couple of times.
        return 2

    elif step == 3:
        # You can reach the third step using four possible
        # combinations:
        # 1. Jumping all the way from the floor
        # 2. Jumping two steps, then one
        # 3. Jumping one step, then two
        # 4. Jumping one step three times
        return 4
    else:
        # You can reach your current step from three different places:
        # 1. From three steps down
        # 2. From two steps down
        # 2. From one step down

        # If you add up the number of ways of getting to those
        # those three positions, then you should have your solution.
        return (
                steps_to(step - 3)
                + steps_to(step - 2)
                + steps_to(step - 1)
        )


print(steps_to(30))
setup_code = "from __main__ import steps_to"
stmt = "steps_to(30)"
times = repeat(setup=setup_code, stmt=stmt, repeat=1, number=5)
print(f"Minimum execution time: {min(times)}")
