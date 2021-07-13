import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd

df=pd.read_csv("hw.csv")

height_list= df["Height(Inches)"].tolist()
weight_list= df["Weight(Pounds)"].tolist()

mean= statistics.mean(height_list)
median=statistics.median(height_list)
mode=statistics.mode(height_list)

mean2= statistics.mean(weight_list)
median2=statistics.median(weight_list)
mode2=statistics.mode(weight_list)

print("Mean of the data is {}".format(mean2))
print("Median of the data is {}".format(median2))
print("Mode of the data is {}".format(mode2))

print("Mean of the data is {}".format(mean))
print("Median of the data is {}".format(median))
print("Mode of the data is {}".format(mode))

std_dev=statistics.stdev(height_list)
print("Standard Deviation of the data is {}".format(std_dev))

first_std_dev_start, first_std_dev_end= mean-std_dev, mean+std_dev
second_std_dev_start, second_std_dev_end= mean-(2*std_dev), mean+(2*std_dev)
third_std_dev_start, third_std_dev_end= mean-(3*std_dev), mean+(3*std_dev)

list_of_data_within_1_std_dev= [result for result in height_list if result>first_std_dev_start and result<first_std_dev_end]
list_of_data_within_2_std_dev= [result for result in height_list if result>second_std_dev_start and result<second_std_dev_end]
list_of_data_within_3_std_dev= [result for result in height_list if result>third_std_dev_start and result<third_std_dev_end]

print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_dev)*100.0/len(height_list)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_dev)*100.0/len(height_list)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_dev)*100.0/len(height_list)))

std_dev=statistics.stdev(weight_list)
print("Standard Deviation of the data is {}".format(std_dev))

first_std_dev_start, first_std_dev_end= mean2-std_dev, mean2+std_dev
second_std_dev_start, second_std_dev_end= mean2-(2*std_dev), mean2+(2*std_dev)
third_std_dev_start, third_std_dev_end= mean2-(3*std_dev), mean2+(3*std_dev)

list_of_data_within_1_std_dev= [result for result in weight_list if result>first_std_dev_start and result<first_std_dev_end]
list_of_data_within_2_std_dev= [result for result in weight_list if result>second_std_dev_start and result<second_std_dev_end]
list_of_data_within_3_std_dev= [result for result in weight_list if result>third_std_dev_start and result<third_std_dev_end]

print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_dev)*100.0/len(weight_list)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_dev)*100.0/len(weight_list)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_dev)*100.0/len(weight_list)))