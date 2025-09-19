class Solution {
    fun majorityElement(nums: IntArray): List<Int> {
        val standard = nums.size / 3

        // 고차함수를 활용한 풀이
        // val result = nums.asSequence()
        //             .groupingBy { it }.eachCount()
        //             .filter { it.value > standard }
        //             .keys.toList()

        // 직접 카운팅하기
        val freq = HashMap<Int, Int>(nums.size * 2)
        nums.forEach { v -> freq[v] = (freq[v] ?: 0) + 1 }
        val result = freq.filter { it.value > standard }.keys.toList()

        return result
    }
}