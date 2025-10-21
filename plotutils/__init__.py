__version__ = "0.0.0"
__author__ = "Philipp Ziegler"


from .colored_line import colored_line
from .watermark import add_watermark
from .figuresize import set_size
from .setup_latex import setup_latex
from .discrete_cmap import discrete_cmap
from .legendutils import MulticolorCircles, MulticolorHandler


__all__ = ["colored_line", "add_watermark", "set_size", "setup_latex", "discrete_cmap"]
