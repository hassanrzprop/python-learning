import math
print(math.sqrt(4))
print(math.factorial(4))

# The math module in Python provides a wide range of mathematical functions and constants. Here are all the methods and constants available in the math module as of Python 3.8:

# Constants
# math.pi: The mathematical constant π.
# math.e: The mathematical constant e.
# math.tau: The mathematical constant τ (2π).
# math.inf: A floating-point positive infinity.
# math.nan: A floating-point “Not a Number” (NaN) value.




# Number-theoretic and representation functions
# math.ceil(x): Return the ceiling of x.
# math.copysign(x, y): Return a float with the magnitude of x but the sign of y.
# math.fabs(x): Return the absolute value of x.
# math.factorial(x): Return x factorial as an integer.
# math.floor(x): Return the floor of x.
# math.fmod(x, y): Return fmod(x, y).
# math.frexp(x): Return the mantissa and exponent of x as the pair (m, e).
# math.isfinite(x): Return True if x is neither an infinity nor a NaN.
# math.isinf(x): Return True if x is a positive or negative infinity.
# math.isnan(x): Return True if x is a NaN (not a number).
# math.isqrt(n): Return the integer square root of the non-negative integer n.
# math.ldexp(x, i): Return x * (2**i).
# math.modf(x): Return the fractional and integer parts of x.
# math.trunc(x): Return the truncated integer value of x.




# Power and logarithmic functions
# math.exp(x): Return e**x.
# math.expm1(x): Return e**x - 1.
# math.log(x[, base]): Return the logarithm of x to the given base.
# math.log1p(x): Return the natural logarithm of 1+x.
# math.log2(x): Return the base-2 logarithm of x.
# math.log10(x): Return the base-10 logarithm of x.
# math.pow(x, y): Return x raised to the power y.
# math.sqrt(x): Return the square root of x.





# Trigonometric functions
# math.acos(x): Return the arc cosine of x.
# math.asin(x): Return the arc sine of x.
# math.atan(x): Return the arc tangent of x.
# math.atan2(y, x): Return atan(y / x).
# math.cos(x): Return the cosine of x.
# math.sin(x): Return the sine of x.
# math.tan(x): Return the tangent of x.
# Angular conversion



# math.degrees(x): Convert angle x from radians to degrees.
# math.radians(x): Convert angle x from degrees to radians.



# Hyperbolic functions
# math.acosh(x): Return the inverse hyperbolic cosine of x.
# math.asinh(x): Return the inverse hyperbolic sine of x.
# math.atanh(x): Return the inverse hyperbolic tangent of x.
# math.cosh(x): Return the hyperbolic cosine of x.
# math.sinh(x): Return the hyperbolic sine of x.
# math.tanh(x): Return the hyperbolic tangent of x.




# Special functions
# math.erf(x): Return the error function at x.
# math.erfc(x): Return the complementary error function at x.
# math.gamma(x): Return the Gamma function at x.
# math.lgamma(x): Return the natural logarithm of the absolute value of the Gamma function at x.



# Utility functions
# math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0): Return True if the values a and b are close to each other.
# math.prod(iterable, *, start=1): Calculate the product of all the elements in the input iterable.
# math.dist(p, q): Return the Euclidean distance between points p and q.
# math.hypot(*coordinates): Return the Euclidean norm, sqrt(sum(x**2 for x in coordinates)).