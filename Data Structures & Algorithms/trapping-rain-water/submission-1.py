class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = []
        max_right = []
        curr_height_left = 0
        curr_height_right = 0
        min_lr = []
        total = 0

        for i in height:
            max_left.append(curr_height_left)
            if i > curr_height_left:
                curr_height_left = i
        # print(max_left)

        for i in reversed(height):
            max_right.append(curr_height_right)
            if i > curr_height_right:
                curr_height_right = i
        max_right = max_right[::-1]
        # print(max_right)

        for i in range(len(max_left)):
            min_lr.append(min(max_left[i], max_right[i]))
        # print(min_lr)

        for i in range(len(min_lr)):
            if min_lr[i] - height[i] < 0:
                total+=0
            else:
                total+=min_lr[i]-height[i]
        return total

        