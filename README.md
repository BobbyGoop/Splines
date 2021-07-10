# Splines representation in Python
### Description
Python application created for studying different splines with the help of matplotlib and numpy. Shows differences between Bezier splines (cubic and quadratic) and Catmull-Rom spline. In other words, the program tries to interpolate chosen function with theese splines and calculate the mean deviation between the origin and the result, adjusting the number of anchor points (obviously, the larger the number, the more accurate the result).
### Usage
The usage of the programm seems to be like this:
1. Come up with some function and its upper and lower limits 
2. Choose the needed number of anchor points (they are equidistant from each other according to the X-axis, but still belong to base fx)
3. Study the results
<br/>
Note that bezier splines must have  middle points just to make the whole chain smooth, and they do not belong to base fx
### Polynomial interpolation
Also includes interpolation of function (in this case the base function cannot be changed) with polynomial according to 5, 8, 13, or 18 anchor points (mutliplires are pre-calculated in Excel, one of the main goal is to calculate them in Python and make polynomial interpolation universal)
