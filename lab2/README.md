# Vision Based Positioning

### Data Collection

![](./KaurCuup.svg)


In order to determine the accuracy of PoseNet at determining the position of the turtlebot, a ground truth value had to be determined. This was done using a VICON object tracking system. To verify this system's measurements are accurate enough to be considered a ground truth, preliminary experiments were conducted. Specifically, a sensor was placed along a tape measure at regular intervals of 50 cm and the position estimation of the VICON system was observed. The estimated position of the sensor  varying with time is shown below.
![](./pos.svg)

For an completely accurate sensor tracking system, we would expect the differences in the height of the plateaus in the graph above to be 50 cm. These values from the VICON system are shown below.
![](./distdiff.png)

As expected the VICON system appears to be very accurate, with a mean error of less than a milimeter. In reality the error could be even lower as we would expect roughly the same level of precision from placing the sensor.

### Turtlebot
It is important to synchronise the turtlebot time with the time of the cameras. This allows us to later compare the predicted motion data with the real data. A visual or sound signal could be used to synchronise the streams, similar to clapperboards that are used in movies. Also, when the devices are connected to the internet, NTP could be used to synchronise both streams with respect to UTC.





<img src="./expxyz.svg" alt="./expxyz.svg" height = "360" width="360"/><img src="./expangle.svg" alt="./expangle.svg" height = "360" width="360"/>


|Error| Mean | Median | Min | Max | 
|------|------  |------  |------  |------  |
|   Translation |  1.423 | 0.974 | 0.02 | 3.97 |
|   Rotation |  26 | 11 | 0.2 | 180|



<img src="./origxyz.svg" alt="./origxyz.svg" height = "360" width="360"/><img src="./origangle.svg" alt="./origangle.svg" height = "360" width="360"/>

|Error| Mean | Median | Min | Max | 
|------|------  |------  |------  |------  |
|   Translation |  0.706 | 0.595 | 0.01 | 4.40 |
|   Rotation |  8.59 | 5.08 | 0.2 | 171|




![](./viconerr.svg)

Images that gave the smallest error in position prediction

| ![space-1.jpg](./bestimages/2019-01-31-14-42-03-236518.png) | ![](./bestimages/2019-01-31-14-43-51-731422.png) | ![](./bestimages/2019-01-31-14-43-59-991355.png) |
|:--:|:--:|:--:| 
| *6376* |*9635*|*9883*|

| ![space-1.jpg](./worstimages/2019-01-31-14-38-57-806163.png) | ![](./worstimages/2019-01-31-14-39-46-309718.png) | ![](./worstimages/2019-01-31-14-39-47-973832.png) |
|:--:|:--:|:--:| 
| *2263* |*806*|*2313*|

