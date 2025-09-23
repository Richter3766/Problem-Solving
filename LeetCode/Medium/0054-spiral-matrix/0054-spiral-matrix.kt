class Solution {
    fun spiralOrder(matrix: Array<IntArray>): List<Int> {
        // 빈 입력 가드
        if (matrix.isEmpty() || matrix[0].isEmpty()) return emptyList()

        val rows = matrix.size
        val cols = matrix[0].size
        val total = rows * cols

        // (dr, dc): 우, 하, 좌, 상
        val directions = listOf(0 to 1, 1 to 0, 0 to -1, -1 to 0)

        // 방문 여부
        val visited = Array(rows) { BooleanArray(cols) }
        val ans = mutableListOf<Int>()

        var r = 0
        var c = 0
        var dir = 0 // 현재 방향 인덱스(0..3)

        while (ans.size < total) {
            // 현재 칸 처리
            ans.add(matrix[r][c])
            visited[r][c] = true

            // 다음 칸 후보
            val (dr, dc) = directions[dir]
            val nr = r + dr
            val nc = c + dc

            // 범위를 벗어나거나 이미 방문했다면 방향 전환
            if (nr !in 0 until rows || nc !in 0 until cols || visited[nr][nc]) {
                dir = (dir + 1) % directions.size
            }

            // 전환된(또는 유지된) 방향으로 실제 이동
            val (ndr, ndc) = directions[dir]
            r += ndr
            c += ndc
        }

        return ans
    }
}