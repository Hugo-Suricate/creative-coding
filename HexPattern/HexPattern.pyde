from Hex import Hex
import HexPatternGenerator as Generator
import HexPatternAnimator as Renderer

frame = 0

def setup():
    size(Renderer.disp_h,Renderer.disp_w)
    frameRate(40)
    
    Generator.newSeed()
    
    Generator.Generate()
    #Renderer.Render(Generator.patterns, Generator.seed)

def draw():
    global frame
    Renderer.Render(Generator.patterns, Generator.seed)
    saveFrame("anim/frame"+str(frame)+".png");
    frame +=1

def keyPressed():
    global seed
    
    if key == 'g':
        Generator.newSeed()
        
        Generator.Generate()
        Renderer.Render(Generator.patterns, Generator.seed)
    if key == 's':
        saveFrame("hex-"+str(seed)+".png")
  
    if key == 'c':
        Renderer.newColors(Generator.pattern_count)
        Renderer.Render(Generator.patterns, Generator.seed)
    
    if key == '+':
        Generator.setRadius(Generator.radius + 1)
        Generator.Generate()
        Renderer.Render(Generator.patterns, Generator.seed)
        
    if key == '-':
        Generator.setRadius(Generator.radius - 1)
        Generator.Generate()
        Renderer.Render(Generator.patterns, Generator.seed)
  
  # if(key == 'b')
  # {
  #   colbg = color(int(random(256)), int(random(256)), int(random(256)));
  # }
