# https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals):
        intervals.sort()
        stack = [intervals[0]]

        for i in range(1,len(intervals)):
            currIntvl = {
                'start': intervals[i][0],
                'end': intervals[i][1]
            }

            lastIntvl = {
                'start': stack[-1][0],
                'end': stack[-1][1]
            }

            if currIntvl['start'] <= lastIntvl['end'] and currIntvl['end'] > lastIntvl['end']: 
                stack[-1][1] = currIntvl['end']
            elif currIntvl['start'] > lastIntvl['end']: 
                stack.append(intervals[i])

        return stack