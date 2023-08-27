#!/usr/bin/env python
# coding: utf-8

# In[43]:
import json

f = open("output.txt")


# In[44]:


x = f.readlines()


# In[45]:


data = []
for i in x:
    i = i.strip()
    if i:
        data.append(i.split(":",1))


# In[46]:


f = open("combined_data.json")
names = json.load(f)


# In[47]:


for i in names:
    name = i["text"].split("\n")[0]
    name = name.split(" ", 1)[1]
    i["text"] = name


# In[48]:


names_dic = {}
for i in names:
    names_dic[i["id"]] = i["text"]


# In[49]:


names_dic.keys()


# In[50]:


json_data = []
entry = {}
for i in data:
    if i[0] == "Prompt ID":
        if entry:
            json_data.append(entry)
        entry = {"prompt_id": i[1], "description": names_dic[int(i[1].strip())], "headlines": []}
        headline = {}
    headline[i[0]] = i[1]
    if i[0] == "Output":
        entry["headlines"].append(headline)
        headline = {}
        
json_data.append(entry)    


# In[51]:


import json


# In[52]:


with open("output_dataset.json","w") as f:
    json.dump(json_data, f)


# In[ ]:




