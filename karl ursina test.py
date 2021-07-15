from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina() 
ground = Entity(model='plane',
                texture= 'grass',
                collider= 'mesh',
                scale= (90,1,90))

player = FirstPersonController()
Sky()

myBox = Entity(model= 'cube',
                color= color.blue,
                collider= 'box',
                position= (5, 0.5, 5))

myBox = Entity(model= 'cube',
                color= color.blue,
                collider= 'box',
                position= (5, 0.5, 4))
myBox = Entity(model= 'cube',
                color= color.black,
                collider= 'box',
                position= (3, 2.5, 5))

myBox = Entity(model= 'cube',
                color= color.black,
                collider= 'box',
                position= (3, 2.5, 4))

myBox = Entity(model= 'cube',
                color= color.red,
                collider= 'box',
                position= (4, 1.5, 5))

myBox = Entity(model= 'cube',
                color= color.red,
                collider= 'box',
                position= (4, 1.5, 4))
myBox = Entity(model= 'cube',
                color= color.brown,
                collider= 'box',
                position= (2, 3.5, 5))

myBox = Entity(model= 'cube',
                color= color.brown,
                collider= 'box',
                position= (2, 3.5, 4))

myBox = Entity(model= 'cube',
                color= color.brown,
                collider= 'box',
                position= (-1, 3.5, 5))

myBox = Entity(model= 'cube',
                color= color.brown,
                collider= 'box',
                position= (-1, 3.5, 4))

myBox = Entity(model= 'cube',
                color= color.brown,
                collider= 'box',
                position= (0, 3.5, 3))

myBox = Entity(model= 'cube',
                color= color.brown,
                collider= 'box',
                position= (1, 3.5, 3))

myBox = Entity(model= 'cube',
                color= color.brown,
                collider= 'box',
                position= (0, 3.5, 6))

myBox = Entity(model= 'cube',
                color= color.brown,
                collider= 'box',
                position= (1, 3.5, 6))       

myBox = Entity(model= 'cube',
                color= color.yellow,
                collider= 'box',
                position= (0.5, 3.5, 4.5))  

myBox = Entity(model= 'cube',
                color= color.black,
                collider= 'box',
                position= (1, 2.5, 7))

myBox = Entity(model= 'cube',
                color= color.black,
                collider= 'box',
                position= (1, 2.5, 2))

myBox = Entity(model= 'cube',
                color= color.black,
                collider= 'box',
                position= (0, 2.5, 7))

myBox = Entity(model= 'cube',
                color= color.black,
                collider= 'box',
                position= (0, 2.5, 2)) 

myBox = Entity(model= 'cube',
                color= color.black,
                collider= 'box',
                position= (-2, 2.5, 5))

myBox = Entity(model= 'cube',
                color= color.black,
                collider= 'box',
                position= (-2, 2.5, 4))
app.run()