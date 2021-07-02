import sys
import numpy as np

# Multipliers are calculated in Excel so
# the polynomial goes through the exact anchor points
# that belong to one certain function (check main)
# The number of possible anchor points is STRICTLY LIMITED
multipliers = {5: [0, 0.17200818364373, -1.6211389382774, 3.3953054526271, 0],

	8: [-0.014177499, 0.311779498, -2.652033233, 10.88663753, -21.6122004, 16.86422734, -0.679182359, 0],

	13: [0, -0.0000400884541, 0.0013853575283, -0.0199512320358, 0.1539198727658, -0.6821029074083, 1.7571644392306, -2.7821631046006, 3.8251969439947, -5.1868666635168, 1.1845366617900, 4.7959909107526, 0],

	18: [-5.477215935383380, -0.000000000688203, 12.655216149234000, 0.000000001503793, -11.489347457871000, -0.000000001235833, 5.134349971294820, 0.000000000601943, -1.245683733807840, -0.000000000228596, 0.101422210870946,
		 0.000000000057648, -0.083025157006375, -0.000000000005725, -0.166511929173567, 0.000000000000127, -1.000000445218090, 1.570796326794900]}


def polynomial_fx(x_values, npoly):
	try:
		if npoly not in multipliers.keys():
			raise IOError("ERROR: Incorrect polynom dots number")
		y_values = np.array([])
		for x in x_values:
			yet = 0
			for i in range(npoly):
				yet += multipliers[npoly][i] * x ** (npoly - 1 - i)
			y_values = np.append(y_values, yet)
		return y_values
	except IOError as e:
		print(e)
		sys.exit(-1)
