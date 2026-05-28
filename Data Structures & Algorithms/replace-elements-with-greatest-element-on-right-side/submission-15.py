class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        count=len(arr)
        for i in range(count):
            greatest= max(arr[i+1::],default=-1)
            arr[i]=greatest
        return arr