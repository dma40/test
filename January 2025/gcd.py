def gcd(x: int, y: int) -> int:
    """
    Precondition: x and y are positive integers
    """
    if x % y == 0:
        return y
    
    if y % x == 0:
        return x
    
    else:
        if x > y:
            return gcd(x, x - y)
        else:
            return gcd(y - x, x)
        

def gcd_of_list(nums: list[int]) -> int:
    """
    Precondition: nums is a list of length greater or equal to 2
    and contains only positive integers.
    """
    if len(nums) == 2:
        return gcd(nums[0], nums[1])
    
    else:
        x1 = nums.pop()
        x2 = nums.pop()
        gcd = gcd(x1, x2)

        nums.append(gcd)
        return gcd_of_list(nums)
    

def list_to_int(digits: list[int]) -> int:
    """
    Precondition: digits is a valid list of distinct digits from 0-9
    """
    result = 0
    for i in range(0, len(digits)):
        result += digits[i] * (10 ** (9 - i))
    return result

def sudoku_grid_to_list(digits: list[list[int]]) -> list[int]:
    result = []
    for i in range(0, len(digits)):
        result.append(list_to_int(digits[i]))
    return result

