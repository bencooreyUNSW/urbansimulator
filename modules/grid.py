#Grid Class
#Create a Grid
#Contributors: Ben Coorey

class Grid:
    
    #Define and initiate the class
    def __init__(self, noX = 5, noY = 5, spacingX = 5, spacingY = 10):
        self.noX = noX
        self.noY = noY
        self.spacingX = spacingX
        self.spacingY = spacingY
        
    def __str__(self):
        return "This is a grid %s x %s Grid with %s x %s spacing" %(self.noX, self.noY, self.spacingX, self.spacingY)