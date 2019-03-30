from bokeh.charts import Bar, output_file, show #use output_notebook to visualize it in notebook
# prepare data (dummy data)
data = {"y": [1, 2, 3, 4, 5]}
# Output to Line.HTML
output_file("lines.html", title="line plot example") #put output_notebook() for notebook
# create a new line chat with a title and axis labels
p = Bar(data, title="Line Chart Example", xlabel='x', ylabel='values', width=400, height=400)
# show the results
show(p)