def score(x, y):
# Idea: if a dart is in a circle of radius 1, then its distance to the origin, 
# given by (x^2 + y^2 )^0.5 must be less than or equal to 1.
    distance = ( x**2 + y**2 )**0.5
    if distance <=1: 
        return 10
    elif distance <= 5:
        return 5
    elif distance <= 10: 
        return 1
    else:
        return 0