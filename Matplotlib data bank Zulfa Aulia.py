#!/usr/bin/env python
# coding: utf-8

# In[5]:


#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# reading the database 
data = pd.read_csv("C:/Users/LENOVO/Downloads/data bank.csv")

# printing the top 10 rows 
display (data.head (10))


# In[6]:


import pandas as pd
import matplotlib.pyplot as plt

# reading the database 
data = pd.read_csv("C:/Users/LENOVO/Downloads/data bank.csv")

# Scatter plot with day against tip 
plt.scatter(data['job'], data['age'])

# Adding Title to the Plot 
plt.title("Scatter Plot")

# Setting the X and Y Labels 
plt.xlabel('job')
plt.ylabel('age')

plt.show()


# In[8]:


import pandas as pd
import matplotlib.pyplot as plt

# reading the database 
data = pd.read_csv("C:/Users/LENOVO/Downloads/data bank.csv")

# Scatter plot with day against tip 
plt.scatter(data['education'], data['age'], c=data['campaign'], s=data['duration'])

# Adding Title to the Plot 
plt.title("Scatter Plot")

# Setting the X and Y Labels 
plt.xlabel('education')
plt.ylabel('age')

plt.colorbar()

plt.show()


# In[10]:


import pandas as pd
import matplotlib.pyplot as plt

# Membaca database
data = pd.read_csv("C:/Users/LENOVO/Downloads/data bank.csv")

plt.plot(data['age'])
plt.plot(data['day'])

# Adding Title to the plot
plt.title("Scatter Plot")

plt.xlabel('job')
plt.ylabel('age')


plt.show()


# In[13]:


import pandas as pd
import matplotlib.pyplot as plt

# reading the database 
data = pd.read_csv("C:/Users/LENOVO/Downloads/data bank.csv")

# Scatter plot with day against tip 
plt.bar(data['education'], data['age'])

# Adding Title to the Plot 
plt.title("Bar Chart")

# Setting the X and Y Labels 
plt.xlabel('education')
plt.ylabel('age')

# Adding the Legends
plt.show()


# In[14]:


import pandas as pd
import matplotlib.pyplot as plt

# reading the database 
data = pd.read_csv("C:/Users/LENOVO/Downloads/data bank.csv")

# histogram of education
plt.hist(data['education'])

# Adding Title to the Plot 
plt.title("Histogram")

# Adding the Legends
plt.show()


# In[15]:


import pandas as pd
import matplotlib.pyplot as plt

# reading the database 
data = pd.read_csv("C:/Users/LENOVO/Downloads/data bank.csv")

# initializing the data 
education = ['secondary', 'tertiary', 'primary', 'unknown']
data = [23, 10, 35, 15]

# ploting the data
plt.pie(data, labels=education)

# Adding Title to the Plot 
plt.title("Education Data")

# Adding the Legends
plt.show()


# In[19]:


import matplotlib.pyplot as plt

# Creating data
education = ['secondary', 'tertiary', 'primary', 'unknown']
data = [23, 10, 35, 15]

# Plotting barchart
plt.bar(education, data)

# Saving the figure. 
plt.savefig("hasil.jpg")

# Saving figure by changing parameter values
plt.savefig("hasil1", facecolor='y', bbox_inches="tight",
            pad_inches=0.3, transparent=True)


# In[ ]:





# In[ ]:





# In[ ]:




