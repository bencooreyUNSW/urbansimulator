#Config Class
#Set of global parameters
#Contributors: Ben Coorey

class config:
    
    @staticmethod
    def roadWidth(argument):
        switcher = {
            1: 12, #Primary
            2: 8, #Secondary
            3: 6, #Tertiary
        }
        return switcher.get(argument, 0)
        
    @staticmethod
    def bdyOffset(argument):
        switcher = {
            1: 6, #Main Street Frontage
            2: 3, #Secondary Street Frontage
            3: 1.5, #Side
            4: 4, #Rear
        }
        return switcher.get(argument, 0)