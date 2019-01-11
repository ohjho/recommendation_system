# How Latent Factor Analysis Work

Latent factors refer to the underlying factors `d` that actually help to explained the observed data (book ratings `R` in our case).  
![Image of Latent Factor Matrix](https://static1.squarespace.com/static/51af568be4b0b9ab836e2474/t/590c6b44d1758ebf2c442418/1493986118765/)

For a given user `i`, his rating of book `j`, where `k` is the number of factors:  
![function of rij](https://static1.squarespace.com/static/51af568be4b0b9ab836e2474/t/590f79b086e6c025ede556e5/1494186471184/Screen+Shot+2017-05-07+at+2.18.33+PM.png)

And we want to minimize the following **error/loss function**:  
![error function](https://static1.squarespace.com/static/51af568be4b0b9ab836e2474/t/590f6913ebbd1a0ad37541b3/1494182166078/Screen+Shot+2017-05-07+at+2.28.17+PM.png)

The catch is that our rating matrix `R` is sparse. Therefore, there's an inherent bias in that our model only *learn* from movies and users who provided ratings. To prevent **overfitting** because of the **bias**, we can introduce a regularization term, **Lambda**:  
![loss function with lambda](https://static1.squarespace.com/static/51af568be4b0b9ab836e2474/t/590f6921f5e23141033c2260/1494186587114/)

## SVD
SVD, **Singular Value Decomposition**, is a common method used for matrix factorization. Despite it being used mainly for **dense matrices** (as [Hug][url_hug_p3] and [Davis](https://www.eecs.umich.edu/eecs/etc/events/showevent.cgi?1857) explained), it does help us understand the basic concepts of how matrices can be decomposed.

Here, SVD decompose the dense rating matrix `A` into two unitary matrices `U` and `V` and a diagonal matrix `sigma`:  

![image of SVD](https://cdn-images-1.medium.com/max/800/1*W4MnB2hyvgqedLmwJLrpqw.png)

`U` represents how much each user like each *feature*. `sigma`, the diagonal matrix, is essentially the weights of each *feature*. And `V` represents how relevant each *feature* is to each movie.

## SVD for Latent Factor Analysis
As [Hug][url_hug_p4] mentioned, *SVD* in the context of recommendation systems is **not** real SVD. It is only *SVD* inspired.

## Our model for Latent Factor Analysis
Building on [Hug's work][url_hug_p4] and many others in the data science community, we also used **SGD (stochastic gradient descent)** to decompose the **sparse user rating matrix** in order to predict users' ratings and create recommendations.

[Our Juypter Notebook]() illustrated the approach we took, and a comparison to Hug's [surprise package's][url_surprise] results (looking primarily on RMSE). Presentation slides are [here](https://gitpitch.com/ohjho/recommendation_system/master?p=latent_factor_analysis)

## Readings:
* [How Netflix recommend movies?](https://www.youtube.com/watch?v=ZspR5PZemcs&t=186s) is a great intro video on YouTube by Luis Serrano, Head of Content in AI and Data Science at Udacity
* [Understanding matrix factorization for recommendation](http://nicolas-hug.com/blog/matrix_facto_1) by Nicolas Hug, the creator of the **surprise** library, on how his SVD implementation work. In [part 3][url_hug_p3], he discusses at length on how to do SVD on a **sparse matrix**.
* [Recommendations](http://www.ilanman.io/blog/2017/5/7/recommendations) by Ilan Man, Head of Data at TrialSpark
* [Matrix Factorization: A Simple Tutorial and Implementation in Python](http://www.albertauyeung.com/post/python-matrix-factorization/) by Albert Yeung, ML engineer at zwoop
* [Movie Recommendation using Regularized Matrix factorization](https://github.com/metpallyv/MovieRecommendation): a GitHub Repo
* [The 4 Recommendation Engines That Can Predict Your Movie Tastes](https://medium.com/@james_aka_yale/the-4-recommendation-engines-that-can-predict-your-movie-tastes-bbec857b8223) with example code on Github
* [A Gentle Guide to Recommender Systems with Surprise](https://kerpanic.wordpress.com/2018/03/26/a-gentle-guide-to-recommender-systems-with-surprise/) with example code on Github
* [Gradient Descent in Python](https://towardsdatascience.com/gradient-descent-in-python-a0d07285742f) by Toward Data Science with sample code for GD, SGD, and mini batch SGD

[url_hug_p3]: http://nicolas-hug.com/blog/matrix_facto_3
[url_hug_p4]: http://nicolas-hug.com/blog/matrix_facto_4
[url_surprise]: http://surpriselib.com/
