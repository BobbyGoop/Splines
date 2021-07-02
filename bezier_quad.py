import numpy as np
from basic_fx import main_func


def quadratic_bezier(px, py):
	bx = list()
	by = list()
	mx = list()
	my = list()
	x1 = px[0]
	y1 = py[0]
	dots_count, div_av = 0, 0
	for j in range(len(px) - 2):
		x_mid = (px[j + 1] + px[j + 2]) / 2
		y_mid = (py[j + 1] + py[j + 2]) / 2
		mx.append(x_mid)
		my.append(y_mid)
		for t in np.linspace(0, 1, 100):
			xt = (1 - t) ** 2 * x1 + 2 * t * (1 - t) * px[j + 1] + t ** 2 * x_mid
			yt = (1 - t) ** 2 * y1 + 2 * t * (1 - t) * py[j + 1] + t ** 2 * y_mid
			bx.append(xt)
			by.append(yt)
			div_av += abs((main_func(xt) - yt))
			dots_count += 1
		x1 = x_mid
		y1 = y_mid

	return bx, by, mx, my, div_av / dots_count