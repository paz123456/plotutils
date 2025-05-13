import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.collections import PatchCollection     

class MulticolorCircles:
    def __init__(self, face_colors, edge_colors=None, face_alpha=1,
                 radius_factor=1, gap=0.4):
        """
        gap : float   – extra spacing between dots, in diameters (0 = touching)
        """
        assert 0 <= face_alpha <= 1, "face_alpha must be in [0,1]"
        assert radius_factor > 0,    "radius_factor must be positive"
        assert gap >= 0,             "gap must be non-negative"

        self.fc  = [mcolors.to_rgba(c, alpha=face_alpha) for c in face_colors]
        self.ec  = edge_colors or ["none"] * len(self.fc)
        self.N   = len(self.fc)
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
        y = height / 2                           # vertical centring
        return plt.Circle((x, y), radius, facecolor=fc, edgecolor=ec)

    # ------------------------------------------------------------------ callable
    def __call__(self, width, height):
        patches = [
            self.get_patch(width, height, i, fc, ec)
            for i, (fc, ec) in enumerate(zip(self.fc, self.ec))
        ]
        return PatchCollection(patches, match_original=True)

class MulticolorHandler:
    """
    """
    @staticmethod
    def legend_artist(legend, orig_handle, fontsize, handlebox):
        """
        """
        width, height = handlebox.width, handlebox.height
        patch = orig_handle(width, height)
        handlebox.add_artist(patch)
        return patch

