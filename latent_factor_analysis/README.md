# How Latent Factor Analysis Work

Latent factors refer to the underlying factors `d` that actually help to explained the observed data (book ratings `R` in our case).  
![Image of Latent Factor Matrix](https://static1.squarespace.com/static/51af568be4b0b9ab836e2474/t/590c6b44d1758ebf2c442418/1493986118765/)

For a given user `i`, his rating of book `j`, where `k` is the number of factors:  
![function of rij](https://static1.squarespace.com/static/51af568be4b0b9ab836e2474/t/590f79b086e6c025ede556e5/1494186471184/Screen+Shot+2017-05-07+at+2.18.33+PM.png)

And we want to minimize the following **error/loss function**:  
![error function](https://static1.squarespace.com/static/51af568be4b0b9ab836e2474/t/590f6913ebbd1a0ad37541b3/1494182166078/Screen+Shot+2017-05-07+at+2.28.17+PM.png)

The catch is that our rating matrix `R` is sparse. Therefore, there's an inherent bias in that our model only *learn* from movies and users who provided ratings. To prevent **overfitting** because of the **bias**, we can introduce a regularization term, **Lambda**:  
![loss function with lambda](https://static1.squarespace.com/static/51af568be4b0b9ab836e2474/t/590f6921f5e23141033c2260/1494186587114/)



## Readings:
* [Recommendations](http://www.ilanman.io/blog/2017/5/7/recommendations) by Ilan Man, Head of Data at TrialSpark
* [Matrix Factorization: A Simple Tutorial and Implementation in Python](http://www.albertauyeung.com/post/python-matrix-factorization/) by Albert Yeung, ML engineer at zwoop
* [Movie Recommendation using Regularized Matrix factorization](https://github.com/metpallyv/MovieRecommendation): a GitHub Repo
