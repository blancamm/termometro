import pygame, sys
from pygame.locals import *

class Termometro(): #se pone al principio porque si lo pone despues como es llamado en mainAPP no va a entender xq todavia no lo ha leido
    def __init__(self):
        self.custome = pygame.image.load('imagenes/termo1.png')
        
    def convertir(self, grados, toUNIDAD):
        resultado = 0
        
        if toUNIDAD == 'F':
           resultado = grados * 9/5 +32
        elif toUNIDAD == 'C':
            resultado = (grados -32) *5/9
        else:
            resultado = grados
       
        return '{:10.2f}'.format(resultado)
        
        
        
class Selector(): #si hago click va a cambiar de foto
    __tipoUnidad = None
    
    def __init__(self, unidad = 'C'):
        self.__customes = []
        self.__customes.append(pygame.image.load('imagenes/posiC.png'))
        self.__customes.append(pygame.image.load('imagenes/posiF.png'))
        
        self.__tipoUnidad = unidad
        
    def custome(self):
        if self.__tipoUnidad == 'C':
            return self.__customes[0]
        elif self.__tipoUnidad == 'F':
            return self.__customes[1]
    
    def change(self, event):
        if self.__tipoUnidad =='F':
            self.__tipoUnidad = 'C'
        else:
            self.__tipoUnidad = 'F'
            
    def unidad(self):
        return self.__tipoUnidad #para acceder al atributo privado que cambia el change
               
     
        
class NumberInput():
    __value = 0
    __strValue = '0'
    __position = [0,0] #para poder modificarlo se pod¡ne en array y no en tupla
    __size = [0, 0] #ancho por alto
    __pointsCount = 0
    
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
    
    def on_event(self, event):
        if event.type == KEYDOWN: #esto quiere decir si pulsas alguna tecla
            if event.unicode.isdigit() and len(self.__strValue) <= 9 or (event.unicode == '.' and self.__pointsCount == 0): #para que no se me vaya del cuadro
                self.__strValue += event.unicode
                self.value(self.__strValue)
                if event.unicode == '.':
                    self.__pointsCount +=1  
            elif event.key == K_BACKSPACE:
                if self.__strValue[-1] =='.':
                    self.__pointsCount -= 1
                self.__strValue = self.__strValue[:-1] #se coge desde 0 al ultimo elemento, pero como es intervalo abierto, no coge el ultimo valor
                self.value(self.__strValue) 
                      
    '''
                mi forma
    for i in range (10):
        if event.unicode == 'i':
            self.entrada = NumberInput('i')
        NO FUNCIONA                                

    otras forma:
        
        if event.type in '0123456789'
    '''

    def value(self, val = None): #HACEMOS EL GETTER DEL VALUE PORQUE LOS ATRIBUTOS SON PRIVADOS
        if val == None:
            return self.__value
        else:
            val = str(val)
            try:
                self.__value = float(val) #si no se mete un entero va a pasar de el (pasa al except) aun asi lo vuelve a poner como str
                self.__strValue = val
                if '.' in self.__strValue:
                    self.__pointsCount = 1
                else:
                    self.__pointsCount= 0
                    
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
        self.entrada = NumberInput('¿funciona?') #como no es un int te pone por defecto 0 cuando abres
        self.entrada.position((115, 30))
        self.entrada.size((133, 28))
        self.selector = Selector()

    def __on_close(self):
        
        pygame.quit()
        sys.exit()
        
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__on_close()
                    
                self.entrada.on_event(event)
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.selector.change(event)#tambien se pasa por el selector por si acaso
                    grados = self.entrada.value() #LLAMAMOS A LA FUNCION GETTER NO AL ATRIBUTO
                    nuevaUnidad = self.selector.unidad()
                    temperatura = self.termometro.convertir(grados, nuevaUnidad)
                    self.entrada.value(temperatura)
            
            
            #PINTAMOS DE NUEVO EL FONDO DE PANTALLA PARA QUE NO SE VEA LA CAPA ANTERIOR
            self.__screen.fill((244, 236, 203))
            
            #PINTAMOS EL TERMOMETRO
            self.__screen.blit(self.termometro.custome, (50,34))  
            
            #PINTAMOS EL EL CUADRO Y LA TEMPERATURA
            text = self.entrada.render() #me devuelve el texto y el recuadro. HAY QUE PONER UNA VARIABLE A ESTE RETURN
            pygame.draw.rect(self.__screen, (255,255,255), (text['fondo'])) #para pintar el fondo (crear rectangulo blanco)
            self.__screen.blit(text['texto'], self.entrada.position())   #para pintar la temperatura que se ha escrito
            
            #PINTAMOS EL SELECTOR
            self.__screen.blit(self.selector.custome(), (115,100))
            
            
            pygame.display.flip() #refresco pantalla
            
if __name__ == '__main__':
    pygame.font.init()
    termometro = MainApp()
    termometro.start()
                    
        