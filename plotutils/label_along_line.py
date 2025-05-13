import numpy as np


def add_label_along_line(

    ax, slope, intercept, x_text, text, **text_kw  # y = slope*x + intercept
):
    """
    Place `text` at (x_text, y_line(x_text)) and rotate it so it follows y = slope*x + intercept.
    Works for any aspect ratio because the rotation is computed in display space.
    """
    # y position where the text is anchored
    y_text = slope * x_text + intercept

    # choose two widely separated points on the same line
    x1, x2 = ax.get_xlim()  # use current x‑limits for robustness
    y1, y2 = slope * x1 + intercept, slope * x2 + intercept

    # transform those two points to display (pixel) coordinates
    (x1_d, y1_d), (x2_d, y2_d) = ax.transData.transform([(x1, y1), (x2, y2)])

    # angle in display space (degrees)
    angle_disp = np.degrees(np.arctan2(y2_d - y1_d, x2_d - x1_d))

    # finally draw the text
    ax.text(
        x_text, y_text, text, rotation=angle_disp, rotation_mode="anchor", **text_kw
    )
