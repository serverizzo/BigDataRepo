import random


class uniformSet:

    def __init__(self,size):
        self.uniformArray = [None] * size
        self.size = size
        self.numberElement = 1 # 1 instead of zero to account for divide by zero


    def willBeIncluded(self):
        
        return random.random() < (self.size/self.numberElement) 


    def randomlySelectedElement(self):
        return random.randrange(self.size)

    def addElement(self, newElement):
        if self.numberElement < self.size:
            self.uniformArray[self.numberElement-1] = newElement
            self.numberElement += 1
        
        else:
            self.numberElement += 1

            # Determine if the element will be added or not.        
            if self.willBeIncluded():
                # print(newElement, "will be included with prob: ", self.size/self.numberElement)
                
                # Determine which element will be replaced
                selectedElement = self.randomlySelectedElement()
                self.uniformArray[selectedElement] = newElement


            
    def returnSet(self):
        return self.uniformArray

