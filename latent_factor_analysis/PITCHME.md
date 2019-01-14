---?image=https://source.unsplash.com/Oaqk7qqNh_c
<!-- Welcome stack
_       __     __                                  __             __  
| |     / /__  / /________  ____ ___  ___     _____/ /_____ ______/ /__
| | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \   / ___/ __/ __ `/ ___/ //_/
| |/ |/ /  __/ / /__/ /_/ / / / / / /  __/  (__  ) /_/ /_/ / /__/ ,<   
|__/|__/\___/_/\___/\____/_/ /_/ /_/\___/  /____/\__/\__,_/\___/_/|_|  

-->
### @color[black](Latent Factor Analysis)
#### @color[black](aka Matrix Factorization)
+++
@snap[north]
### Overview
@snapend
@snap[west]
@ul
* Matrix Factorization
* SVD
* SGD
* surprise
* Our Implementation
@ulend
@snapend
+++
### Results Comparsion
Recommendations for user `276847` using...

@div[left-50 fragment]
surpise-svd:
![svdpp results](latent_factor_analysis/pitch_assets/svdpp_recommend.png)
@divend

@div[right-50 fragment]
our SGD:
![our results](latent_factor_analysis/pitch_assets/our_recommendation.png)
@divend

---?image=https://source.unsplash.com/dzCBKa8rIAM
<!-- Matrix Factorization


    __  ___      __       _         ______           __             _             __  _           
   /  |/  /___ _/ /______(_)  __   / ____/___ ______/ /_____  _____(_)___  ____ _/ /_(_)___  ____
  / /|_/ / __ `/ __/ ___/ / |/_/  / /_  / __ `/ ___/ __/ __ \/ ___/ /_  / / __ `/ __/ / __ \/ __ \
 / /  / / /_/ / /_/ /  / />  <   / __/ / /_/ / /__/ /_/ /_/ / /  / / / /_/ /_/ / /_/ / /_/ / / / /
/_/  /_/\__,_/\__/_/  /_/_/|_|  /_/    \__,_/\___/\__/\____/_/  /_/ /___/\__,_/\__/_/\____/_/ /_/



-->
### Matrix Factorization
+++?image=https://source.unsplash.com/dzCBKa8rIAM
#### Matrix Factorization
![mat factorization image](https://cdn-images-1.medium.com/max/1075/1*2i-GJO7JX0Yz6498jUvhEg.png)

+++?image=https://source.unsplash.com/dzCBKa8rIAM
### Singular Vector Decomposition
<img src='https://hadrienj.github.io/assets/images/2.8/singular-value-decomposition.png' height = '250' />

+++?image=https://source.unsplash.com/dzCBKa8rIAM
### Singular Vector Decomposition
<img src='https://research.fb.com/wp-content/uploads/2016/11/post00049_image0001.png' height = '450' />

---?image=https://source.unsplash.com/tMvuB9se2uQ
<!-- SGD stack


   _____ __________
  / ___// ____/ __ \
  \__ \/ / __/ / / /
 ___/ / /_/ / /_/ /
/____/\____/_____/  


-->
### Stochastic Gradient Descent

<img src='https://cdn-images-1.medium.com/max/800/1*Sa5kGcZIVNTLjrI8P-YsSQ.gif' width='450' />
+++?image=https://source.unsplash.com/tMvuB9se2uQ
### Stochastic Gradient Descent
@ul
* Randomly initialize `P` and `Q`
* For a given `epoch`, minimize:  

![sgd loss function](latent_factor_analysis/pitch_assets/sgd_lossfun.png)
+++?image=https://source.unsplash.com/tMvuB9se2uQ
### Stochastic Gradient Descent
* adjust `p(u)` and `q(i)` at each `epoch` according to:  

![sgd derivatives](latent_factor_analysis/pitch_assets/sgd_derivatives.png)
@ulend

---?image=https://source.unsplash.com/iVVBVb2RqLc
<!-- Surprise Stack


                               _         
   _______  ___________  _____(_)_______
  / ___/ / / / ___/ __ \/ ___/ / ___/ _ \
 (__  ) /_/ / /  / /_/ / /  / (__  )  __/
/____/\__,_/_/  / .___/_/  /_/____/\___/
               /_/                       

-->
### surprise
<br />
![image of surprise library](latent_factor_analysis/pitch_assets/surprise_logo.png)
+++?image=https://source.unsplash.com/iVVBVb2RqLc
### SVD vs SVD++
@div[top-50 fragment]
<img src='https://github.com/ohjho/recommendation_system/raw/master/latent_factor_analysis/pitch_assets/svd_rmse.png' height = '100' />
@divend
@div[bottom-50 fragment]
<img src='https://github.com/ohjho/recommendation_system/raw/master/latent_factor_analysis/pitch_assets/svdpp_rmse.png' height = '100' />
@divend
+++?image=https://source.unsplash.com/iVVBVb2RqLc
### SVD vs SVD++
Recommendations for user `276847` using...

@div[left-50 fragment]
surpise-svd:
![svdpp results](latent_factor_analysis/pitch_assets/svdpp_recommend.png)
@divend

@div[right-50 fragment]
surprise-svd++:
![fake our model results](latent_factor_analysis/pitch_assets/svd_recommend.png)
@divend
---?image=https://source.unsplash.com/JFeOy62yjXk
<!-- Our Implementation Stack


   ____                ____                __                          __        __  _           
  / __ \__  _______   /  _/___ ___  ____  / /__  ____ ___  ___  ____  / /_____ _/ /_(_)___  ____
 / / / / / / / ___/   / // __ `__ \/ __ \/ / _ \/ __ `__ \/ _ \/ __ \/ __/ __ `/ __/ / __ \/ __ \
/ /_/ / /_/ / /     _/ // / / / / / /_/ / /  __/ / / / / /  __/ / / / /_/ /_/ / /_/ / /_/ / / / /
\____/\__,_/_/     /___/_/ /_/ /_/ .___/_/\___/_/ /_/ /_/\___/_/ /_/\__/\__,_/\__/_/\____/_/ /_/
                                /_/                                                              

-->
### Our implementation
+++?image=https://source.unsplash.com/JFeOy62yjXk
### Our implementation
#### Biases
![our fun](latent_factor_analysis/pitch_assets/our_math.png)
+++?image=https://source.unsplash.com/JFeOy62yjXk
### Our implementation
#### Evaluation
![our rmse](latent_factor_analysis/pitch_assets/our_rmse.png)
+++?image=https://source.unsplash.com/JFeOy62yjXk
### Our implementation
#### Recommendation
![our recommendation](latent_factor_analysis/pitch_assets/our_recommendation.png)
