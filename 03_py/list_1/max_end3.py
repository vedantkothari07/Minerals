def max_end3(nums):
  a = 0;
  if (nums[0] > nums[len(nums) - 1]):
    a = nums[0];
  else:
    a = nums[len(nums) - 1];
  nums[0] = a;
  nums[1] = a;
  nums[2] = a;
  return nums;