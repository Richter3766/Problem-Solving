class Solution {
    fun isValid(s: String): Boolean {
        // 기초적인 스택 문제
        // 열린 괄호는 스택에 넣기

        // 닫힌 괄호가 나오면 스택 pop 한 값과 비교하기
        // 만약 같으면 넘어가고
        // 다르면 False 반환
        val openOf = setOf('(', '{', '[')
        val closeOf = mapOf('(' to ')', '{' to '}', '[' to ']')
        val stack = ArrayDeque<Char>()

        for (p in s) {
            if (p in openOf) {
                stack.addLast(p)      // push
                continue
            }
            // 닫는 괄호를 만났을 때
            if (stack.isEmpty()) return false
            val last = stack.removeLast() // pop
            if (closeOf[last] != p) return false
        }
        return stack.isEmpty()
    }
}