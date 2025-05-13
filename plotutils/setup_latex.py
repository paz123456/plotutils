import matplotlib.pyplot as plt


def setup_latex():
    plt.rcParams.update(
        {
            "text.usetex": True,
            "text.latex.preamble": r"\usepackage{amsmath}\usepackage{amssymb} \usepackage{upgreek}",
        }
    )
