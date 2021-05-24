from PIL import Image
import numpy as np
import math

fileName = "Images/rotate.png"
image = np.array(Image.open(fileName))             
angle=int(input("Angle: "))               


angle=math.radians(angle)                               
cosine=math.cos(angle)
sine=math.sin(angle)
height=image.shape[0]                                   
width=image.shape[1]                                   


# Define the height and width of the rotated bound
rotatedHeight  = abs(round(abs(image.shape[0]*cosine)+abs(image.shape[1]*sine)))
rotatedWidth  = abs(round(abs(image.shape[1]*cosine)-abs(image.shape[0]*sine)))


result = np.zeros((rotatedHeight,rotatedWidth,image.shape[2]))

# Centroid of the original
originalCentroidY   = round(((image.shape[0])/2))    
originalCentroidX    = round(((image.shape[1])/2))   

# Centroid of the resultant image
rotatedCentroidY= round(((rotatedHeight)/2))        
rotatedCentroidX= round(((rotatedWidth)/2))         

for i in range(height):
    for j in range(width):
        #co-ordinates of the pixels with respect to the centroid of original image
        y=image.shape[0]-i-originalCentroidY                
        x=image.shape[1]-j-originalCentroidX                   

        #Transformation
        rotatedY=round(-x*sine+y*cosine)
        rotatedX=round(x*cosine+y*sine)

        #Change of origin
        rotatedY=rotatedCentroidY-rotatedY
        rotatedX=rotatedCentroidX-rotatedX

        #Condition to prevent absurd values
        if 0 <= rotatedX < rotatedWidth and 0 <= rotatedY < rotatedHeight and rotatedX>=0 and rotatedY>=0:
            result[rotatedY,rotatedX,:]=image[i,j,:]                        

rotatedImg=Image.fromarray((result).astype(np.uint8))
rotatedImg