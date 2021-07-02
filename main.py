import numpy as np
import matplotlib.pyplot as plt
import basic_fx
from math import pi
from bezier_cube import cubic_bezier
from bezier_quad import quadratic_bezier
from catmull import catmull_chain
from polynom import polynomial_fx



SPLINE_POINTS = 7


def generate_bezier_dots(number = 100):
	x = np.linspace(basic_fx.LOWER_LIMIT, basic_fx.UPPER_LIMIT, number)

	if number < 100:
		if len(x) % 4 != 0:
			while len(x) % 4 != 0:
				x = np.insert(x, -1, x[-1])
		else:
			x = np.insert(x, -1, x[-1])
			x = np.insert(x, -1, x[-1])

	y = np.empty((len(x)))
	for i in range(len(y)):
		y[i] = basic_fx.main_func(x[i])
	return x, y


if __name__ == "__main__":
	fig, axes = plt.subplots(2, 2, figsize=(16, 10))
	plt.suptitle(f"Number of anchor points (except polynom): {SPLINE_POINTS}")
	x_out, y_out = generate_bezier_dots()
	x_origin, y_origin = generate_bezier_dots(SPLINE_POINTS)

	# Drawing cubic bezier
	b_cubex, b_cubey, mx, my, b_cube_div = cubic_bezier(x_origin, y_origin)
	axes[0, 1].set_title(f"Cubic Bezier (Mean deviation: {round(b_cube_div * 100, 4)}%)")
	axes[0, 1].scatter(x_origin, y_origin, c="blue", label='Anchor points', s=15)
	axes[0, 1].scatter(mx, my, c='red', s=15, label="Middle points")
	axes[0, 1].plot(x_out, y_out, c="green", linewidth=1, label="f(x)")
	axes[0, 1].plot(b_cubex, b_cubey, c="blue", label='Cubic bezier', linewidth=1)

	# Drawing quadratic bezier
	b_quadx, b_quady, mx, my, b_quad_div = quadratic_bezier(x_origin, y_origin)
	axes[0, 0].set_title(f"Quadratic Bezier (Mean deviation: {round(b_quad_div * 100, 4)}%)")
	axes[0, 0].scatter(mx, my, c='red', s=15, label="Middle points")
	axes[0, 0].scatter(x_origin, y_origin, c="blue", label='Anchor points', s=15)
	axes[0, 0].plot(b_quadx, b_quady, c="blue", label='Quadratic bezier', linewidth=1)
	axes[0, 0].plot(x_out, y_out, c="green", linewidth=1, label="f(x)")

	# Drawing Catmull - Rom
	anchor_cx = np.linspace(basic_fx.LOWER_LIMIT, basic_fx.UPPER_LIMIT, SPLINE_POINTS)
	anchor_cx = np.insert(anchor_cx, 0, anchor_cx[0])
	anchor_cx = np.insert(anchor_cx, -1, anchor_cx[-1])
	anchor_cy = np.empty(len(anchor_cx))
	for i in range(SPLINE_POINTS):
		anchor_cy[i] = basic_fx.main_func(anchor_cx[i])

	cat_x, cat_y, cat_div = catmull_chain(anchor_cx, anchor_cy, SPLINE_POINTS)
	axes[1, 0].set_title(f"Catmull-Rom Spline (Mean deviation: {round(cat_div* 100, 4)}%)")
	axes[1, 0].scatter(x_origin, y_origin, c="blue", label='Anchor points', s=15)
	axes[1, 0].plot(x_out, y_out, c="green", linewidth=1, label="f(x)")
	axes[1, 0].plot(cat_x, cat_y, c="blue", label="Catmull-Rom spline", linewidth=1)

	# ONLY FOR DRAWING POLYNOMIAL REPRESENTATION
	# The number of anchor points for polynom that
	# belong to f(x) = 2sin(x) + 1.5sin(2x) function
	# (should not be changed unlike bezier and catmull splines)
	POLY_NUMB = 13
	UPPER_PL = 0
	LOWER_PL = 7

	anchor_px = np.linspace(0, 2 * pi, POLY_NUMB)
	anchor_py = 2*np.sin(anchor_px) + 1.5 * np.sin(2*anchor_px )

	out_fx = np.linspace(0, 2 * pi, 100)
	out_px = np.linspace(LOWER_PL, UPPER_PL, 100)
	out_fy = 2*np.sin(out_fx) + 1.5 * np.sin(2*out_fx)
	out_py = polynomial_fx(out_px, POLY_NUMB)

	axes[1, 1].set_title(f"Polynomial representation ({POLY_NUMB} an. p.)")
	axes[1, 1].scatter(anchor_px, anchor_py,  c="red", label='Anchor points (for poly only)', s=15)
	axes[1, 1].plot(out_px, out_py, c="blue", label="Polynom", linewidth=1)
	axes[1, 1].plot(out_fx, out_fy, c="red", linewidth=1, label="f(x) (constant)")

	for ax in fig.get_axes():
		ax.label_outer()
		ax.legend(loc=3)
		ax.grid()
	fig.canvas.manager.set_window_title('Splines comparison')
	plt.subplots_adjust(left=0.03, bottom=0.04, top=0.92, right=0.97, wspace = 0.05, hspace= 0.125)
	plt.show()
