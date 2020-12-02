import numpy as np

nums = np.loadtxt('input')
set_nums = set(nums);

for i in nums:
    remainder = 2020-i;
    for j in nums:
        if (remainder-j) in set_nums:
            print(f'{i*j*(remainder-j)} is the answer')
            break
