import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

dice_result=[]
for i in range(1, 1001):
    dice_1= random.randint(1,6)
    dice_2= random.randint(1,6)
    dice_result.append(dice_1+dice_2)

mean= statistics.mean(dice_result)
median=statistics.median(dice_result)
mode=statistics.mode(dice_result)

print("Mean of the data is {}".format(mean))
print("Median of the data is {}".format(median))
print("Mode of the data is {}".format(mode))

std_dev=statistics.stdev(dice_result)
print("Standard Deviation of the data is {}".format(std_dev))

first_std_dev_start, first_std_dev_end= mean-std_dev, mean+std_dev
second_std_dev_start, second_std_dev_end= mean-(2*std_dev), mean+(2*std_dev)
third_std_dev_start, third_std_dev_end= mean-(3*std_dev), mean+(3*std_dev)

list_of_data_within_1_std_dev= [result for result in dice_result if result>first_std_dev_start and result<first_std_dev_end]
list_of_data_within_2_std_dev= [result for result in dice_result if result>second_std_dev_start and result<second_std_dev_end]
list_of_data_within_3_std_dev= [result for result in dice_result if result>third_std_dev_start and result<third_std_dev_end]

print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_dev)*100.0/len(dice_result)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_dev)*100.0/len(dice_result)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_dev)*100.0/len(dice_result)))

fig=ff.create_distplot([dice_result], ["Result"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[first_std_dev_start, first_std_dev_start], y=[0, 0.17], mode="lines", name="First Deviation Start"))
fig.add_trace(go.Scatter(x=[first_std_dev_end, first_std_dev_end], y=[0, 0.17], mode="lines", name="First Deviation End"))
fig.add_trace(go.Scatter(x=[second_std_dev_start, second_std_dev_start], y=[0, 0.17], mode="lines", name="Second Deviation Start"))
fig.add_trace(go.Scatter(x=[second_std_dev_end, second_std_dev_end], y=[0, 0.17], mode="lines", name="Second Deviation End"))
fig.add_trace(go.Scatter(x=[third_std_dev_start, third_std_dev_start], y=[0, 0.17], mode="lines", name="First Deviation Start"))
fig.add_trace(go.Scatter(x=[third_std_dev_end, third_std_dev_end], y=[0, 0.17], mode="lines", name="Third Deviation End"))
fig.show()