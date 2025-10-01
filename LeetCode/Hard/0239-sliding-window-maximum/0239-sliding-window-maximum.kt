class Solution {
    fun maxSlidingWindow(nums: IntArray, k: Int): IntArray {
        // 최대 힙과 카운트를 관리
        // 힙은 lazy removal로 삭제는 나중에 진행하도록 함
        // 이는 힙에서 특정 값을 바로 삭제하는 것이 좋지 않기 때문
        
        // lazy removal의 기준은 
        // 윈도우 내 값을 카운터로 각 값당 개수를 유지하여
        // 힙의 peek의 수가 0이 되는 경우이며,
        // counter[peek]이 0이 아닐 때까지 poll도록 함.
        
        val heap = PriorityQueue<Int>() // 최대 힙으로 사용
        val counter = HashMap<Int, Int>()   
        val answer = mutableListOf<Int>()
        // 초기 윈도우 설정
        for (i in 0..<k){
            val num = nums[i]
            counter[num] = counter.getOrDefault(num, 0) + 1
            heap.add(-num)  // 최대 힙을 위해 -를 붙여 넣음
        }
        answer.add(-heap.peek())

        // 슬라이딩 윈도우
        for (i in k..<nums.size){
            // 윈도우 우측 이동
            val num = nums[i]
            counter[num] = counter.getOrDefault(num, 0) + 1
            heap.add(-num)
            
            // 윈도우 벗어난 값 빼주기
            val left = nums[i - k]
            counter[left] = counter.getOrDefault(left, 1) - 1

            // lazy removal
            while (counter[-heap.peek()] == 0) {
                heap.poll()
            }
            // 정답에 현재 윈도우 최댓값 추가
            answer.add(-heap.peek())
        }

        return answer.toIntArray()
    }
}