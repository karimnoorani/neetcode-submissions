class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        count = {i: 0 for i in range(n)} # keeping count of meetings for each room
        upcoming = [[s, e-s] for s, e in meetings] # heap keeping track of upcoming meetings
        minAvailMeeting = [i for i in range(n)] # heap to get the next meeting room
        inProgress = [] # endTime, meetingRoom
        heapq.heapify(upcoming)
        heapq.heapify(minAvailMeeting)
        
        while upcoming:
            while inProgress and inProgress[0][0] <= upcoming[0][0]:
                t, meetingRoom = heapq.heappop(inProgress)
                heapq.heappush(minAvailMeeting, meetingRoom)
            if len(inProgress) < n:
                delay = 0
                meetingRoom = heapq.heappop(minAvailMeeting)
            else:
                t, meetingRoom = heapq.heappop(inProgress)
                delay = t-upcoming[0][0]

            newMeeting = heapq.heappop(upcoming) # start, duration
            heapq.heappush(inProgress, [delay+newMeeting[0]+newMeeting[1], meetingRoom])
            count[meetingRoom] += 1
        max_value = max(count.values())
        keys_with_max_value = [key for key, value in count.items() if value == max_value]
        return keys_with_max_value[0]