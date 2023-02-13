init()

size = (8,5)

screen =  display.set_mode(size)

running = True
while running:
    for e in event.get() :
        if e.type == QUIT:
            running = False
quit()