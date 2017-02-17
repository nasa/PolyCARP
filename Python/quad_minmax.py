"""
quad_minmax - algorithms to determine properties of the minimum of a quadratic on an interval

Contact: Anthony Narkawicz (anthony.narkawicz@nasa.gov), George Hagen (george.hagen@nasa.gov)

Copyright (c) 2015-2016 United States Government as represented by
the National Aeronautics and Space Administration.  No copyright
is claimed in the United States under Title 17, U.S.Code. All Other
Rights Reserved.
"""

def quadratic(a,b,c,x):
    return a*x**2+b*x+c

def quad_min_int(a,b,c,xl,xu):
    if (a<=0 and quadratic(a,b,c,xl)>=quadratic(a,b,c,xu)):
        return xu
    elif a<=0:
        return xl
    elif 2*a*xl<=-b and -b<=2*a*xu:
        return -b/(2*a)
    elif -b<2*a*xl:
        return xl
    else:
        return xu

def quad_min_le_D_int(ap,b,c,xl,xu,D):
    if xl>xu:
        return False
    elif 2*ap*xl<=-b and -b<=2*ap*xu:
        return (b**2-4*ap*(c-D)>0)
    elif quadratic(ap,b,c-D,xl)<0 or quadratic(ap,b,c-D,xu)<0:
        return True
    else:
        return False
