class TimeMap:

    def __init__(self):
        self.store={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key]=[]
        self.store[key].append((timestamp,value))
        
        # print(self.store[0][1])

    
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        values=self.store[key]
        res=""
        left=0
        right=len(values)-1
        while left<=right:
            mid=(left+right)//2

            if values[mid][0] <=timestamp:
                res=values[mid][1]
                left=mid+1
                print(res)
            else:
                right=mid-1
        return res

        

        '''
        alice: [1,happy] [2,"something"]
        l=0,r=0
        mid

        Inintialize the dictoanry to store keyis name and value,timestamp..

        in set function I need to store the key,(value,timestamp)
        
        set -> alice:(happy,1)

        get(alice,1) to get we chek if the timestamp exist then return the value[0] in that timestamp
        if not we get the previous timestamp..

        the conditon to do binary search is timesatmp>= previous_timestamp..


        get(alice,2) check if 

        after creating dictonry set return a dictonary after appendin a new value to it..

        get()

        is where we do the binary search..

        so left=0 right= len(key[value])

        '''
