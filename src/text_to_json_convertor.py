#!/usr/bin/env python
# coding: utf-8

# In[1]:


f = open("prompting-jokes/src/output.txt")


# In[2]:


x = f.readlines()


# In[4]:


data = []
for i in x:
    i = i.strip()
    if i:
        data.append(i.split(":",1))


# In[7]:


json_data = []
entry = {}
for i in data:
    if i[0] == "Prompt ID":
        if entry:
            json_data.append(entry)
        entry = {"prompt_id": i[1], "headlines": []}
        headline = {}
    elif i[0] != "Output":
        headline[i[0]] = i[1]
    else:
        entry["headlines"].append(headline)
        headline = {}
json_data.append(entry)    


# In[14]:


import json


# In[16]:


with open("output_dataset.json","w") as f:
    json.dump(json_data, f)


# In[ ]:




