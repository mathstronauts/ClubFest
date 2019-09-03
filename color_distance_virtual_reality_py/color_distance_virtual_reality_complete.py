from visual import*
import serial

## Create a serial object
arduinoData = serial.Serial('com7',115200)

## Create a scene
scene = display(title='Virtual World')
## Number of pixels by width and height
scene.width = 800
scene.height = 800
scene.autoscale = False
## Range of scene is 12x12x12 inches
scene.range = (12,12,12)

## Create Ultrasonic
back = box(length = 1 , width=10, height=5 , pos=(-8.5,0,0),color= (0,0,1))
cylinder1 = cylinder(pos=(-8.5,0,2.5),radius=1.5,length=2.5)
cylinder2 = cylinder(pos=(-8.5,0,-2.5),radius=1.5,length=2.5)

# Create pad
pad = box(length = 0.1 , width=6, height=6 , pos=(-6,0,0),color= (1,0,0))


## Start live coding here
    
while True:
    pass
    ## iterate through loop 30 times per second
    rate(30)

    ## Read from serial communication
    data = arduinoData.readline()

    ## data looks like this at the momemt:
    ##     "RED value,GREEN value, BLUE value, distance"

    ## split this line up into its individual components
    dataNums = data.split(',')
    ## dataNums now look like this:
    ##      ["RED value","GREEN value","BLUE value","distance"]
    ## PLEASE NOTE: Values are in strings (not appropriate for math operations)
    ## We will need to convert them to numerical data types
    ## But first check to make sure all data was recieved properly over serial
    ## to check make sure the length of dataNums is 4 (R,G,B and distance)
    if len(dataNums)==4:
        ## if 4 data was recieved convert the colors to integers and the...
        ## distance to float(decimal)
        ## PLEASE NOTE: to access the individual data you have to index the value...
        ## that is needed.
        ## Recall when we sent the data from arduino they were sent in the following...
        ## order: R,G,B,distance
        ## Therefore the first element in the dataNum array is our red value, the second...
        ## is green and so on
        ## the first element of the dataNum array is index 0, the second is 1 etc
        red = int(dataNums[0])
        green = int(dataNums[1])
        blue = int(dataNums[2])
        distance = float(dataNums[3])
        # convert distance to inches
        distance = distance*0.4
        if distance< 1.6:
            pad.color = (red/255, green/255, blue/255)
        if distance< 10.8:
        ## Note: We are starting at -6, where the US cylinder stops in the x axis
            pad.pos = vector((-6+distance),0,0)

