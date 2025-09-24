class Solution {
    fun topKFrequent(nums: IntArray, k: Int): IntArray {
        // 빈도수를 저장할 해시맵
        val counter = HashMap<Int, Int>()   

        // 최대 빈도수 유지를 위한 힙
        val minHeap = PriorityQueue<Pair<Int, Int>>(compareBy { it.first} ) 
        
        // 인자의 nums에서 빈도수 카운팅
        nums.forEach{ num ->
            val cur = counter.getOrDefault(num, 0) + 1
            counter[num] = cur
        }

        // 최소 힙의 크기를 k로 유지하여 최대 빈도수 숫자만 남김
        counter.forEach{ (key, freq) ->
            minHeap.add(freq to key)
            if (minHeap.size > k) {
                minHeap.poll()
            }
        }

        return minHeap
            .map{ it.second }
            .toIntArray()
    }
}