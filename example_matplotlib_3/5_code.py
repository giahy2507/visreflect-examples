import matplotlib.pyplot as plt

if __name__ == "__main__":
    fig, axs = plt.subplots(2, 1, figsize=(6, 6))
    
    # Data #1
    datasets_1 = ['Matplotlib-py', 'Graphics', 'ChartJS', 'Vega-Lite', "nvBench"]
    plot_distribution_1 = {
        "Line Chart": [61.85, 34.43, 48.12, 23.00, 6.24],
        "Scatter": [27.70, 52.54, 3.75, 37.31, 5.43],
        "Bar Chart": [9.92, 12.39, 27.90, 37.91, 81.16],
        "Pie Chart": [0.53, 0.65, 20.22, 1.79, 7.17]
    }

    # Data #2
    datasets_2 = ["Matplotlib-nb", 'Matplotlib-py', 'PlotCoder', 'ChartDialog']
    plot_distribution_2 = {
        "Line Chart": [53.48, 56.98, 47.13, 24.38],
        "Scatter":    [27.28, 25.52, 28.39, 2.57],
        "Bar Chart":  [11.00, 9.14, 17.30, 22.47],
        "Pie Chart":  [0.72, 0.49, 0.99, 14.35],
        "Contour":    [1.58, 1.93, 1.10, 17.54],
        "Streamplot": [0.03, 0.07, 0.03, 16.66],
        "Heatmap":    [5.93, 5.99, 5.05, 2.02],
    }
    

    # Plot Data #1 in the first subplot
    x = [i*0.5 for i in range(len(datasets_1))]
    width = 0.1
    axs[0].bar(x, plot_distribution_1["Line Chart"], width, label="Line Chart")
    axs[0].bar([i + width for i in x], plot_distribution_1["Scatter"], width, label="Scatter")
    axs[0].bar([i + 2 * width for i in x], plot_distribution_1["Bar Chart"], width, label="Bar Chart")
    axs[0].bar([i + 3 * width for i in x], plot_distribution_1["Pie Chart"], width, label="Pie Chart")

    # Add labels, title, and legend in the first subplot
    axs[0].set_xticks([i + 1.5 * width for i in x])
    axs[0].set_xticklabels(datasets_1, fontsize=12, rotation=10)
    axs[0].set_yticklabels(list(range(0, 90, 10)), fontsize=12)
    axs[0].legend(fontsize=11)
    axs[0].set_ylabel('Percentage', fontsize=11)

    # set red tick labels
    for label in axs[0].get_xticklabels():
        if label.get_text() == "nvBench":
            label.set_color('red')


    # ------------------------------------------------------------

    # Plot Data #2 in the second subplot
    x = [i*1 for i in range(len(datasets_2))]
    width = 0.1
    axs[1].bar(x, plot_distribution_2["Line Chart"], width, label="Line Chart")
    axs[1].bar([i + width for i in x], plot_distribution_2["Scatter"], width, label="Scatter")
    axs[1].bar([i + 2 * width for i in x], plot_distribution_2["Bar Chart"], width, label="Bar Chart")
    axs[1].bar([i + 3 * width for i in x], plot_distribution_2["Pie Chart"], width, label="Pie Chart")
    axs[1].bar([i + 4 * width for i in x], plot_distribution_2["Contour"], width, label="Contour")
    axs[1].bar([i + 5 * width for i in x], plot_distribution_2["Streamplot"], width, label="Streamplot")
    axs[1].bar([i + 6 * width for i in x], plot_distribution_2["Heatmap"], width, label="Heatmap")

    # Add labels, title, and legend in the first subplot
    axs[1].set_ylabel('Percentage', labelpad=0, fontsize=11)
    axs[1].set_xticks([i + 1.5 * width for i in x])
    axs[1].set_xticklabels(datasets_2, fontsize=12)
    axs[1].set_yticklabels(list(range(0, 90, 10)), fontsize=12)
    axs[1].legend(fontsize=11, framealpha=0.5, loc="upper right")
    
    # set red tick labels
    for label in axs[1].get_xticklabels():
        if label.get_text() == "PlotCoder" or label.get_text() == "ChartDialog":
            label.set_color('red')
    
    # ------------------------------------------------------------
    # remove padding or margin of output image
    fig.tight_layout()

    fig.savefig('2_visualisation_image.png', dpi=500, format="png")

    

    


