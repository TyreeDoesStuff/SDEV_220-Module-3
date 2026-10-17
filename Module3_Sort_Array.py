
# Name: Tyree Callahan
# File: Module3_Sort_Array.py
# Sort an array containing 0s, 1s, and 2s.

class Solution:
    def sort012(self, arr):
        low = 0
        mid = 0
        high = len(arr) - 1

        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

        return arr


numbers = [2, 0, 1, 2, 1, 0]

solution = Solution()
print(solution.sort012(numbers))
