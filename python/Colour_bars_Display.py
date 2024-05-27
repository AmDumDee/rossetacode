
from livewires import *

horiz=640; vert=480
begin_graphics(width=horiz,height=vert,title="v_stripes",background=Colour.black)
NameColors=["black","red","green","dark_blue","purple","blue","yellow","white"]
stepik=horiz/len(NameColors)

for index,each in enumerate(NameColors):
    ExcStrng="set_colour(Colour."+each+")"
    exec(ExcStrng)
    box(index*stepik,0,(index+1)*stepik,vert,filled=1)

while keys_pressed() != ['x']: 
    pass

end_graphics()
