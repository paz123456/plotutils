import matplotlib.pyplot as plt
import pandas as pd


def add_watermark(fig, text, fontsize=None, xy=(0.95, 0.05), alpha=0.5, color="gray"):
    """
    Add a watermark to the lower right corner of a matplotlib figure.

    Parameters:
    - fig: matplotlib.figure.Figure
        The figure object to which the watermark will be added.
    - text: str, optional
        The watermark text to add. Default is 'Watermark'.
    - fontsize: int, optional
        The font size of the watermark text. Default is 12.
    - xy: tuple with position of text in figure coordinates. Default is (.95, .05)
    - alpha: float, optional
        The transparency level of the watermark text. Default is 0.5.
    - color: str, optional
        The color of the watermark text. Default is 'gray'.
    """
    if isinstance(text, pd.Timestamp):
        text = text.strftime("%Y-%m-%d %H:%M:%S")
        fontsize = 8
    if fontsize:
        fig.text(
            xy[0],
            xy[1],
            text,
            fontsize=fontsize,
            alpha=alpha,
            color=color,
            ha="right",
            va="bottom",
            transform=fig.transFigure,
        )
    else:
        fig.text(
            xy[0],
            xy[1],
            text,
            alpha=alpha,
            color=color,
            ha="right",
            va="bottom",
            transform=fig.transFigure,
        )
