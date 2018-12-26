import matplotlib.pyplot as plt


def make_plot(num, title, scale):
    fig, ax = plt.subplots(num=num)

    fig.suptitle(title)

    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_smart_bounds(True)
    ax.spines['bottom'].set_smart_bounds(True)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    ax.grid(linestyle='dashed')
    ax.axis(scale)

    return fig, ax
