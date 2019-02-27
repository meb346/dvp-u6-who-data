
# coding: utf-8

# # Introduction
# 
# For this project, you will act as a data researcher for the World Health Organization. You will investigate if there is a strong correlation between the economic output of a country and the life expectancy of its citizens.  
# 
# During this project, you will analyze, prepare, and plot data, and seek to answer questions in a meaningful way.
# 
# After you perform analysis, you'll be creating an article with your visualizations to be featured in the fictional "Time Magazine".
# 
# **Focusing Questions**: 
# + Has life expectancy increased over time in the six nations?
# + Has GDP increased over time in the six nations?
# + Is there a correlation between GDP and life expectancy of a country?
# + What is the average life expactancy in these nations?
# + What is the distribution of that life expectancy?
# 
# GDP Source:[World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD)national accounts data, and OECD National Accounts data files.
# 
# Life expectancy Data Source: [World Health Organization](http://apps.who.int/gho/data/node.main.688)
# 

# ## Step 1. Import Python Modules

# Import the modules that you'll be using in this project:
# - `from matplotlib import pyplot as plt`
# - `import pandas as pd`
# - `import seaborn as sns`

# In[1]:


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# To look for connections between GDP and life expectancy you will need to load the datasets into DataFrames so that they can be visualized.
# 
# Load **all_data.csv** into a DataFrame called `df`. Then, quickly inspect the DataFrame using `.head()`.
# 
# Hint: Use `pd.read_csv()`
# 

# In[2]:


df = pd.read_csv('all_data.csv')
df.head()


# ## Step 2 Prep The Data

# ## Step 3 Examine The Data

# The datasets are large and it may be easier to view the entire dataset locally on your computer. You can open the CSV files directly from the folder you downloaded for this project.
# 
# Let's learn more about our data:
# - GDP stands for **G**ross **D**omestic **P**roduct. GDP is a monetary measure of the market value of all final goods and services produced in a time period. 
# - The GDP values are in current US dollars.

# What six countries are represented in the data?

# In[3]:


#Chile, China, Germany, Mexico, USA, Zimbabwe


# What years are represented in the data?

# In[4]:


#2000 to 2015


# ## Step 4 Tweak The DataFrame
# 
# Look at the column names of the DataFrame `df` using `.head()`. 

# In[5]:


df.head()


# What do you notice? The first two column names are one word each, and the third is five words long! `Life expectancy at birth (years)` is descriptive, which will be good for labeling the axis, but a little difficult to wrangle for coding the plot itself. 
# 
# **Revise The DataFrame Part A:** 
# 
# Use Pandas to change the name of the last column to `LEABY`.
# 
# Hint: Use `.rename()`. [You can read the documentation here.](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html)). </font>

# In[6]:


df.rename(columns={'Life expectancy at birth (years)':'LEABY'}, inplace=True)


# Run `df.head()` again to check your new column name worked.

# In[7]:


df.head()


# ---

# ## Step 5 Bar Charts To Compare Average

# To take a first high level look at both datasets, create a bar chart for each DataFrame:
# 
# A) Create a bar chart from the data in `df` using `Country` on the x-axis and `GDP` on the y-axis. 
# Remember to `plt.show()` your chart!

# In[8]:


sns.set_style('whitegrid')

f, ax = plt.subplots(figsize = (15, 10))
sns.set_palette('bright')
sns.barplot(data=df, x='Country', y='GDP')
ax.set_title('Average GDP by Country in Trillions of US Dollars')
plt.show()


# B) Create a bar chart using the data in `df` with `Country` on the x-axis and `LEABY` on the y-axis.
# Remember to `plt.show()` your chart!

# In[9]:


sns.set_style('whitegrid')
f, ax = plt.subplots(figsize = (15,10))
sns.set_palette('bright')
sns.barplot(data=df, x='Country', y='LEABY')
ax.set_title('Average Life Expectancy at Birth by Country')

plt.show()


# What do you notice about the two bar charts? Do they look similar?

# In[10]:


#No, LEABY is relatively close when comparing each country, with Zimbabwe being an outlier, 
#but for GDP the US is far above the other countries


# ## Step 6. Violin Plots To Compare Life Expectancy Distributions 

# Another way to compare two datasets is to visualize the distributions of each and to look for patterns in the shapes.
# 
# We have added the code to instantiate a figure with the correct dimmensions to observe detail. 
# 1. Create an `sns.violinplot()` for the dataframe `df` and map `Country` and `LEABY` as its respective `x` and `y` axes. 
# 2. Be sure to show your plot

# In[26]:


#set style
sns.set_style('darkgrid')

#set context and font size
sns.set_context('talk', font_scale=1)

#create figure
f, ax = plt.subplots(figsize=(15, 10)) 

#set color palette. Used the same palette above so it is easier to compare plots.
sns.set_palette('bright')

#create plot
sns.violinplot(data=df, x='Country', y='LEABY')

#set title
ax.set_title('Violin Plot of Life Expectancy by Country')

#set y label
ax.set_ylabel('Life Expectancy at Birth in Years')

#save figure
plt.savefig("violin_plot_LEABY.png")

plt.show()
#From this plot we can see that zimbabwe has the widest distribution, thus their life expectancy has changed the most


# What do you notice about this distribution? Which country's life expactancy has changed the most?

#  

# ## Step 7. Bar Plots Of GDP and Life Expectancy over time
# 
# We want to compare the GDPs of the countries over time, in order to get a sense of the relationship between GDP and life expectancy. 
# 
# First, can plot the progession of GDP's over the years by country in a barplot using Seaborn.
# We have set up a figure with the correct dimensions for your plot. Under that declaration:
# 1. Save `sns.barplot()` to a variable named `ax`
# 2. Chart `Country` on the x axis, and `GDP` on the `Y` axis on the barplot. Hint: `ax = sns.barplot(x="Country", y="GDP")`
# 3. Use the `Year` as a `hue` to differentiate the 15 years in our data. Hint: `ax = sns.barplot(x="Country", y="GDP", hue="Year", data=df)`
# 4. Since the names of the countries are long, let's rotate their label by 90 degrees so that they are legible. Use `plt.xticks("rotation=90")`
# 5. Since our GDP is in trillions of US dollars, make sure your Y label reflects that by changing it to `"GDP in Trillions of U.S. Dollars"`. Hint: `plt.ylabel("GDP in Trillions of U.S. Dollars")`
# 6. Be sure to show your plot.
# 

# In[12]:


#set style
sns.set_style('whitegrid')

#create figure
f, ax = plt.subplots(figsize=(15, 15)) 

ax = sns.barplot(data=df, x='Country', y='GDP', hue='Year')
plt.xticks(rotation=90)
plt.ylabel('GDP in Trillions of U.S. Dollars')
ax.set_title('GDP by Year for Each Country')
plt.show()


# Now that we have plotted a barplot that clusters GDP over time by Country, let's do the same for Life Expectancy.
# 
# The code will essentially be the same as above! The beauty of Seaborn relies in its flexibility and extensibility. Paste the code from above in the cell bellow, and: 
# 1. Change your `y` value to `LEABY` in order to plot life expectancy instead of GDP. Hint: `ax = sns.barplot(x="Country", y="LEABY", hue="Year", data=df)`
# 2. Tweak the name of your `ylabel` to reflect this change, by making the label `"Life expectancy at birth in years"` Hint: `ax.set(ylabel="Life expectancy at birth in years")`
# 

# In[13]:


#set style
sns.set_style('whitegrid')

f, ax = plt.subplots(figsize=(15, 15)) 
ax = sns.barplot(data=df, x='Country', y='LEABY', hue='Year')
ax.set(ylabel='Life expectancy at birth in years')
ax.set_title('Life Expectancy by Year for Each Country')

#move legend outside of plot so it doesn't cover data
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()


# What are your first impressions looking at the visualized data?
# 
# - Which countries' bars changes the most?
# - What years are there the biggest changes in the data?
# - Which country has had the least change in GDP over time? 
# - How do countries compare to one another?
# - Now that you can see the both bar charts, what do you think about the relationship between GDP and life expectancy?
# - Can you think of any reasons that the data looks like this for particular countries?

# In[14]:


#1. Zimbabwe has the biggest change in life expectancy from 2000-2015, 
#however, it is hard to see Zimbabwe's data on the GDP chart because of the scale
#It appears that China has the largest change in GDP from 2000-2015

#2. It's hard to tell based on this plot, but it appears that there is a large change in Zimbabwe's life expectancy from 2009-2011.
# China has a large change in GDP freom 2010-2012

#3. It's hard to say since we cannot see Zimbabwe on the GDP chart, but it appears that Chile has the least change in GDP.

#4.USA has by far the largest GDP, but does not have the largest life expectancy. 
#In general, life expectancy is closer between the countries, with Zimbabwe being the outlier.

#5. #Based on these charts, it seems that GDP and life expectancy are slightly related, 
#however, to learn more, it would be helpful to have the GDP averaged by population, the GDP per capita. 
# For example, although Germany looks like it has relatively small GDP on these graphs, 
#it is also a much smaller country than the US, China, and Mexico. 
#Because Germany has a relatively large amount of money/person, it has a well established healthcare system, likely contributing to high LEABY

#6. China has rapidly industrialized, thus the rapidly increasing GDP. 
#Zimbabwe has experienced major political and social upheaval, as well as an HIV/AIDs pandemic that has probably contributed to the fluxuating LEABY.







# Note: You've mapped two bar plots showcasing a variable over time by country, however, bar charts are not traditionally used for this purpose. In fact, a great way to visualize a variable over time is by using a line plot. While the bar charts tell us some information, the data would be better illustrated on a line plot.  We will complete this in steps 9 and 10, for now let's switch gears and create another type of chart.

# ## Step 8. Scatter Plots of GDP and Life Expectancy Data

# To create a visualization that will make it easier to see the possible correlation between GDP and life expectancy, you can plot each set of data on its own subplot, on a shared figure.
# 
# To create multiple plots for comparison, Seaborn has a special (function)[https://seaborn.pydata.org/generated/seaborn.FacetGrid.html] called `FacetGrid`. A FacetGrid takes in a function and creates an individual graph for which you specify the arguments!
#     
# Since this may be the first time you've learned about FacetGrid, we have prepped a fill in the blank code snippet below. 
# Here are the instructors to fill in the blanks from the commented word bank:
# 
# 1. In this graph, we want GDP on the X axis and Life Expectancy on the Y axis.
# 2. We want the columns to be split up for every Year in the data
# 3. We want the data points to be differentiated (hue) by Country.
# 4. We want to use a Matplotlib scatter plot to visualize the different graphs
# 
# 
# Be sure to show your plot!
# 

# In[23]:


#set style and color
sns.set_style('whitegrid')
sns.set_palette('bright')
sns.set_context('notebook')

#create figure and plot
g = sns.FacetGrid(df, col='Year', hue='Country', col_wrap=4, height=2)
g = (g.map(plt.scatter, 'GDP', 'LEABY', edgecolor="w").add_legend())

#save fig
plt.savefig("scatter_GDP_LEABY.png")

plt.show()


# + Which country moves the most along the X axis over the years?
# + Which country moves the most along the Y axis over the years?
# + Is this surprising?
# + Do you think these scatter plots are easy to read? Maybe there's a way to plot that! 

# In[16]:


#China moves the most along the X axis, this means that China's GDP grew the most
#Zimbabwe moves the most along the Y axis over the years, meaning that Zimnanwe's Life Expectancy has changed the most
#These results make sense, as China has experienced massive growth over this time period. 
#Zimbabwe had an economic collapse over this time period, but also started receiving more foreign aid to help the AIDs crisis, 
#which may have increased the life expectancy


# ## Step 9. Line Plots for Life Expectancy

# In the scatter plot grid above, it was hard to isolate the change for GDP and Life expectancy over time. 
# It would be better illustrated with a line graph for each GDP and Life Expectancy by country. 
# 
# FacetGrid also allows you to do that! Instead of passing in `plt.scatter` as your Matplotlib function, you would have to pass in `plt.plot` to see a line graph. A few other things have to change as well. So we have created a different codesnippets with fill in the blanks.  that makes use of a line chart, and we will make two seperate FacetGrids for both GDP and Life Expectancy separately.
# 
# Here are the instructors to fill in the blanks from the commented word bank:
# 
# 1. In this graph, we want Years on the X axis and Life Expectancy on the Y axis.
# 2. We want the columns to be split up by Country
# 3. We want to use a Matplotlib line plot to visualize the different graphs
# 
# 
# Be sure to show your plot!
# 
# 

# In[17]:



#set style
sns.set_style('ticks')

g3 = sns.FacetGrid(df, col="Country", col_wrap=3, height=4)

g3 = (g3.map(plt.plot, "Year", "LEABY").add_legend())

plt.savefig("facet_LEABY.png")
plt.show()

#Zimbabwe changes the most.
#2007-2010 appears to be a big change but it is hard to say based on these plots alone
#Appears that the USA had the least change over this period
#The LEABY for the US has remained relatively steady over the last few decades because we have not had major increases in infrastructure
#The LEABY For Zimbabwe has fluctuated due to governmental termoil, famine, an AIDs crisis and aid from NGOs


# What are your first impressions looking at the visualized data?
# 
# - Which countries' line changes the most?
# - What years are there the biggest changes in the data?
# - Which country has had the least change in life expectancy over time? 
# - Can you think of any reasons that the data looks like this for particular countries?

#  

# ## Step 10. Line Plots for GDP

# Let's recreate the same FacetGrid for GDP now. Instead of Life Expectancy on the Y axis, we now we want GDP.
# 
# Once you complete and successfully run the code above, copy and paste it into the cell below. Change the variable for the X axis. Change the color on your own! Be sure to show your plot.
# 

# In[18]:


sns.set_style('ticks')

g3 = sns.FacetGrid(df, col="Country", col_wrap=3, height=4)
g3 = (g3.map(plt.plot, "Year", "GDP", color="red").add_legend())

plt.savefig("facet_GDP.png")
plt.show()


# Which countries have the highest and lowest GDP?

# In[19]:


#The USA has the highest GDP. Zimbabwe has the lowest.


# Which countries have the highest and lowest life expectancy?

# In[20]:


#Germany has the highest life expectancy. Zimbabwe has the lowest.


# ## Step 11 Researching Data Context 

# Based on the visualization, choose one part the data to research a little further so you can add some real world context to the visualization. You can choose anything you like, or use the example question below.
# 
# What happened in China between in the past 10 years that increased the GDP so drastically?

# In[21]:


#China has experienced massive industrialization in the last few decades, which contributes to their increase in GDP


# ## Step 12 Create Blog Post

# Use the content you have created in this Jupyter notebook to create a blog post reflecting on this data.
# Include the following visuals in your blogpost:
# 
# 1. The violin plot of the life expectancy distribution by country
# 2. The facet grid of scatter graphs mapping GDP as a function Life Expectancy by country
# 3. The facet grid of line graphs mapping GDP by country
# 4. The facet grid of line graphs mapping Life Expectancy by country
# 
# 
# We encourage you to spend some time customizing the color and style of your plots! Remember to use `plt.savefig("filename.png")` to save your figures as a `.png` file.
# 
# When authoring your blog post, here are a few guiding questions to guide your research and writing:
# + How do you think the histories and the cultural values of each country relate to its GDP and life expectancy?
# + What would have helped make the project data more reliable? What were the limitations of the dataset?
# + Which graphs better illustrate different relationships??

# In[22]:


#Averaging GDP by population would've helped make it easier to compare large countries to small countries
#Bar charts make it easier to compare the avg GDPs, while the facet grids and line plots are easier to see trends over time

