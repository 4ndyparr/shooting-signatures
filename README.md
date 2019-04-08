# shooting-signatures
An at-a-glance view of a soccer shooting performance relative to location

![Signatures Mosaic](https://github.com/4ndyparr/shooting-signatures/blob/master/mosaic_wedge_.png)

## about
Soccer Shooting Signatures is a data visualization project based on the *shooting signatures* developed by Peter Beshai for [Buckets](http://buckets.peterbeshai.com), an interactive NBA visualization tool. The idea was to apply the same concept (an at-a-glance view of a shooting performance relative to location) for soccer.

![Tesselation](https://github.com/4ndyparr/shooting-signatures/blob/master/tesselation.png)

Similarly to basketball, in soccer, *distance* (to the goal) is the single most important location-related factor that explains shooting percentages (check the figure above for a visual demostration), with the other important factor being the *angle* (and it has itself a strong correlation with distance). So I decided to apply the same signature technique to soccer shooting data to see what insights it can bring.

![Sample](https://github.com/4ndyparr/shooting-signatures/blob/master/distance.png)

The first problem I had to tackle was what to consider *distance to the goal*. Unlike basketball, where the distance is simply the distance to the hoop, in soccer the distance to the goal is relative. Are we considering the shortest distance to any part of the goal? Or the distance to a particular point of it, like the middle? Also it could be interesting a *distance differential* than is parallel to the boxes, this way we could easily divide the signature in more significative areas. I finally went for the model of the right.

![Sample](https://github.com/4ndyparr/shooting-signatures/blob/master/sample.png)

The signature, for each distance to the goal, represents the goal percentage for the shots within that distance as the *height* of the signature at that distance, and the number of shots as its *width*, with the difference in goal percentage between a particular player and the average (the average goal percentage of all players) represented with a *colormap*. This way, looking at a players' signature you can see in a glimpse the absolute and relative shooting accuracy and the shooting volume of a player across the different distances.
