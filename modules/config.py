#Config Class
#Set of global parameters
#Contributors: Ben Coorey

class config:
    
    @staticmethod
    def roadWidth(argument):
        switcher = {
            1: 6, #Primary
            2: 4, #Secondary
            3: 3, #Tertiary
        }
        return switcher.get(argument, 0)