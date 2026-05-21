class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = [i for i in range(n)]
        meeting_heap = []
        for start, end in meetings:
            heapq.heappush(meeting_heap, [start, end-start])
        meeting_count = {i: 0 for i in range(n)}
        in_progress_heap = [] # [end time, room ]
        heapq.heapify(rooms)
        time = 0
        
        while meeting_heap:
            if time < meeting_heap[0][0]:
                time = meeting_heap[0][0]

            while in_progress_heap and in_progress_heap[0][0] <= time:
                _, room = heapq.heappop(in_progress_heap)
                heapq.heappush(rooms, room)
            
            while rooms and meeting_heap and meeting_heap[0][0] <= time:
                room = heapq.heappop(rooms)
                _, duration = heapq.heappop(meeting_heap)
                heapq.heappush(in_progress_heap, [time+duration, room])
                meeting_count[room] += 1
            
            time += 1
        
        maxMeetingRoom = None
        maxMeetingCount = 0

        for room in range(n):
            if meeting_count[room] > maxMeetingCount:
                maxMeetingRoom = room
                maxMeetingCount = meeting_count[room]
        
        return maxMeetingRoom