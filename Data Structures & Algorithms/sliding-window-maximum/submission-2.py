"""
nums = [1,2,1,0,4,2,6], k = 3

Since we are aiming for O(n) time, we need a way to tell the maximum in a
window of size '3' without comparing all the elements in the window.
The time complexity for that would be O(k * (n - k)), since we can have only
(n - k + 1) windows.

So, let's look at the first two possible windows:
[1,2,1] and [2,1,0].

If we had two precomputed slices of the same size 3,
corresponding to each of the two windows, and we knew that the element at
a certain index of each of those slices will give us the max of the actual
windows, we would be happy.

So, what could those 2 slices look like? If we kept taking the max, while
traversing from the left, that could work. So it would be

[1,2,2] and [2,2,2]

But these two windows are actually not discrete. In the context of the
input list, they overlap. [1,2,1,0]
So we cannot get this in a single pass yet.

So let's break up the input list into continuous non-overlapping windows.

[[1,2,1], [0,4,2], [6]]

Now we apply the same idea of getting max by traversing left for each of these
windows.

[[1,2,2], [0,4,4], [6]]

So taking the last element from each of these windows would give us the max
for these 3 windows. But that last one is not even a window as per the problem.
It has to be of size 3. So a valid window with the last element, and in fact,
the only valid window would be [4,4,6]. What if we kept extending this
split to the left for the input list? There is a symmetry.

[[1], [2,1,0], [4,2,6]]

So now we have 4 possible windows of size 3 from the input list. But
there is one more for this input - [1,0,4]. So clearly a naive split is not
working for us.

Let's look at this remaining window, [1,0,4] and see what it is telling us.
If we stuck to our first split 
[[1,2,1], [0,4,2], [6]]
this belongs to the first and second splits both.
[1] to the first and [0,4] to the second.

Given we have our left max computed
[[1,2,2], [0,4,4], [6]]
we can see that the max for [0,4] is 4 but the max for [1] is clearly not 2!
2 is not even in the window bounds of [1,0,4].

But what if we ask the question to the split [1,0,4] given it knows about
our input split, i.e. [[1,2,1], [0,4,2], [6]]:
To 4: Hey, what is your max from the start of the current split?
To 1: What is your max from the end of the current split?

4 has an answer from out left max: 4!
1 has no answer yet. So we need a rolling max from the other end of the input!

leftmax: [[1,2,2], [0,4,4], [6]]
rightmax: [[1], [2,1,0], [6,6,6]]

Now 1 can safely answer: "It is me! I am the max!"

Now the window [1,0,4] has the answer to the question we asked it.
It's max is the max(leftmax at 4, rightmax at 1)

Let's assume the generalization is max(leftmax at right bound, rightmax at left bound)

Cool, so does this hold for non-overlapping windows from our input split?
[1,2,2] -> max(2, 1) - yes
[0,4,2] -> max(4, 2) - yes

Great, now the rest is to just flatten the explicit splits and work with index
arithmetic with
leftmax: [1,2,2,0,4,4,6]
rightmax: [1,2,1,0,6,6,6]
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        leftmax = [0] * len(nums)
        rightmax = [0] * len(nums)

        n = len(nums)

        output = []

        for i in range(n):
            if i == 0 or i % k == 0:
                leftmax[i] = nums[i]
            else:
                leftmax[i] = max(nums[i], leftmax[i-1]) # i==0 check prevents out of bounds
            
            j = n - 1 - i
            if j == n - 1 or j % k == 0:
                rightmax[j] = nums[j]
            else:
                rightmax[j] = max(nums[j], rightmax[j + 1])
            
        
        for i in range(0, n-k+1):
            output.append(max(rightmax[i], leftmax[i+k-1]))
        
        return output
        

