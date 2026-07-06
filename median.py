class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1

            left_max1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            right_min1 = float('inf') if partition1 == m else nums1[partition1]
            left_max2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            right_min2 = float('inf') if partition2 == n else nums2[partition2]

            if left_max1 <= right_min2 and left_max2 <= right_min1:
                if (m + n) % 2 == 0:
                    return (max(left_max1, left_max2) + min(right_min1, right_min2)) / 2.0
                else:
                    return max(left_max1, left_max2)
            elif left_max1 > right_min2:
                right = partition1 - 1
            else:
                left = partition1 + 1


# Main function for testing
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums1 = [1, 3]
    nums2 = [2]
    result1 = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Test 1: nums1={nums1}, nums2={nums2}")
    print(f"Output: {result1}")
    print(f"Expected: 2.0\n")

    # Test case 2
    nums1 = [1, 2]
    nums2 = [3, 4]
    result2 = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Test 2: nums1={nums1}, nums2={nums2}")
    print(f"Output: {result2}")
    print(f"Expected: 2.5\n")

    # Test case 3 (edge case - empty array)
    nums1 = []
    nums2 = [1]
    result3 = solution.findMedianSortedArrays(nums1, nums2)
    print(f"Test 3: nums1={nums1}, nums2={nums2}")
    print(f"Output: {result3}")
    print(f"Expected: 1.0")