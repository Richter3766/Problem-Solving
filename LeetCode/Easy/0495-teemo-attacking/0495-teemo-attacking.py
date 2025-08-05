class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # 티모가 공격시 duration * t 만큼 독딜
        # [t, t + duration]

        # 독이 끝나기 전에 공격하면 리셋
        # 오름차순 timeSerie -> 티모가 공격한 시간
        # duration: 독 유지 시간
        
        # 애쉬가 독에 걸린 총 시간 구하기
        # 수직선 상에서 독에 걸린 시간들 병합한 후 총 길이 구하면 끝
        poisoned = [] # (시작, 끝)이 담길 배열
        for start in timeSeries:
            # 비어있으면 바로 넣기
            if not poisoned:
                time_slot = (start, start + duration)
                poisoned.append(time_slot)
                continue

            prev_start, prev_end = poisoned[-1]
            # 마지막 독 시간이 현재 공격보다 길면 독이 리셋되는 상태이므로 병합
            if prev_end >= start:
                time_slot = (prev_start, start + duration)
                poisoned[-1] = time_slot
            # 짧으면 별개이므로 따로 계산
            else:
                time_slot = (start, start + duration)
                poisoned.append(time_slot)
        
        answer = 0
        for start, end in poisoned:
            answer += end - start

        return answer