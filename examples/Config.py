import matplotlib.pyplot as plt

def plot_config():

    SMALL_SIZE = 8
    MEDIUM_SIZE = 12
    BIGGER_SIZE = 24

    params = {
        'backend': 'pdf',
        'axes.labelsize': 10,
        'legend.fontsize': 10,
        'xtick.labelsize': 8,
        'ytick.labelsize': 8,
        'text.usetex': True,
    }

    plt.rcParams.update(params)
    plt.rc('text.latex', preamble=r'\usepackage{graphicx} \usepackage{grffile} \usepackage{siunitx} \usepackage{mhchem} \DeclareSIUnit[number-unit-product = {}]\calorie{cal}')
    plt.rcParams["legend.frameon"] = False
    plt.rcParams["legend.handlelength"] = 1.2
    plt.rcParams["xtick.direction"] = "in"
    plt.rcParams["ytick.direction"] = "in"
    plt.rcParams["xtick.top"] = True
    plt.rcParams["ytick.right"] = True

    plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)     # fontsize of the x and y labels
    plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labelsize
    plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
    plt.rc('lines', linewidth=1)			 # line width
    plt.rc('lines', markersize=3)			 # marker size
    plt.rc('figure', titlesize=40)

def my_formatter(x, pos):
    if x.is_integer():
        return '$'+str(int(x))+'$'
    else:
        return '$'+str(round(x,5))+'$'

