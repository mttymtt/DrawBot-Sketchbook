def easeInOutQuad(t):
    t *= 2
    if t < 1:
        return 0.5 * (t ** 2)
    else:
        t = 2 - t
        return 1 - 0.5 * (t ** 2)
        
total_frames = 20
         
for frame in range(total_frames):
    newPage()
    ease = easeInOutQuad(frame / (total_frames - 1))
    print(ease)
    
    oval(width() * ease, 0, 10, 10)
    
for frame in range(total_frames):
    newPage()
    ease = easeInOutQuad(frame / (total_frames - 1))
    print(ease)
    
    oval(width() - (width() * ease), 0, 10, 10)
    
saveImage("04_animation.gif")