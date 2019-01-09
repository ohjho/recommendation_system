# Content- Based Filtering
This is a simple way for user to implement the model of content-based of recommender system. We will use Python to illustrate the following. Basically, Content -Based Filtering is going to find the missing value with the recommender system.  

After the recommender is trained by the arrays, the list of documents exist and are more similar to the input document.
The training process will be 3 main steps:
¡E	Pre-processing: stopwords removal, stemming, html tag stripping
¡E	Before Clustering : Document vectors formation using tf-idf
¡E	Clustering: Find the cosine similarity scores between all document vectors

## Reference and acknowledgement:
Running the Program
recommendBasic computes recommendations using the threshold user profile builder, and recommendWeighted uses the weighted user profile builder.
For example:
$ ./gradlew recommendBasic -PuserId=91

Special thanks to https://github.com/Mahendra-Maiti/Content-based-recommender/blob/master/README.md

