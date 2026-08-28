"""
Obvious O(n) space solution: Hash Set

Required: O(1) space

Note:
- Size of array is n + 1.
- Numbers in the array are bound to the range: [1, n] 
- Therefore, each number points to a valid index in the array.
- The first number in the array is at index 0. No number in the array will point to this
index since the lower bound of the range is 1.

Treat numbers in the array as ListNode,
such that an element at index 'i' with value 'v'
is equivalent to a Node(v) pointing to Node(z), where z = arr[v].
(The value of a node also points to the index in the array where the node's .next link is.)

In general, for just 2 nodes A and B to form a cycle with the given system:
[0, 2, 1] : A(2) and B(1)

Example 1: [1,2,3,2,2]
1 -> 2 -> 3 -> 2
          ↑----|

Example 2: [1,2,3,4,4]
1 -> 2 -> 3 -> 4 -> 4 -
                    |-|

Example 3: [1,2,3,1]
1 -> 2 -> 3 -> 1
     |---------|

Observe:
- The first element in the array with index 0 will never be a part of the cycle, since
lower bound is 1.
- The entrypoint to the cycle is a node at index 'i', and i is being pointed to by
at least two nodes (values). 

Therefore the index i is the duplicate.
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
          slow = 0
          fast = 0

          while True:
               slow = nums[slow]
               fast = nums[nums[fast]]

               if slow == fast:
                    break

          slow2 = 0

          while slow != slow2:
               slow2 = nums[slow2]
               slow = nums[slow]
     
          return slow
        