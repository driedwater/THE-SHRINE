from myMath import *
import sys

def myMain():
    nums = [*map(int, sys.argv[1].split(','))]

    print(f"The difference is:{subtraction(max(nums),min(nums))}", end=" ")
    print(f"The summation is:{add(max(nums), min(nums))}", end=" ")
    print(f"The summation of all input is:{sumTotal(nums)}", end=" ")
    print(f"The number of even numbers is:{sum([i%2==0 for i in nums])}", end=" ")
    nums = clear(nums) if min(nums) < 5 else nums
    print(f"The values in the list are:{nums}")

if __name__ == "__main__":
    myMain()

