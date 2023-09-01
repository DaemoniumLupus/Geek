class Translation:
    def Translation(self, num , notation):
        buffer_massive = []
        while num > notation:
            buffer_massive.append(num % notation)
            num //= notation
            
        buffer_massive.append(num%notation)
        if num//notation != 0:
            buffer_massive.append(num//notation)
    
        num_string = ""
        for i in range(1,len(buffer_massive) + 1):
            num_string += str(buffer_massive[-i])
        
        return num_string