def on_forever():
    x = input.acceleration(Dimension.X)
    y = input.acceleration(Dimension.Y)

    if x > 100:
        basic.show_arrow(ArrowNames.EAST)
    elif x < -100:
        basic.show_arrow(ArrowNames.WEST)
    elif y > 200:
        basic.show_arrow(ArrowNames.SOUTH) 
    elif y < -200:
        basic.show_arrow(ArrowNames.NORTH) 
    else:
        basic.show_icon(IconNames.HAPPY)    
basic.forever(on_forever)
