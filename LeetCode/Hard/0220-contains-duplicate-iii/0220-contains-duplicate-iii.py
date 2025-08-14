class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        # 슬라이딩 윈도우와 버킷 해싱의 조합
        # indexDiff 만큼 윈도우 크기 유지
        # valueDiff + 1 만큼의 크기로 구간을 나누어 버킷으로 사용
        # 같은 버킷에 들어오는 값이 있으면 True
        # 인접한 버킷의 값이 있으면 값 비교해보기

        buckets = {}
        bucket_size = valueDiff + 1
        left = 0

        for i, num in enumerate(nums):
            if i > indexDiff:
                bucket = nums[i - indexDiff - 1] // bucket_size
                del buckets[bucket]
                left += 1

            bucket = num // bucket_size
            if bucket in buckets:
                return True
            
            buckets[bucket] = num
            if (bucket - 1) in buckets:
                if abs(num - buckets[bucket - 1]) <= valueDiff:
                    return True
            if (bucket + 1) in buckets:
                if abs(num - buckets[bucket + 1]) <= valueDiff:
                    return True
        return False