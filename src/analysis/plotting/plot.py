import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def get_colors():
    return np.array([
        [0.1, 0.1, 0.1],          # black
        [0.4, 0.4, 0.4],          # very dark gray
        [0.7, 0.7, 0.7],          # dark gray
        [0.9, 0.9, 0.9],          # light gray
        [0.984375, 0.7265625, 0], # dark yellow
        [1, 1, 0.9]               # light yellow
    ])


def color_bars(ax, colors):
    # Iterate over each subplot
    dark_color = colors[2]
    for p in ax.patches:
        p.set_edgecolor(dark_color)


def set_style(font_scale=1.0, style_rc=None):
    import seaborn as sns
    import matplotlib
    # This sets reasonable defaults for font size for
    # a figure that will go in a paper
    sns.set_context("paper")
    # Set the font to be serif, rather than sans
    # sns.set(font='serif')
    # sns.set(font_scale=font_scale)
    # if style_rc != None:
    sns.set(font='serif', font_scale=font_scale, rc=style_rc)
    # sns.set(font='serif', font_scale=font_scale)
    sns.set_style('whitegrid', {'axes.edgecolor': '.0', 'grid.linestyle': u'--',
                                'grid.color': '.8', 'xtick.color': '.15',
                                'xtick.minor.size': 3.0, 'xtick.major.size':
                                6.0, 'ytick.color': '.15', 'ytick.minor.size':
                                3.0, 'ytick.major.size': 6.0,
                                "font.family": "serif",
                                "font.serif": ["Times", "Palatino", "serif"]
                                # , "patch.linewidth":1.1
                                })
    matplot_colors = ["b", "g", "r", "c", "m", "y", "k", "w"]
    custom_colors = get_colors()
    sns.set_palette(custom_colors)
    matplotlib.rcParams['pdf.fonttype'] = 42
    matplotlib.rcParams['ps.fonttype'] = 42



def to_percent(y, position):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
    s = str(round(100 * y))
    
    # The percent symbol needs escaping in latex
    if matplotlib.rcParams['text.usetex'] is True:
        return s + r'$\%$'
    else:
        return s + '%'

formatter = FuncFormatter(to_percent)



def plot_bars(df, x="hardness", hue="split", system = "T5", order=None):
    # sns.set_style("whitegrid")
    set_style(font_scale=1.2)
    f, axs = plt.subplots(1, 3, figsize=(12, 4), sharey=True)
    if system:
        data = df[(df["db_id"]=="exp_v1") & (df["system"]==system)]
    else:
        data = df[(df["db_id"]=="exp_v1")]

    ncol = len(df[hue].unique())
    hue_order = sorted(df[hue].unique())
    sns.barplot(x=x, y='label', hue=hue, data=data, ax=axs[0],
                errorbar=None, order=order, hue_order=hue_order)
    axs[0].set_title('Data Model v1')
    axs[0].set_ylim(0, 1)
    axs[0].set_ylabel("Execution Accuracy")
    axs[0].yaxis.set_major_formatter(formatter)
    
    axs[0].get_legend().remove()

    
    if system:
        data = df[(df["db_id"]=="exp_v2") & (df["system"]==system)]
    else:
        data = df[(df["db_id"]=="exp_v2")]
    sns.barplot(x=x, y='label', hue=hue, data=data, ax=axs[1],
                errorbar=None, order=order,hue_order=hue_order)

    axs[1].set_title('Data Model v2')
    axs[1].set_ylabel("")
    axs[1].yaxis.set_major_formatter(formatter)
    axs[1].get_legend().remove()
    axs[1].set_ylim(0, 1)
    
    if system:
        data = df[(df["db_id"]=="exp_v3") & (df["system"]==system)]
    else:
        data = df[(df["db_id"]=="exp_v3")]
    sns.barplot(x=x, y='label', hue=hue, data=data, ax=axs[2],
                errorbar=None, order=order, hue_order=hue_order)
    axs[2].set_title('Data Model v3')
    # sns.move_legend(axs[2], "upper left", bbox_to_anchor=(1, 1))
    axs[2].set_ylabel("")
    axs[2].yaxis.set_major_formatter(formatter)
    axs[2].get_legend().remove()
    axs[2].set_ylim(0, 1)
    
    # Get the handles and labels. For this example, we'll use the ones from the last subplot, axs[2]
    handles, labels = axs[2].get_legend_handles_labels()
    
    # When creating the legend, you can specify the number of columns
    f.legend(handles, labels, loc='lower center', ncol=ncol, bbox_to_anchor=(0.5, -0.1))
    
    # sns.scatterplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species", ax=axs[0])
    # sns.histplot(data=penguins, x="species", hue="species", shrink=.8, alpha=.8, legend=False, ax=axs[1])
    f.suptitle(system, fontsize=14)
    f.tight_layout()
    f.savefig(system+"-"+x+".pdf", bbox_inches='tight')

def plot_bars_counts(df, x="hardness", hue="split", system = "T5", order=None, hue_order=None, rotation=0):

    counts_0 = df[df["db_id"]=="exp_v1"][x].value_counts()
    
    erroneous_counts_gpt_0 = df[(df["system"]==r"GPT-3.5$_{Keys}$") & (df["db_id"]=="exp_v1")][x].value_counts()*1*(2/3)
    erroneous_counts_llama_0 = df[(df["system"]=="Llama2-70b$_{Keys}$") & (df["db_id"]=="exp_v1")][x].value_counts()*1*(2/3)
    counts_0 = (counts_0-(erroneous_counts_gpt_0+erroneous_counts_llama_0))/len(df[hue].unique())

    set_style(font_scale=1.2)
    f, axs = plt.subplots(1, 3, figsize=(12, 4), sharey=True)
    if system:
        data = df[(df["db_id"]=="exp_v1") & (df["system"]==system)]
    else:
        data = df[(df["db_id"]=="exp_v1")]

    ncol = len(df[hue].unique())
    if not hue_order:
        hue_order = sorted(df[hue].unique())
    
    sns.barplot(x=x, y='label', hue=hue, data=data, ax=axs[0],
                errorbar=None, order=order, hue_order=hue_order, edgecolor="black")
    axs[0].set_title('Data Model v1')
    axs[0].set_ylim(0, 1)
    axs[0].set_ylabel("Execution Accuracy")
    axs[0].yaxis.set_major_formatter(formatter)
    
    axs[0].get_legend().remove()
    axs[0].tick_params(axis='x', rotation=rotation)

    max_height_0 = max([p.get_height() for p in axs[0].patches])

    
    if system:
        data = df[(df["db_id"]=="exp_v2") & (df["system"]==system)]
    else:
        data = df[(df["db_id"]=="exp_v2")]
    sns.barplot(x=x, y='label', hue=hue, data=data, ax=axs[1],
                errorbar=None, order=order,hue_order=hue_order, edgecolor="black")

    axs[1].set_title('Data Model v2')
    axs[1].set_ylabel("")
    axs[1].yaxis.set_major_formatter(formatter)
    axs[1].get_legend().remove()
    axs[1].set_ylim(0, 1)
    axs[1].tick_params(axis='x', rotation=rotation)

    max_height_1 = max([p.get_height() for p in axs[1].patches])
    counts_1 = df[df["db_id"]=="exp_v2"][x].value_counts()
    
    erroneous_counts_gpt_1 = df[(df["system"]==r"GPT-3.5$_{Keys}$") & (df["db_id"]=="exp_v2")][x].value_counts()*1*(2/3)
    erroneous_counts_llama_1 = df[(df["system"]=="Llama2-70b$_{Keys}$") & (df["db_id"]=="exp_v2")][x].value_counts()*1*(2/3)
    counts_1 = (counts_1-(erroneous_counts_gpt_1+erroneous_counts_llama_1))/len(df[hue].unique())


    # erroneous_counts_1 = df[(df["system"]==r"GPT-3.5$_{s}$") & (df["db_id"]=="exp_v2")][x].value_counts()*2*(2/3)
    # counts_1 = (counts_1-erroneous_counts_1)/len(df[hue].unique())
    
    if system:
        data = df[(df["db_id"]=="exp_v3") & (df["system"]==system)]
    else:
        data = df[(df["db_id"]=="exp_v3")]
    sns.barplot(x=x, y='label', hue=hue, data=data, ax=axs[2],
                errorbar=None, order=order, hue_order=hue_order, edgecolor="black")

    max_height_2 = max([p.get_height() for p in axs[2].patches])
    counts_2 = df[df["db_id"]=="exp_v3"][x].value_counts()

    erroneous_counts_gpt_2 = df[(df["system"]==r"GPT-3.5$_{Keys}$") & (df["db_id"]=="exp_v3")][x].value_counts()*1*(2/3)
    erroneous_counts_llama_2 = df[(df["system"]=="Llama2-70b$_{Keys}$") & (df["db_id"]=="exp_v3")][x].value_counts()*1*(2/3)
    counts_2 = (counts_2-(erroneous_counts_gpt_2+erroneous_counts_llama_2))/len(df[hue].unique())

    
    # erroneous_counts_2 = df[(df["system"]==r"GPT-3.5$_{s}$") & (df["db_id"]=="exp_v3")][x].value_counts()*2*(2/3)
    # counts_2 = (counts_2-erroneous_counts_2)/len(df[hue].unique())
    
    axs[2].set_title('Data Model v3')
    # sns.move_legend(axs[2], "upper left", bbox_to_anchor=(1, 1))
    axs[2].set_ylabel("")
    axs[2].yaxis.set_major_formatter(formatter)
    axs[2].get_legend().remove()
    axs[2].set_ylim(0, 1)

    axs[2].tick_params(axis='x', rotation=rotation)



    for i, label in enumerate(axs[2].get_xticklabels()):
        # Calculate the position for the annotation (middle of the group of bars)
        x_pos = i

        # count_0 = counts_0[label.get_text()]
        try:
            count_0 = counts_0[label.get_text()]
        except:
            count_0 = 0
            
        y_max = axs[0].get_ylim()[1]  # Get the maximum y-value of the plot
        # Annotate the bar
        axs[0].annotate('{:d}'.format(int(round(count_0))),
                        (x_pos, y_max - y_max*0.20), 
                        ha = 'center', va = 'center', 
                        xytext = (0, 10), 
                        textcoords = 'offset points', fontsize=10)

        try:
            count_1 = counts_1[label.get_text()]
        except:
            count_1 = 0
        axs[1].annotate('{:d}'.format(int(round(count_1))),
                        (x_pos, y_max - y_max*0.20), 
                        ha = 'center', va = 'center', 
                        xytext = (0, 10), 
                        textcoords = 'offset points', fontsize=10)
        try:
            count_2 = counts_2[label.get_text()]
        except:
            count_2 = 0
        
        axs[2].annotate('{:d}'.format(int(round(count_2))),
                        (x_pos, y_max - y_max*0.20), 
                        ha = 'center', va = 'center', 
                        xytext = (0, 10), 
                        textcoords = 'offset points', fontsize=10)    

    
    # Get the handles and labels. For this example, we'll use the ones from the last subplot, axs[2]
    handles, labels = axs[2].get_legend_handles_labels()

    # When creating the legend, you can specify the number of columns
    f.legend(handles, labels, loc='lower center', ncol=ncol, bbox_to_anchor=(0.5, -0.1))
    # , frameon=True).get_frame().set_edgecolor('black')
    
    # sns.scatterplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species", ax=axs[0])
    # sns.histplot(data=penguins, x="species", hue="species", shrink=.8, alpha=.8, legend=False, ax=axs[1])
    f.suptitle(system, fontsize=14)
    f.tight_layout()
    f.savefig(system+"-"+x+".pdf", bbox_inches='tight') 



def plot_single_bar(df, x="hardness", hue="split", system = "T5", order=None, filename=""):
    # sns.set_style("whitegrid")
    set_style()
    f, ax = plt.subplots(1, 1, figsize=(12, 4), sharey=True)
    if system:
        data = df[(df["system"]==system)]
    else:
        data = df

    ncol = len(df[hue].unique())
    if not order:
        order = sorted(df[x].unique())
    hue_order = sorted(df[hue].unique())
    sns.barplot(x=x, y='label', hue=hue, data=data, ax=ax,
                errorbar=None, order=order, hue_order=hue_order)
    # axs[0].set_title('Data Model v1')
    ax.set_ylim(0, 1)
    ax.set_ylabel("Execution Accuracy")
    ax.yaxis.set_major_formatter(formatter)
    
    ax.get_legend().remove()

    
    
    # Get the handles and labels. For this example, we'll use the ones from the last subplot, axs[2]
    handles, labels = ax.get_legend_handles_labels()
    
    # When creating the legend, you can specify the number of columns
    f.legend(handles, labels, loc='lower center', ncol=ncol, bbox_to_anchor=(0.5, -0.1))
    
    # sns.scatterplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species", ax=axs[0])
    # sns.histplot(data=penguins, x="species", hue="species", shrink=.8, alpha=.8, legend=False, ax=axs[1])
    f.suptitle(system, fontsize=14)
    f.tight_layout()
    if not filename:
        filename = system+"-"+x+".pdf"
    else:
        filename = filename+".pdf"
    f.savefig(filename, bbox_inches='tight')


def plot_bars_vertical(df, x="hardness", hue="split", system = "T5", order=None, hue_order=None,
                       filename="", figsize=(14,12), font_scale=1.4, rotation=0):
    # sns.set_style("whitegrid")

    counts_0 = df[df["db_id"]=="exp_v1"][x].value_counts()
    # erroneous_counts_gpt_0 = df[(df["system"]==r"GPT-3.5$_{s+c}$") & (df["db_id"]=="exp_v1")][x].value_counts()*2*(2/3)                           
    erroneous_counts_gpt_0 = df[(df["system"]==r"GPT-3.5$_{Keys}$") & (df["db_id"]=="exp_v1")][x].value_counts()*1*(2/3)
    erroneous_counts_llama_0 = df[(df["system"]=="Llama2-70b$_{Keys}$") & (df["db_id"]=="exp_v1")][x].value_counts()*1*(2/3)

    counts_0 = (counts_0-(erroneous_counts_gpt_0+erroneous_counts_llama_0))/len(df[hue].unique())
                           
    set_style(font_scale=font_scale)
    f, axs = plt.subplots(3, 1, figsize=figsize, sharex=True)
    if system:
        data = df[(df["db_id"]=="exp_v1") & (df["system"]==system)]
    else:
        data = df[(df["db_id"]=="exp_v1")]

    ncol = len(df[hue].unique())
    if not hue_order:                  
        hue_order = sorted(df[hue].unique())
    sns.barplot(x=x, y='label', hue=hue, data=data, ax=axs[0],
                errorbar=None, order=order, hue_order=hue_order, edgecolor="black")
                           
    max_height_0 = max([p.get_height() for p in axs[0].patches])
                           
    axs[0].set_title('Data Model v1')
    axs[0].set_ylim(0, 1)
    axs[0].set_ylabel("Execution Accuracy")
    axs[0].set_xlabel("")
    axs[0].yaxis.set_major_formatter(formatter)
    
    axs[0].get_legend().remove()

    
    if system:
        data = df[(df["db_id"]=="exp_v2") & (df["system"]==system)]
    else:
        data = df[(df["db_id"]=="exp_v2")]
    sns.barplot(x=x, y='label', hue=hue, data=data, ax=axs[1],
                errorbar=None, order=order,hue_order=hue_order, edgecolor="black")

    max_height_1 = max([p.get_height() for p in axs[1].patches])
    counts_1 = df[df["db_id"]=="exp_v2"][x].value_counts()
                           
    erroneous_counts_gpt_1 = df[(df["system"]==r"GPT-3.5$_{Keys}$") & (df["db_id"]=="exp_v2")][x].value_counts()*1*(2/3)
    erroneous_counts_llama_1 = df[(df["system"]=="Llama2-70b$_{Keys}$") & (df["db_id"]=="exp_v2")][x].value_counts()*1*(2/3)
    counts_1 = (counts_1-(erroneous_counts_gpt_1+erroneous_counts_llama_1))/len(df[hue].unique())

    axs[1].set_title('Data Model v2')
    axs[1].set_ylabel("Execution Accuracy")
    axs[1].set_xlabel("")
    axs[1].yaxis.set_major_formatter(formatter)
    axs[1].get_legend().remove()
    axs[1].set_ylim(0, 1)
    
    if system:
        data = df[(df["db_id"]=="exp_v3") & (df["system"]==system)]
    else:
        data = df[(df["db_id"]=="exp_v3")]
    sns.barplot(x=x, y='label', hue=hue, data=data, ax=axs[2],
                errorbar=None, order=order, hue_order=hue_order, edgecolor="black")

    max_height_2 = max([p.get_height() for p in axs[2].patches])
    counts_2 = df[df["db_id"]=="exp_v3"][x].value_counts()

                           
    erroneous_counts_gpt_2 = df[(df["system"]==r"GPT-3.5$_{Keys}$") & (df["db_id"]=="exp_v3")][x].value_counts()*1*(2/3)
    erroneous_counts_llama_2 = df[(df["system"]=="Llama2-70b$_{Keys}$") & (df["db_id"]=="exp_v3")][x].value_counts()*1*(2/3)
    counts_2 = (counts_2-(erroneous_counts_gpt_2+erroneous_counts_llama_2))/len(df[hue].unique())
                           
    axs[2].set_title('Data Model v3')
    # sns.move_legend(axs[2], "upper left", bbox_to_anchor=(1, 1))
    axs[2].set_ylabel("Execution Accuracy")
    axs[2].yaxis.set_major_formatter(formatter)
    axs[2].get_legend().remove()
    axs[2].set_ylim(0, 1)

    axs[2].tick_params(axis='x', rotation=rotation)
                           

    for i, label in enumerate(axs[2].get_xticklabels()):
        # Calculate the position for the annotation (middle of the group of bars)
        x_pos = i

        # count_0 = counts_0[label.get_text()]
        try:
            count_0 = counts_0[label.get_text()]
        except:
            count_0 = 0
        y_max_0 = axs[0].get_ylim()[1]

        # Annotate the bar
        axs[0].annotate('{:d}'.format(int(round(count_0))),
                        (x_pos, y_max_0 - y_max_0*0.20), 
                        ha = 'center', va = 'center', 
                        xytext = (0, 10), 
                        textcoords = 'offset points', fontsize=12)

        try:
            count_1 = counts_1[label.get_text()]
        except:
            count_1 = 0
            
        y_max_1 = axs[1].get_ylim()[1]

        axs[1].annotate('{:d}'.format(int(round(count_1))),
                        (x_pos, y_max_1 - y_max_1*0.20), 
                        ha = 'center', va = 'center', 
                        xytext = (0, 10), 
                        textcoords = 'offset points', fontsize=12)
        try:
            count_2 = counts_2[label.get_text()]
        except:
            count_2 = 0
        y_max_2 = axs[1].get_ylim()[1]

        axs[2].annotate('{:d}'.format(int(round(count_2))),
                        (x_pos, y_max_2 - y_max_2*0.20), 
                        ha = 'center', va = 'center', 
                        xytext = (0, 10), 
                        textcoords = 'offset points', fontsize=12)    
    #Get the handles and labels. For this example, we'll use the ones from the last subplot, axs[2]
    handles, labels = axs[2].get_legend_handles_labels()
    
    # When creating the legend, you can specify the number of columns
    f.legend(handles, labels, loc='lower center', ncol=ncol, bbox_to_anchor=(0.5, -0.03))
    
    # sns.scatterplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species", ax=axs[0])
    # sns.histplot(data=penguins, x="species", hue="species", shrink=.8, alpha=.8, legend=False, ax=axs[1])
    f.suptitle(system, fontsize=14)
    f.tight_layout()
    f.savefig(system+"-"+x+".pdf", bbox_inches='tight')