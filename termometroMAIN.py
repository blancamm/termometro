import pygame, sys
from pygame.locals import *

class Termometro(): #se pone al principio porque si lo pone despues como es llamado en mainAPP no va a entender xq todavia no lo ha leido
    def __init__(self):
        self.custome = pygame.image.load('imagenes/termo1.png')
        
class NumberInput():
    __value = 0
    __strValue = '0'
    __position = [0,0] #para poder modificarlo se pod¡ne en array y no en tupla
    __size = [0, 0] #ancho por alto
    
    def __init__(self, value = 0):
        
        self.__font = pygame.font.SysFont('Arial',24) #eliges la fuente
        self.value(value) #para comprobar si es un numero, si no lo es se pone el 0 por defect0

    def render(self):
        textBlock = self.__font.render(self.__strValue, True, (74, 74, 74)) #SOLO PINTA CADENAS
        rect = textBlock.get_rect()#ahora vamos a renderizar este texto (obtener el recuadro)
        rect.left = self.__position[0]
        rect.top = self.__position[1]
        rect.size = self.__size #en memoria esta el cuadro creado
        
        return {'fondo':rect, 'texto': textBlock}
        
        
    def value(self, val = None): #HACEMOS EL GETTER DEL VALUE PORQUE LOS ATRIBUTOS SON PRIVADOS
        if val == None:
            return self.__value
        else:
            val = str(val)
            try:
                self.__value = int(val) #si no se mete un entero va a pasar de el
                self.__strValue = val
            except:
                pass
                
    def ancho(self, val = None):
        if val == None:
            return self.__size[0]
        else:
            try:
                self.__size [0] == int(val)
            except:
                pass
            
    def altura(self, val = None):
        if val == None:
            return self.__size[1]
        else:
            try:
                self.__size [1] == int(val)
            except:
                pass
            
    def size( self, val= None):
        if val == None:
            return self.__size
        else:
            try:
                w = int(val[0])
                h = int(val[1])
                self.__size = [int(val[0]), int(val[1])]
            except:
                pass
            
    def posX(self, valor = None):
        if valor == None:
            return self.__position[0]
        else:
            try:
                self.__position[0] == int(valor)
            except:
                pass
            
    def posY(self, valor = None):
        if valor == None:
            return self.__position[1]
        else:
            try:
                self.__position[1] == int(valor)
            except:
                pass
            
    def position( self, val= None):
        if val == None:
            return self.__size
        else:
            try:
                w = int(val[0])
                h = int(val[1])
                self.__position = [int(val[0]), int(val[1])]
            except:
                pass
        
class MainApp():
    termometro = None
    entradas = None
    selector = None

    def __init__(self):
        self.__screen = pygame.display.set_mode((290,415))
        pygame.display.set_caption('Termómetro')
        self.__screen.fill((244, 236, 203))
        
        self.termometro = Termometro()
        self.entrada = NumberInput('¿funciona?')
        self.entrada.position((115, 30))
        self.entrada.size((133, 28))        
    
    def __on_close(self):
        
        pygame.quit()
        sys.exit()
        
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__on_close()
            
            
            self.__screen.blit(self.termometro.custome, (50,34))   #foto fija
            text = self.entrada.render() #me devuelve el texto y el recuadro. HAY QUE PONER UNA VARIABLE A ESTE RETURN
            pygame.draw.rect(self.__screen, (255,255,255), (text['fondo'])) #para pintar el fondo (crear rectangulo blanco)
            self.__screen.blit(text['texto'], self.entrada.position())   #para pintar la temperatura que se ha escrito
            
            
            pygame.display.flip() #refresco pantalla
            
if __name__ == '__main__':
    pygame.font.init()
    termometro = MainApp()
    termometro.start()
                    
        