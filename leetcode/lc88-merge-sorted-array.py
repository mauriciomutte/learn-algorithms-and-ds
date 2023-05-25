# Link: https://leetcode.com/problems/merge-sorted-array/

class Solution:
  def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    array_and_m_difference = m - len(nums1)
    if array_and_m_difference < 0:
      del nums1[array_and_m_difference:]
    nums1.extend(nums2)
    nums1.sort()
