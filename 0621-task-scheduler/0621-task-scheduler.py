class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        m = max(freq.values())
        
        max_tasks = sum(1 for ele in freq.values() if ele == m)
        
        inter = (m-1) * (n + 1) + max_tasks
        
        return max(inter, len(tasks))