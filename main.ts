basic.forever(function on_forever() {
    let x = input.acceleration(Dimension.X)
    let y = input.acceleration(Dimension.Y)
    if (x > 100) {
        basic.showArrow(ArrowNames.East)
    } else if (x < -100) {
        basic.showArrow(ArrowNames.West)
    } else if (y > 200) {
        basic.showArrow(ArrowNames.South)
    } else if (y < -200) {
        basic.showArrow(ArrowNames.North)
    } else {
        basic.showIcon(IconNames.Happy)
    }
    
})
