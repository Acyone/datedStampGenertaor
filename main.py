from PIL import Image as img
import random
import os
import errno
############################
#Start date

for y in range(2020,2026):
    for m in range(1,13):
        for d in range(1,32):
        
        
            ############################
            #generate random numbers
            variations = [14,2,2,2]
            
            randomVariations = [0,0,0,0]
            #for the circle
            randomVariations[0] = random.randint(1,variations[0])
            print(randomVariations[0])
            
            #for the day
            randomVariations[1] = random.randint(1,variations[1])
            print(randomVariations[1])
            
            #for the month
            randomVariations[2] = random.randint(1,variations[2])
            print(randomVariations[2])
            
            #for the year
            randomVariations[3] = random.randint(1,variations[3])
            print(randomVariations[3])
        
        
            #import elements
            
            circle = img.open(os.path.join("data/circles/" + str(randomVariations[0]) + ".png"), "r")
            day = img.open(os.path.join("data/days/" + str(d) + "/" + str(randomVariations[1]) + ".png"), "r")
            month = img.open(os.path.join("data/months/" + str(m) + "/" + str(randomVariations[2]) + ".png"), "r")
            year = img.open(os.path.join("data/years/" +  str(y) + "/" + str(randomVariations[3]) + ".png"), "r")
                        
            tampon = img.composite( circle, day, circle)
            tampon = img.composite( tampon, month, tampon)
            tampon = img.composite( tampon, year, tampon)
            
            # Rotate the stamp slightly
            tampon = tampon.rotate(random.randint(-10,10), img.BILINEAR)
            
            filename = "generated/" +  str(y) + "/" + str(m) + "/" + str(y) + "-" + str(m) + "-" + str(d) + ".png"
            if not os.path.exists(os.path.dirname(filename)):
                try:
                    os.makedirs(os.path.dirname(filename))
                except OSError as exc: # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise
            
            
            tampon.save(filename)
