import numpy as np

nums = np.loadtxt('input')
set_nums = set(nums);
for i in nums:
    if (2020-i) in set_nums:
        print(f'{i*(2020-i)} is the answer')
        break
