class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        def size(head):
            count = 0
            while head:
                count += 1
                head = head.next
            return count
        
        n = size(head)
        
        part_len = n // k
        extra_for = n % k
        
        parts = []
        current = head
        
        for i in range(k):
            part_head = current
            current_part_size = part_len + (1 if i < extra_for else 0)
            
            for _ in range(current_part_size - 1):
                if current:
                    current = current.next
            if current:
                next_part = current.next
                current.next = None
                current = next_part
            parts.append(part_head)
        return parts
