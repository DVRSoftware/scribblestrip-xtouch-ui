class counter:
    def __init__(self,counts):
        self.counts=counts
        self.cnt=counts
    
    def expired(self):
        self.cnt+=1
        if(self.cnt>=self.counts):
            self.cnt=0
            return True
        else:
            return False
        