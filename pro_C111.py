import pandas as pd
import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv('studentMarks.csv')
data = df['Math_score'].tolist()


mean = statistics.mean(data)
stdev = statistics.stdev(data)
print("Mean:",mean)
print("Standard Deviation:",stdev)

def randomsetofmeans(counter):
    dataset = []
    for i in range(0,counter):
        randomindex = random.randint(0,len(data)-1)
        value = data[randomindex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

meanlist = []
for i in range(0,1000):
    setofmeans = randomsetofmeans(100)
    meanlist.append(setofmeans)

sample_stdev = statistics.stdev(meanlist)
sample_mean = statistics.mean(meanlist)
print('Sample Mean:',sample_mean)
print('Sample Stdev:',sample_stdev)




stdev_1_start, stdev_1_end = sample_mean-sample_stdev, sample_mean+sample_stdev
stdev_2_start, stdev_2_end = sample_mean-2*sample_stdev, sample_mean+2*sample_stdev
stdev_3_start, stdev_3_end = sample_mean-3*sample_stdev, sample_mean+3*sample_stdev


df_1 = pd.read_csv('School_1_Sample.csv')
data1 = df_1['Math_score'].tolist()
meanofsample1 = statistics.mean(data1)
print('Mean of Sample 1:',meanofsample1)

df_2 = pd.read_csv('School_2_Sample.csv')
data2 = df_2['Math_score'].tolist()
meanofsample2 = statistics.mean(data2)
print('Mean of Sample 2:',meanofsample2)

df_3 = pd.read_csv('School_3_Sample.csv')
data3 = df_3['Math_score'].tolist()
meanofsample3 = statistics.mean(data3)
print('Mean of Sample 3:',meanofsample3)


z_score1 = (meanofsample1-sample_mean)/sample_stdev
z_score2 = (meanofsample2-sample_mean)/sample_stdev
z_score3 = (meanofsample3-sample_mean)/sample_stdev

print("Z score 1:",z_score1)
print("Z score 2:",z_score2)
print("Z score 3:",z_score3)


fig = ff.create_distplot([meanlist],["Maths Scores"],show_hist = False)
fig.add_trace(go.Scatter(x = [sample_mean,sample_mean],y = [0,0.2],mode = "lines", name = "Sample Mean"))
fig.add_trace(go.Scatter(x = [stdev_1_start,stdev_1_start], y = [0,0.2], mode = "lines", name = "Stand. Dev 1 Start"))
fig.add_trace(go.Scatter(x = [stdev_1_end,stdev_1_end], y = [0,0.2], mode = "lines", name = "Stand. Dev 1 End"))
fig.add_trace(go.Scatter(x = [stdev_2_start,stdev_2_start], y = [0,0.2], mode = "lines", name = "Stand. Dev 2 Start"))
fig.add_trace(go.Scatter(x = [stdev_2_end,stdev_2_end], y = [0,0.2], mode = "lines", name = "Stand. Dev 2 End"))
fig.add_trace(go.Scatter(x = [stdev_3_start,stdev_3_start], y = [0,0.2], mode = "lines", name = "Stand. Dev 3 Start"))
fig.add_trace(go.Scatter(x = [stdev_3_end,stdev_3_end], y = [0,0.2], mode = "lines", name = "Stand. Dev 3 End"))
fig.add_trace(go.Scatter(x = [meanofsample1,meanofsample1], y = [0,0.2], mode = "lines", name = "Mean of Sample 1"))
fig.add_trace(go.Scatter(x = [meanofsample2,meanofsample2], y = [0,0.2], mode = "lines", name = "Mean of Sample 2"))
fig.add_trace(go.Scatter(x = [meanofsample3,meanofsample3], y = [0,0.2], mode = "lines", name = "Mean of Sample 3"))

fig.show()