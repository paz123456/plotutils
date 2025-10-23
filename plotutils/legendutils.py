import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.collections import PatchCollection
from matplotlib.legend_handler import HandlerBase
from matplotlib.patches import PathPatch
from matplotlib.markers import MarkerStyle
import matplotlib as mpl


class HandlerGradientLine(HandlerBase):
    """Draw a horizontal gradient line as the legend handle.
        Example:
    # --- make a dummy handle for the gradient entry
    grad_handle = Line2D([], [], label="Dust trajectory (speed)")

    # keep your existing scatter legend entry and append the gradient handle
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(
        handles + [grad_handle],
        labels + ["Dust trajectory (speed)"],
        loc="upper right",
        handler_map={grad_handle: HandlerGradientLine(cmap="cool", lw=2)},
    )
    """

    def __init__(self, cmap="cool", n=256, lw=2, **kwargs):
        super().__init__(**kwargs)
        self.cmap = plt.get_cmap(cmap) if isinstance(cmap, str) else cmap
        self.n = int(n)
        self.lw = lw

    def create_artists(
        self, legend, orig_handle, x0, y0, width, height, fontsize, trans
    ):
        xs = np.linspace(x0, x0 + width, self.n)
        y = y0 + 0.5 * height
        segs = [((xs[i], y), (xs[i + 1], y)) for i in range(self.n - 1)]
        cols = self.cmap(np.linspace(0, 1, self.n - 1))
        lc = LineCollection(segs, colors=cols, linewidths=self.lw, transform=trans)
        return [lc]


class MulticolorCircles:
    def __init__(
        self, face_colors, edge_colors=None, face_alpha=1, radius_factor=1, gap=0.4
    ):
        """
        Helper to have nice legend entrance for scatter plots with same marker
        but change of color.
        gap : float   – extra spacing between dots, in diameters (0 = touching)

        Use like:

        n_points = 3
        # get n_points distinct colors
        # n_points is the number of markers shown in the legend

        cmap = cm.get_cmap("brg_r", n_points)

        handles, labels = fig.axes[0].get_legend_handles_labels()

        # rgba ➜ hex strings (handy for MulticolorCircles)
        brg_r_hex = [mcolors.to_hex(cmap(i)) for i in range(cmap.N)]

        multi_dot_handle = MulticolorCircles(brg_r_hex, radius_factor=3.4, gap=1.9)
        handles.append(multi_dot_handle)
        labels.append("MyLabel")

        fig.legend(
            handles,
            labels,
            handlelength=1.5,
            handler_map={MulticolorCircles: MulticolorHandler},
        )



        """
        assert 0 <= face_alpha <= 1, "face_alpha must be in [0,1]"
        assert radius_factor > 0, "radius_factor must be positive"
        assert gap >= 0, "gap must be non-negative"

        self.fc = [mcolors.to_rgba(c, alpha=face_alpha) for c in face_colors]
        self.ec = edge_colors or ["none"] * len(self.fc)
        self.N = len(self.fc)
        self.rad_factor = radius_factor
        self.gap = gap

    # ------------------------------------------------------------------ helpers
    def _radius_and_chunk(self, width, height):
        """Return (radius, chunk width actually used for one dot)."""
        # total width taken up by gaps:
        total_gap = (self.N - 1) * self.gap
        # each "unit" = one diameter; diam + gap*diam + diam ...
        diam = width / (self.N + total_gap)
        radius = min(diam / 2, height / 2) * self.rad_factor
        return radius, diam

    def get_patch(self, width, height, idx, fc, ec):
        radius, diam = self._radius_and_chunk(width, height)
        # x-centre: idx * (diam + gap*diam) + radius
        x = (idx * (1 + self.gap) + 0.5) * diam
        y = height / 2  # vertical centring
        return plt.Circle((x, y), radius, facecolor=fc, edgecolor=ec)

    # ------------------------------------------------------------------ callable
    def __call__(self, width, height):
        patches = [
            self.get_patch(width, height, i, fc, ec)
            for i, (fc, ec) in enumerate(zip(self.fc, self.ec))
        ]
        return PatchCollection(patches, match_original=True)


class MulticolorHandler:
    """ """

    @staticmethod
    def legend_artist(legend, orig_handle, fontsize, handlebox):
        """ """
        width, height = handlebox.width, handlebox.height
        patch = orig_handle(width, height)
        handlebox.add_artist(patch)
        return patch
