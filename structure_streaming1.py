#!/usr/bin/env python
# coding: utf-8

# In[1]:


import findspark
findspark.init('/home/mysparkub/spark-3.0.0-bin-hadoop2.7')
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split
spark = SparkSession.builder.appName('struct_streaming1').getOrCreate()
lines = spark.readStream.format("socket").option('host', 'localhost').option('port', 9999).load()
words = lines.select(explode(split(lines.value, " ")).alias("word"))
wordCounts = words.groupBy("word").count()
query = wordCounts.writeStream.outputMode("complete").format("console").start()
query.awaitTermination()


# In[2]:





# In[3]:





# In[13]:





# In[20]:





# In[21]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




