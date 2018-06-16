# 两个非空(非负整数)链表，数字以相反顺序存储，每个节点包含一个数字，添加这两个数字并将其作为链表返回。

def addTwoNumbers(self, l1, l2):
	carry = 0  # 进位
	root = n = ListNode(0)
	while l1 or l2 or carry:
		v1 = v2 = 0
		if l1:
			v1 = l1.val
			l1 = l1.next
		if l2:
			v2 = l2.val
			l2 = l2.next
		carry, val = divmod(v1+v2+carry, 10)
		n.next = ListNode(val)
		n = n.next
	return root.next


Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.