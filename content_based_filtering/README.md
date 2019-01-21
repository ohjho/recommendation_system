# Content-Based Filtering
We explored that there are 2 approaches for Content-Based Filtering.

## Approach 1: Recommendation through Description of the Content
In this approach based on the description of the item, the user is suggested an item. The description goes deeper into the product details, i.e title, summary, taglines, genre. It provides much more information about the item. The format of these details are in text format(string) and is important to convert

Term Frequency-Inverse Document Frequency(TF-IDF) TF-IDF is used in Information Retrieval for feature extraction purposes and it is a sub-area of Natural Language Processing(NLP).

In the End, TF-IDF is a measure used to evaluate how important a word is to a document in a document corpus. The importance of the word increases proportionally to the number of times a word appears in the document but is offset by the frequency of the word in the corpus.

## Approach 2: Using Rated Content to Recommend
Approach 2 leverages description or attributes from items the user has interacted to recommend similar items. It depends only on the user previous choices, making this method robust to avoid the cold-start problem. For textual items, like articles, news and books, it is simple to use the article category or raw text to build item profiles and user profiles.

Suppose I watch a particular genre movie I will be recommended movies w.r.t that specific genre. The Title, Year of Release, Director, Cast are also helpful in identifying similar movie content.