GlowScript 3.0 VPython

G=6.67e-11

ge = gcurve(color = color.blue, label="Force on Earth")
#gn = gcurve(color = color.cyan, label="Force on Neptune")
#gj = gcurve(color = color.yellow, label="Force on Jupiter")
SunMercuryDistance = 5.7e10
SunVenusDistance  = 1.08e11
SunEarthDistance = 1.5e11
SunMarsDistance = 2.28e11
SunJupiterDistance = 7.79e11
SunSaturnDistance = 1.43e12
SunUranusDistance = 2.388e12
SunNeptuneDistance = 4.5e12

SunMass = 1.9891e30
SunRadius = 6.96e8

def equation(x1,x2):
    G = 6.67e-11
    rad = x1.pos-x2.pos
    magnitude = mag(rad)
    unitdistance = rad/magnitude
    force_magnitude = G*x1.mass*x2.mass/magnitude**2
    force_vector = -force_magnitude*unitdistance
    return force_vector

vstartMercury=sqrt(G*1.9891e30/SunMercuryDistance)*3.285e23
vstartVenus=sqrt(G*1.9891e30/SunVenusDistance)*4.867e24
vstartEarth=sqrt(G*1.9891e30/SunEarthDistance)*5.972e24
vstartMars=sqrt(G*1.9891e30/SunMarsDistance)*6.39e23
vstartJupiter=sqrt(G*1.9891e30/SunJupiterDistance)*1.898e27
vstartSaturn=sqrt(G*1.9891e30/SunSaturnDistance)*5.683e26
vstartUranus=sqrt(G*1.9891e30/SunUranusDistance)*8.681e25 
vstartNeptune=sqrt(G*1.9891e30/SunNeptuneDistance)*1.024e26

sun = sphere(pos=vector(0,0,0), radius=SunRadius, color=color.yellow, mass = SunMass, momentum=vector(0,0,0), make_trail=True)
earth = sphere(pos=vector(SunEarthDistance,0,0), radius=6.378e6, color=color.blue, mass = 5.972e24, make_trail=True, momentum=vector(0,vstartEarth,0))
mercury = sphere(pos=vector(SunMercuryDistance,0,0), radius=2440000, color=color.gray(0.5), mass = 3.285e23, make_trail=True, momentum=vector(0,vstartMercury,0))
venus = sphere(pos=vector(SunVenusDistance,0,0), radius=6052000, color=vector(1,0.7,0.2), mass = 4.867e24, make_trail=True, momentum=vector(0,vstartVenus,0))
mars = sphere(pos=vector(SunMarsDistance,0,0), radius=3390000, color=color.magenta, mass = 6.39e23, make_trail=True, momentum=vector(0,vstartMars,0))
jupiter = sphere(pos=vector(SunJupiterDistance,0,0), radius=69911000, color=color.yellow, mass = 1.898e27, make_trail=True, momentum=vector(0,vstartJupiter,0))
saturn = sphere(pos=vector(SunSaturnDistance,0,0), radius=58232000, color=color.orange, mass = 5.683e26, make_trail=True, momentum=vector(0,vstartSaturn,0))
uranus = sphere(pos=vector(SunUranusDistance,0,0), radius=25362000, color=color.green, mass = 8.681e25, make_trail=True, momentum=vector(0,vstartUranus,0))
neptune = sphere(pos=vector(SunNeptuneDistance,0,0), radius=24622000, color=color.cyan, mass = 1.024e26, make_trail=True, momentum=vector(0,vstartNeptune,0))



dt = 24*60*60*2
t = 0
while t<24*60*60*365.25*165:
    rate(100)
 
#    sun.force=equation(earth,sun) + equation(mercury,sun) + equation(venus,sun) + equation(mars,sun) + equation(jupiter,sun) + equation(saturn,sun) + equation(uranus,sun) + equation(neptune,sun)
    earth.force=equation(earth,sun)
    mercury.force=equation(mercury,sun)
    venus.force=equation(venus,sun)
    mars.force=equation(mars,sun)
    jupiter.force=equation(jupiter,sun)
    saturn.force=equation(saturn,sun)
    uranus.force=equation(uranus,sun)
    neptune.force=equation(neptune,sun)
    
    ge.plot(t, mag(earth.force))
  #  gn.plot(t, mag(neptune.force))
  #  gj.plot(t, mag(jupiter.force))
    
#    sun.momentum = sun.momentum + sun.force*dt
    mercury.momentum = mercury.momentum + mercury.force*dt
    venus.momentum = venus.momentum + venus.force*dt
    earth.momentum = earth.momentum + earth.force*dt
    mars.momentum = mars.momentum + mars.force*dt
    jupiter.momentum=jupiter.momentum+jupiter.force*dt
    saturn.momentum=saturn.momentum+saturn.force*dt
    uranus.momentum=uranus.momentum+uranus.force*dt
    neptune.momentum = neptune.momentum + neptune.force*dt
    
#    sun.pos = sun.pos+sun.momentum/sun.mass*dt
    mercury.pos = mercury.pos+mercury.momentum/mercury.mass*dt
    venus.pos = venus.pos + venus.momentum/venus.mass*dt
    earth.pos = earth.pos + earth.momentum/earth.mass*dt
    mars.pos = mars.pos + mars.momentum/mars.mass*dt
    jupiter.pos=jupiter.pos+jupiter.momentum/jupiter.mass*dt
    saturn.pos=saturn.pos+saturn.momentum/saturn.mass*dt
    uranus.pos=uranus.pos+uranus.momentum/uranus.mass*dt
    neptune.pos = neptune.pos + neptune.momentum/neptune.mass*dt
    
    t = t + dt
