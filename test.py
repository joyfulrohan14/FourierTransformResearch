import numpy as np
import pandas as pd
from bokeh.plotting import figure, show, output_file, curdoc
from bokeh.layouts import layout, row, column, Spacer, widgetbox
from bokeh.models import ColumnDataSource, DateRangeSlider, BoxAnnotation, HoverTool
from bokeh.models.widgets import RangeSlider, Button, CheckboxButtonGroup, Div


# synthetic data

data = pd.DataFrame({
    'date':pd.date_range(start='1/1/2000', periods=1000),
    'x':np.random.choice(range(100), 1000)
})

startDate = data.iloc[0]['date']
endDate = data.iloc[-1]['date']
source = ColumnDataSource(data)


# title
title1 = Div(text='Some series')
title2 = Div(text='Some series')
title3 = Div(text='Some series')
title4 = Div(text='Some series')
title5 = Div(text='Some series')
title6 = Div(text='Some series')

# main figure
p1 = figure( x_axis_type='datetime', x_range=(startDate,endDate))
p1.line(x=data['date'], y=data['x'], line_width=2, color='navy')
p1.toolbar.logo = None

p2 = figure( x_axis_type='datetime', x_range=(startDate,endDate))
p2.line(x=data['date'], y=data['x'], line_width=2, color='navy')
p2.toolbar.logo = None

p3 = figure( x_axis_type='datetime', x_range=(startDate,endDate))
p3.line(x=data['date'], y=data['x'], line_width=2, color='navy')
p3.toolbar.logo = None

p4 = figure( x_axis_type='datetime', x_range=(startDate,endDate))
p4.line(x=data['date'], y=data['x'], line_width=2, color='navy')
p4.toolbar.logo = None

p5 = figure( x_axis_type='datetime', x_range=(startDate,endDate))
p5.line(x=data['date'], y=data['x'], line_width=2, color='navy')
p5.toolbar.logo = None

p6 = figure( x_axis_type='datetime', x_range=(startDate,endDate))
p6.line(x=data['date'], y=data['x'], line_width=2, color='navy')
p6.toolbar.logo = None


# some 'tier-1' widgets
someButton1 = Button(label='>>', button_type='success')
someSelector1 = CheckboxButtonGroup(labels=['Series A', 'Series B'], active=[0, 1])
someButton2 = Button(label='>>', button_type='success')
someSelector2 = CheckboxButtonGroup(labels=['Series A', 'Series B'], active=[0, 1])
someButton3 = Button(label='>>', button_type='success')
someSelector3 = CheckboxButtonGroup(labels=['Series A', 'Series B'], active=[0, 1])
someButton4 = Button(label='>>', button_type='success')
someSelector4 = CheckboxButtonGroup(labels=['Series A', 'Series B'], active=[0, 1])
someButton5 = Button(label='>>', button_type='success')
someSelector5 = CheckboxButtonGroup(labels=['Series A', 'Series B'], active=[0, 1])
someButton6 = Button(label='>>', button_type='success')
someSelector6 = CheckboxButtonGroup(labels=['Series A', 'Series B'], active=[0, 1])

# range slider widget
def updateRange(attr, old, new):
    p1.x_range.start = new[0]
    p1.x_range.end = new[1]
    p2.x_range.start = new[0]
    p2.x_range.end = new[1]
    p3.x_range.start = new[0]
    p3.x_range.end = new[1]
    p4.x_range.start = new[0]
    p4.x_range.end = new[1]
    p5.x_range.start = new[0]
    p5.x_range.end = new[1]
    p6.x_range.start = new[0]
    p6.x_range.end = new[1]

rSlider1 = DateRangeSlider(start=startDate, end=endDate, value=(startDate,endDate), show_value=False, width=600)
rSlider1.on_change('value', updateRange)
rSlider2 = DateRangeSlider(start=startDate, end=endDate, value=(startDate,endDate), show_value=False, width=600)
rSlider2.on_change('value', updateRange)
rSlider3 = DateRangeSlider(start=startDate, end=endDate, value=(startDate,endDate), show_value=False, width=600)
rSlider3.on_change('value', updateRange)
rSlider4 = DateRangeSlider(start=startDate, end=endDate, value=(startDate,endDate), show_value=False, width=600)
rSlider4.on_change('value', updateRange)
rSlider5 = DateRangeSlider(start=startDate, end=endDate, value=(startDate,endDate), show_value=False, width=600)
rSlider5.on_change('value', updateRange)
rSlider6 = DateRangeSlider(start=startDate, end=endDate, value=(startDate,endDate), show_value=False, width=600)
rSlider6.on_change('value', updateRange)

curdoc().add_root(
    layout(
        [[column(title1, row(someSelector1, someButton1), p1, rSlider1), column(title2, row(someSelector2, someButton2), p2, rSlider2), column(title3, row(someSelector3, someButton3), p3, rSlider3)],
        [column(title4, row(someSelector4, someButton4), p4, rSlider4), column(title5, row(someSelector5, someButton5), p5, rSlider5), column(title6, row(someSelector6, someButton6), p6, rSlider6)]]
    )
)