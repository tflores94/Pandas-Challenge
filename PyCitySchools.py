#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# PyCity Schools Analysis
- Your analysis here


# In[ ]:


# Dependencies and Setup
import pandas as pd
from pathlib import Path

# file to load (Remember to Change These)
school_data_to_load = Path("Resources/schools_complete.csv")
student_data_to_load = Path("Resources/students_complete.csv")

# Read School and Student Data File and store into Pandas DataFrames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset.
school_data_complete = pd.merge(student_data, school_data, how="left", on="school_name")
school_data_complete.head()


# In[ ]:


# Calculate the total number of unique schools
school_count = len(school_data_complete["school_name"].unique())
school_count


# In[ ]:




