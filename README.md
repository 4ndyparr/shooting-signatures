# shooting-signatures
An at-a-glance view of a soccer shooting performance relative to location

![Signatures Mosaic](https://github.com/4ndyparr/shooting-signatures/blob/master/mosaic_wedge.png)

## about
Soccer Shooting Signatures is a data visualization project based on the *shooting signatures* developed by Peter Beshai for [Buckets](http://buckets.peterbeshai.com), an interactive NBA visualization tool. The idea was to apply the same concept (an at-a-glance view of a shooting performance relative to location) for soccer.

![Tesselation](https://github.com/4ndyparr/shooting-signatures/blob/master/tesselation.png)

Similarly to basketball, in soccer, *distance* (to the goal) is the single most important location-related factor that explains shooting percentages (check the figure above for a visual demostration), with the other important factor being the *angle* (and it has itself a strong correlation with distance). So I decided to apply the same signature technique to soccer shooting data to see what insights it can bring.

![Sample](https://github.com/4ndyparr/shooting-signatures/blob/master/sample_wedge_all_2.png)

For each distance to the goal, the goal percentage for the shots within that distance is represented as the *height* of the signature at that distance, and the number of shots as its *width*, with the difference in goal percentage between a particular player and the average (the average goal percentage of all players) represented with a *colormap*. This way, looking at a players' signature you can see in a glimpse the absolute and relative shooting accuracy and the shooting volume of a player across the different distances.
