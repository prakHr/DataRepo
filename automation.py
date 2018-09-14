#-----------------------------------------SETTINGS TO BEGIN AUTOMATING THE CODE ON TRADE.RAPNET SITE USING IMAGE RECOGNITION AND COORDINATES ON SCREEN(CAN'T BE DONE ON BACKGROUND)------------#
#------------ click on show 250 results,open a text file minimize the size and find the position of edit button, goto ctrl+shift+i =>network tab--------------------------------------------------------- #
#-----------find the position of close button (1348,125) and double arrow(1214,127)on the network from ctrl+shift+i and keep it minimized on site ------------------------------------------------------#
#----------do the maths :- no of pages to click=1298697/250=5194.788=>5193-20 =5173 pages to do for 250---------------------------------------------------------------------------#
#------------code can be made shorter by storing locations of 10 buttons as a (x,y)tuple in an array and write a one single code that iterates through that array------------------------------------------------#
###########################################################################################################################################################
import pyautogui,time

#hot-key pressing is not possible so right mouse click/move to edit button=> then move to copy/cut/paste and click it
#pyautogui.moveTo(198,257);pyautogui.keyDown('ctrl');time.sleep(0.300);pyautogui.keyDown('a');time.sleep(0.300);pyautogui.keyUp('a');time.sleep(0.300);pyautogui.keyUp('ctrl')


time.sleep(10)

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True#go to upper left corner to invoke it
#10 buttons are clicked using imageRecognition,or if you are comfortable with fixed coordinates with the settings properly applied you can give them using pyautogui.position() and time.sleep() then repeated pattern of clicking 5173 pages at a fixed button(1110,677)#
width,height=pyautogui.size()#gives total inner width and height of inner window


#for 250 results (10 scrolls is necessary) 
pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width)

pyautogui.click(button='right');pyautogui.typewrite(['up','enter'],interval=0.1)#right click and inspect(ctrl+shift+I)


#intead of Image Recognition of buttons use time.sleep() that is faster than reverse image processing and giving a limited region as these methods are not reliable due to loading nature of ajax,json page
pyautogui.click(1005,718);time.sleep(2)#after inspecting dragging by clicking the horizontal scrollbar of the site at bottom
#coordinates of button 2 are found using x2,y2=pyautogui.center(pyautogui.locateOnScreen('b22.png'))
x2,y2=757,667
time.sleep(2)
pyautogui.click(x2,y2)
#1
while(pyautogui.locateOnScreen('shape.png')==None):
    time.sleep(0.300)
pyautogui.click(1214,127);pyautogui.typewrite(['down','down','down','down','enter'],interval=0.1)#click the double arrow and go to network
pyautogui.moveTo(1158,299);pyautogui.click(button='right');pyautogui.typewrite(['down','down','down','down','right','down','down','down','down','enter'],interval=0.1)#copy the response file
pyautogui.moveTo(44,41);pyautogui.click();pyautogui.typewrite(['down','down','down','down','enter'],interval=0.1)#move to edit button of text file
pyautogui.moveTo(1348,125);pyautogui.click()#then close

#the again scroll all the way down and right click go to inspect,then click button3 ,same procedure is repeated for 10 butttons after that position of rest of the button get fixed so simply run a while loop

pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width)
pyautogui.click(button='right');pyautogui.typewrite(['up','enter'],interval=0.1)
pyautogui.click(1005,718);time.sleep(2)
x3,y3=pyautogui.center(pyautogui.locateOnScreen('b3.png'))
pyautogui.click(x3,y3)

#after going to next page do image recognition on shape named row-header and wait for the page to load
while(pyautogui.locateOnScreen('shape.png')==None):
    time.sleep(0.300)

pyautogui.click(1214,127);pyautogui.typewrite(['down','down','down','down','enter'],interval=0.1)
pyautogui.moveTo(1158,299);pyautogui.click(button='right');pyautogui.typewrite(['down','down','down','down','right','down','down','down','down','enter'],interval=0.1)
pyautogui.moveTo(44,41);pyautogui.click();pyautogui.typewrite(['down','down','down','down','enter'],interval=0.1)
pyautogui.moveTo(1348,125);pyautogui.click()

pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width)
pyautogui.click(button='right');pyautogui.typewrite(['up','enter'],interval=0.1)
pyautogui.click(1005,718);time.sleep(2)
x4,y4=pyautogui.center(pyautogui.locateOnScreen('b4.png'))
pyautogui.click(x4,y4)


while(pyautogui.locateOnScreen('shape.png')==None):
    time.sleep(0.300)

pyautogui.click(1214,127);pyautogui.typewrite(['down','down','down','down','enter'],interval=0.1)
pyautogui.moveTo(1158,299);pyautogui.click(button='right');pyautogui.typewrite(['down','down','down','down','right','down','down','down','down','enter'],interval=0.1)
pyautogui.moveTo(44,41);pyautogui.click();pyautogui.typewrite(['down','down','down','down','enter'],interval=0.1)
pyautogui.moveTo(1348,125);pyautogui.click()

pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width)
pyautogui.click(button='right');pyautogui.typewrite(['up','enter'],interval=0.1)
pyautogui.click(1005,718);time.sleep(2)
x5,y5=pyautogui.center(pyautogui.locateOnScreen('b5.png'))
pyautogui.click(x5,y5)

while(pyautogui.locateOnScreen('shape.png')==None):
    time.sleep(0.300)

pyautogui.click(1214,127);pyautogui.typewrite(['down','down','down','down','enter'],interval=0.1)
pyautogui.moveTo(1158,299);pyautogui.click(button='right');pyautogui.typewrite(['down','down','down','down','right','down','down','down','down','enter'],interval=0.1)
pyautogui.moveTo(44,41);pyautogui.click();pyautogui.typewrite(['down','down','down','down','enter'],interval=0.1)
pyautogui.moveTo(1348,125);pyautogui.click()

pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width)
pyautogui.click(button='right');pyautogui.typewrite(['up','enter'],interval=0.1)
pyautogui.click(1005,718);time.sleep(2)
x6,y6=pyautogui.center(pyautogui.locateOnScreen('b6.png'))
pyautogui.click(x6,y6)


while(pyautogui.locateOnScreen('shape.png')==None):
    time.sleep(0.300)

pyautogui.click(1214,127);pyautogui.typewrite(['down','down','down','down','enter'],interval=0.1)
pyautogui.moveTo(1158,299);pyautogui.click(button='right');pyautogui.typewrite(['down','down','down','down','right','down','down','down','down','enter'],interval=0.1)
pyautogui.moveTo(44,41);pyautogui.click();pyautogui.typewrite(['down','down','down','down','enter'],interval=0.1)
pyautogui.moveTo(1348,125);pyautogui.click()

pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width)
pyautogui.click(button='right');pyautogui.typewrite(['up','enter'],interval=0.1)
pyautogui.click(1005,718);time.sleep(2)
x7,y7=pyautogui.center(pyautogui.locateOnScreen('b7.png'))
pyautogui.click(x7,y7)

while(pyautogui.locateOnScreen('shape.png')==None):
    time.sleep(0.300)

pyautogui.click(1214,127);pyautogui.typewrite(['down','down','down','down','enter'],interval=0.1)
pyautogui.moveTo(1158,299);pyautogui.click(button='right');pyautogui.typewrite(['down','down','down','down','right','down','down','down','down','enter'],interval=0.1)
pyautogui.moveTo(44,41);pyautogui.click();pyautogui.typewrite(['down','down','down','down','enter'],interval=0.1)
pyautogui.moveTo(1348,125);pyautogui.click()

pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width)
pyautogui.click(button='right');pyautogui.typewrite(['up','enter'],interval=0.1)
pyautogui.click(1005,718);time.sleep(2)
x8,y8=pyautogui.center(pyautogui.locateOnScreen('b8.png'))
pyautogui.click(x8,y8)

while(pyautogui.locateOnScreen('shape.png')==None):
    time.sleep(0.300)

pyautogui.click(1214,127);pyautogui.typewrite(['down','down','down','down','enter'],interval=0.1)
pyautogui.moveTo(1158,299);pyautogui.click(button='right');pyautogui.typewrite(['down','down','down','down','right','down','down','down','down','enter'],interval=0.1)
pyautogui.moveTo(44,41);pyautogui.click();pyautogui.typewrite(['down','down','down','down','enter'],interval=0.1)
pyautogui.moveTo(1348,125);pyautogui.click()
    
pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width)
pyautogui.click(button='right');pyautogui.typewrite(['up','enter'],interval=0.1)
pyautogui.click(1005,718);time.sleep(2)
x9,y9=pyautogui.center(pyautogui.locateOnScreen('b9.png'))
pyautogui.click(x9,y9)

while(pyautogui.locateOnScreen('shape.png')==None):
    time.sleep(0.300)

pyautogui.click(1214,127);pyautogui.typewrite(['down','down','down','down','enter'],interval=0.1)
pyautogui.moveTo(1158,299);pyautogui.click(button='right');pyautogui.typewrite(['down','down','down','down','right','down','down','down','down','enter'],interval=0.1)
pyautogui.moveTo(44,41);pyautogui.click();pyautogui.typewrite(['down','down','down','down','enter'],interval=0.1)
pyautogui.moveTo(1348,125);pyautogui.click()

pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width)
pyautogui.click(button='right');pyautogui.typewrite(['up','enter'],interval=0.1)
pyautogui.click(1005,718);time.sleep(2)
x10,y10=pyautogui.center(pyautogui.locateOnScreen('b10.png'))
pyautogui.click(x10,y10)

while(pyautogui.locateOnScreen('shape.png')==None):
    time.sleep(0.300)

pyautogui.click(1214,127);pyautogui.typewrite(['down','down','down','down','enter'],interval=0.1)
pyautogui.moveTo(1158,299);pyautogui.click(button='right');pyautogui.typewrite(['down','down','down','down','right','down','down','down','down','enter'],interval=0.1)
pyautogui.moveTo(44,41);pyautogui.click();pyautogui.typewrite(['down','down','down','down','enter'],interval=0.1)
pyautogui.moveTo(1348,125);pyautogui.click()

pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width)
pyautogui.click(button='right');pyautogui.typewrite(['up','enter'],interval=0.1)
pyautogui.click(1005,718);time.sleep(2)
#x11,y11=pyautogui.center(pyautogui.locateOnScreen('b11.png'))

iterator=1
while (iterator<5173):
    time.sleep(6)
    x,y=893,685
    pyautogui.click(x,y)
    
    while(pyautogui.locateOnScreen('shape.png')==None):
        time.sleep(0.300)

    pyautogui.click(1214,127);pyautogui.typewrite(['down','down','down','down','enter'],interval=0.5)
    pyautogui.moveTo(1158,299);pyautogui.click(button='right');pyautogui.typewrite(['down','down','down','down','right','down','down','down','down','enter'],interval=0.5)
    pyautogui.moveTo(44,41);pyautogui.click();pyautogui.typewrite(['down','down','down','down','enter'],interval=0.5)
    pyautogui.moveTo(1348,125);pyautogui.click()

    pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width);pyautogui.scroll(-width)
    pyautogui.click(button='right');pyautogui.typewrite(['up','enter'],interval=0.3)
    pyautogui.click(1005,718);time.sleep(2)    
    
    iterator+=1
    time.sleep(2)




