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

            lastIntvlIdx = len(stack) - 1
            lastIntvl = {
                'start': stack[lastIntvlIdx][0],
                'end': stack[lastIntvlIdx][1]
            }

            if currIntvl['start'] <= lastIntvl['end'] and currIntvl['end'] > lastIntvl['end']: 
                stack[lastIntvlIdx][1] = currIntvl['end']
            elif currIntvl['start'] <= lastIntvl['end'] and currIntvl['end'] <= lastIntvl['end']: 
                continue
            elif currIntvl['start'] > lastIntvl['end']: 
                stack.append(intervals[i])

        return stack