# Sensor Networks Lab


### Signal Variability

We found the signal to vary significantly with minor variations in the surrounding environment. 
- A wooden door at 1Mand detector at 2M realized an attenuation of 5dB.
- A person sitting at 1M and detector placed at 2M realized an attenuation of ~3dB, only when the transmitter was perfectly blocked.  
- Numerous orientations had a varying degree of attenuation. The phone placed flat achieved -43dB signal strength, vertically it achieved -45dB and horizontally it achieved -50dB. 

The challenge with obtaining a perfect representation of these signals is the fact that there is human interaction, particularly in the case of phone orientation when a person has to hold the device and can block/interfere the signal.



### Path Loss

Below you can see a figure of signal strength as a function of distance. The experiment was then repeated three times and the data is visible in the graph below. Each distance was not repeatedly measured to avoid autocorrelation. The green triangles series shows the average of the three measured series along with least-squares trendline. The black line is added for comparison of the slope to the theoretical model

![](./RSSI-vs-distance.svg)

Theoretically, the signal should decrease proportionally to the distance squared, however, there are reflections from walls, floor, ceiling, people and objects in the room. In reality the signal days slightly slower than the theoritical model. This caused variations in the signal, some of them are consistent between different series which implies it was caused by the geometry of the room. The differences between different runs are most likely caused by the moving people, different phone placement and vvariation in the transmitted signal.

### Horus on synthetic data

<img src="./histogramAP1.svg" alt="./histogramAP1.svg" width="240"/><img src="./histogramAP2.svg" alt="./histogramAP2.svg" width="240"/><img src="./histogramAP3.svg" alt="./histogramAP3.svg" width="240"/>

The signal variation is modelled as a Gaussian distribution. Gassian distributions is good choice as several of the sources for the signal variation (thermal noise on the transmitter and receiver, air composition and density on the path, etc) can be modelled as Gaussian noise. Hence, the overall variation is Gaussian as well. Each source at each location results in a gaussian with a mean and standard deviation. Using this information, we can compute the log likelihood of a test point against this gaussian and some the losses across access points at a given location. For example, if we have 63 fixed training locations, we will have 63 losses. We can feed these losses through a softmax to obtain probabilities. We can then use all these probabilities or the top K to weight the positions and obtain an average.



#### Set 1 : 3 AP's

Top 1 Probability Results

<img src="./images/path1_top1.svg" alt="./images/path1_top1.svg" width="360"/><img src="./images/error1_top1.svg" alt="./images/error1_top1.svg" width="360"/>


Top 5 Probability Results

<img src="./images/path1_5top.svg" alt="./images/path1_5top.svg" width="360"/><img src="./images/error1_5top.svg" alt="./images/error1_5top.svg" width="360"/>

Top 10 Probability Results

<img src="./images/path1_10top.svg" alt="./images/path1_10top.svg" width="360"/><img src="./images/error1_10top.svg" alt="./images/error1_10top.svg" width="360"/>


#### Set 2 : 5 AP's

Top 1 Probability Results

<img src="./images/path2_top1.svg" alt="./images/path2_top1.svg" width="360"/><img src="./images/error2_top1.svg" alt="./images/error2_top1.svg" width="360"/>


Top 5 Probability Results

<img src="./images/path2_5top.svg" alt="./images/path2_5top.svg" width="360"/><img src="./images/error2_5top.svg" alt="./images/error2_5top.svg" width="360"/>

Top 10 Probability Results

<img src="./images/path2_10top.svg" alt="./images/path2_10top.svg" width="360"/><img src="./images/error2_10top.svg" alt="./images/error2_10top.svg" width="360"/>



