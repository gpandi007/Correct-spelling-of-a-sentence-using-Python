#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install textblob')


# In[2]:


from textblob import Word


# In[3]:


word = Word('appple')


# In[4]:


result = word.correct()

print(result)


# In[5]:


from textblob import Word


def correct_word_spelling(word):
    
    word = Word(word)
    
    result = word.correct()
    
    print(result)
    

correct_word_spelling('appple')


# In[6]:


from textblob import TextBlob


# In[10]:


sentence = TextBlob('A sentfencee to checkk!')


# In[11]:


result = sentence.correct()

print(result)


# In[13]:


from textblob import TextBlob


def correct_sentence_spelling(sentence):
    
    sentence = TextBlob(sentence)
    
    result = sentence.correct()
    
    print(result)


# In[ ]:





# In[ ]:




