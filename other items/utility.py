import matplotlib.pyplot as plt
import scipy.stats as st

class PlotTools:

    def check_columns(df, head_rows=5):
        """
        :param df: pandas dataframe
        :param head_rows: integer, the number of row to display
        :return: None
        """

        for column in df.columns:
            srs = df[column].value_counts()
            print("=" * 60)
            print(f"Column: {column}")
            print("-" * 20)
            print(f"--- Total Unique Values: {len(srs)} ---")
            print(srs.head(head_rows).to_string())
            print(f"Min: {srs.index.min()},  Max: {srs.index.max()}")
            # print(f"Data type: {srs.dtype}")


    def linear_regression(df, x, y, **kwargs):
        """
        df: dataframe
        x: string, column name
        y: string, column name
        """
        import matplotlib.pyplot as plt
        import scipy.stats as st

        plt.figure(figsize=kwargs["figsize"]) if "figsize" in kwargs else plt.figure()

        x = df[x]
        y = df[y]
        plt.scatter(x, y)
        (slope, intercept, rvalue, pvalue, stderr) = st.linregress(x, y)
        regress_values = x * slope + intercept
        line_eq = f"y = {round(slope, 2)}x + {round(intercept, 2)}"
        plt.plot(x, regress_values, "r-")

        xy = kwargs["xy"] if "xy" in kwargs else (df[x].max() * 0.75, df[y].max() * 0.9)
        fontsize = kwargs["fontsize"] if "fontsize" in kwargs else 12
        color = kwargs["color"] if "color" in kwargs else "red"
        plt.annotate(line_eq, xy, fontsize=fontsize, color=color)
        plt.annotate(f"rvalue: {round(rvalue, 2)}", xy, fontsize=fontsize, color=color)
