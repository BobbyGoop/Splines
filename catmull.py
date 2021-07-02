import numpy as np
from basic_fx import main_func

def catmull_chain(x_or, y_or, p_num):
	cx = list()
	cy = list()
	dots_count, div_av = 0, 0
	for j in range(p_num - 1):
		for t in np.linspace(0, 1, 100):
			xt = (-t * (1 - t) ** 2 * x_or[j] + (2 - 5 * t ** 2 + 3 * t ** 3) * x_or[j + 1] + t * (1 + 4 * t - 3 * t ** 2) * x_or[j + 2] - t ** 2 * (1 - t) * x_or[j + 3]) / 2
			yt = (-t * (1 - t) ** 2 * y_or[j] + (2 - 5 * t ** 2 + 3 * t ** 3) * y_or[j + 1] + t * (1 + 4 * t - 3 * t ** 2) * y_or[j + 2] - t ** 2 * (1 - t) * y_or[j + 3]) / 2
			# if j != 0 and j != p_num - 3:
			div_av += abs((main_func(xt)) - yt)
			cx.append(xt)
			cy.append(yt)
			dots_count += 1
	return cx, cy, div_av / dots_count

