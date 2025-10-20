class Solution(object):
    def largestAltitude(self, gain):
        altitude = 0
        max_altitude = 0

        for num in gain:
            altitude += num
            if altitude > max_altitude:
                max_altitude = altitude
        return max_altitude

        #T:O(n), S:O(1)