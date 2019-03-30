from bokeh.charts import Bar, output_file, show 
from bokeh.plotting import figure
plot = figure(plot_width=400, tools='pan,box_zoom')
#plot.circle([1,2,3,4,5],[8,6,5,2,3])
plot.circle(x=10,y=[1.5,2,3.5,4,5.5],size=[10,20,30,40,50])
output_file("circles.html", title="Circle plot Example") 
show(plot)