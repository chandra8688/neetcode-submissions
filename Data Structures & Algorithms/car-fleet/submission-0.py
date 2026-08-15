class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=sorted(zip(position,speed),key=lambda x:x[0],reverse=True)
        fleet_times=[]
        for pos,spd in cars:
            time=(target-pos)/spd
            if not fleet_times or time>fleet_times[-1]:
                fleet_times.append(time)
        return len(fleet_times)