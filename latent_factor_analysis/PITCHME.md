---?image=https://source.unsplash.com/ptA_7ODacAk/
<!-- Welcome stack
_       __     __                                  __             __  
| |     / /__  / /________  ____ ___  ___     _____/ /_____ ______/ /__
| | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \   / ___/ __/ __ `/ ___/ //_/
| |/ |/ /  __/ / /__/ /_/ / / / / / /  __/  (__  ) /_/ /_/ / /__/ ,<   
|__/|__/\___/_/\___/\____/_/ /_/ /_/\___/  /____/\__/\__,_/\___/_/|_|  

-->
@snap[north-east]
### @color[black](Latent Factor Analysis)
@snapend
+++?image=https://source.unsplash.com/PR9fXnVzfzw/
@snap[west]
### @color[white](Overview)
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
<br />
@div[left-50 fragment]
![svdpp results](latent_factor_analysis/pitch_assets/svdpp_recommend.png)
@divend
@div[right-50 fragment]
![fake our model results](latent_factor_analysis/pitch_assets/svd_recommend.png)
@divend

---?image=https://source.unsplash.com/9pw4TKvT3po/
<!-- Matrix Factorization


    __  ___      __       _         ______           __             _             __  _           
   /  |/  /___ _/ /______(_)  __   / ____/___ ______/ /_____  _____(_)___  ____ _/ /_(_)___  ____
  / /|_/ / __ `/ __/ ___/ / |/_/  / /_  / __ `/ ___/ __/ __ \/ ___/ /_  / / __ `/ __/ / __ \/ __ \
 / /  / / /_/ / /_/ /  / />  <   / __/ / /_/ / /__/ /_/ /_/ / /  / / / /_/ /_/ / /_/ / /_/ / / / /
/_/  /_/\__,_/\__/_/  /_/_/|_|  /_/    \__,_/\___/\__/\____/_/  /_/ /___/\__,_/\__/_/\____/_/ /_/



-->
@snap[north]
### Matrix Factorization
@snapend
+++
@snap[north-east]
#### Matrix Factorization
@snapend
<br /><br />
<img src='https://camo.githubusercontent.com/8a871316416dcf58b9e2d6ee9f732d6a5b0f449b/68747470733a2f2f737461746963312e73717561726573706163652e636f6d2f7374617469632f3531616635363862653462306239616238333665323437342f742f3539306336623434643137353865626632633434323431382f313439333938363131383736352f' height='450' />

---?image=https://source.unsplash.com/FRQUz7W1SvI/
<!-- SVD Stack


   ______    ______
  / ___/ |  / / __ \
  \__ \| | / / / / /
 ___/ /| |/ / /_/ /
/____/ |___/_____/  



-->
@snap[north]
### Singular Vector Decomposition
@snapend
+++
@snap[north-east]
### Singular Vector Decomposition
@snapend
<br />
<img src = 'https://camo.githubusercontent.com/f3a071674e23aac009988b6f913d9efec9e541e3/68747470733a2f2f63646e2d696d616765732d312e6d656469756d2e636f6d2f6d61782f3830302f312a57344d6e4232687976677165644c6d774a4c727071772e706e67' width = '500' />

---?image=https://source.unsplash.com/jG1z5o7NCq4/
<!-- SGD stack


   _____ __________
  / ___// ____/ __ \
  \__ \/ / __/ / / /
 ___/ / /_/ / /_/ /
/____/\____/_____/  


-->
### Stochastic Gradient Descent
+++
@snap[north-east]
### Stochastic Gradient Descent
@snapend
<br />
<img src = 'https://cdn-images-1.medium.com/max/800/1*Sa5kGcZIVNTLjrI8P-YsSQ.gif' height = '450' />

<!-- Surprise Stack


                               _         
   _______  ___________  _____(_)_______
  / ___/ / / / ___/ __ \/ ___/ / ___/ _ \
 (__  ) /_/ / /  / /_/ / /  / (__  )  __/
/____/\__,_/_/  / .___/_/  /_/____/\___/
               /_/                       

-->
@snap[north]
### surprise
@snapend
<br />
![image of surprise library](http://surpriselib.com/logo_white.svg)
