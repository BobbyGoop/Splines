import numpy as np
from basic_fx import main_func


def cubic_bezier(px, py):
	bx = list()
	by = list()
	mx = list()
	my = list()
	x1 = px[0]
	y1 = py[0]
	dots_count, div_av = 0, 0

	for j in range(0, len(px)-2, 2):
		print(j)
		x_mid = (px[j + 2] + px[j + 3]) / 2
		y_mid = (py[j + 2] + py[j + 3]) / 2
		mx.append(x_mid)
		my.append(y_mid)
		for t in np.linspace(0, 1, 200):
			xt = (((1 - t) * x1 + 3 * t * px[j + 1]) * (1 - t) + 3 * t ** 2 * px[j + 2]) * (1 - t) + t ** 3 * x_mid
			yt = (((1 - t) * y1 + 3 * t * py[j + 1]) * (1 - t) + 3 * t ** 2 * py[j + 2]) * (1 - t) + t ** 3 * y_mid
			bx.append(xt)
			by.append(yt)
			div_av += abs((main_func(xt) - yt))
			dots_count += 1
		x1 = x_mid
		y1 = y_mid


	return bx, by, mx, my, div_av/dots_count