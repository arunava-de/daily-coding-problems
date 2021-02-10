## We'll use merge sort (modified) to solve the problem

def counting_inversions(A):

    def merge_sort(l, temp_l, left, right):
        res = 0
        if right<=left:
            return res

        mid = (left+right)//2

        res += merge_sort(l,temp_l,left,mid)
        res += merge_sort(l,temp_l,mid+1,right)
        res += merge(l,temp_l,left,right,mid)

        return res

    def merge(l, temp_l, left, right, mid):
        inv = 0

        i = left
        j = mid+1
        k = left 

        m = []
        while i<=mid and j<=right:
            if l[i]<=l[j]:
                temp_l[k] = l[i]
                i += 1
                k += 1
            else:
                temp_l[k] = l[j]
                j += 1
                k += 1
                inv += mid-i + 1
        
        while i<=mid:
            temp_l[k] = l[i]
            i += 1
            k += 1
        
        while j<=right:
            temp_l[k] = l[j]
            j += 1
            k += 1
        
        for i in range(left,right+1):
            l[i] = temp_l[i]
        
        return inv

    print(merge_sort(A, [0]*len(A), 0, len(A)-1))
    

counting_inversions([1,3,2])
counting_inversions([2,4,1,3,5])



        