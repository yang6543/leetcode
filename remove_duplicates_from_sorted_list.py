# 给定一个排序链表，删除所有重复项，每个元素只出现一次

def deleteDuplicates(self, head):
	"""
	:type head: ListNode
	:rtype: ListNode
	"""
	cur = head
	while cur:
		while cur.next and cur.next.val == cur.val:
			cur.next = cur.next.next
		cur = cur.next
	return head


Input: 1->1->2->3->3
Output: 1->2->3