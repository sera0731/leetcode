# Time complexity : O(N)
# Space complexity : O(N)

from collections import deque

class Solutions :
	def isCousins(self, root: TreeNode, x: int, y: int) -> bool :
	
		queue = deque([root])
		
		while queue :
		
			queue_length = len(queue)
			
			cousins = False
			siblings = False
			
			for i in range(queue_length) :
				node = queue.popleft()
				
				if not node :
					siblings = False
				else :
					if node.val == x or node.val == y :
						if not cousins :
							cousins, siblings = True, True
						else :
							return not siblings
							
					queue.append(node.left)
					queue.append(node.right)
					queue.append(None)
					
			if cousins :
				return False
				
		return False
			
