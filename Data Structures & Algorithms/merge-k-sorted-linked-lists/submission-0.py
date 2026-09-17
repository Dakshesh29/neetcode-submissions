# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []

        for list in lists:
            current = list
            while current:
                res.append(current.val)
                current = current.next
        def merge(arr,L,M,R):
            left = arr[L:M+1]
            right = arr[M+1:R+1]
            i,j,k = L,0,0

            while j<len(left) and k<len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j+=1
                else:
                    arr[i]=right[k]
                    k+=1
                i+=1
            while j<len(left):
                arr[i]=left[j]
                j+=1
                i+=1
            while k<len(right):
                arr[i]=right[k]
                k+=1
                i+=1

        def mergeSort(arr,l,r):
            if l>=r:
                return
            
            m = (l+r)//2
            mergeSort(arr,l,m)
            mergeSort(arr,m+1,r)
            merge(arr,l,m,r)

            return arr

        mergeSort(res,0,len(res)-1)

        dummy = ListNode(0)
        current = dummy 

        for value in res:
            current.next = ListNode(value)
            current = current.next

        return dummy.next
