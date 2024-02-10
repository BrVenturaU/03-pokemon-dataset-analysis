import matplotlib.pyplot as plt


def plot_pie_chart(x, labels, figsize, explode_by=0.1, title="", autopct="%1.1f%%"):
    x_explode = x.map(lambda val: explode_by if val == x.max() else 0)
    plt.figure(figsize=figsize)
    plt.pie(x, labels=labels, explode=x_explode, autopct=autopct)
    plt.legend()
    plt.title(title)