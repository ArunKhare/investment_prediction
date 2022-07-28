##Investment predictions
    predicting the stock price

### Start Machine Learning project.

### Software and account Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)

-----------------------------
Creating conda environment
-----------------------------
conda create -n venv python==3.9 -y
install ipykernel # jupyternotebook
```
conda activate venv
```
pip install -r requirements.txt
```
------------------------------
Setting up GIT:
------------------------------
create git repository in github.com
local folder requried: .gitignore
CLi commands @ local project Root folder path:

git init
```
git add .
```
git commit -m "first commit"
''''''
git remote add origin git@github.com:ArunKhare/Investment_prediction.git
'''''''
git push -u origin master / git push origin


> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status 
```
git status
```
To check all version maintained by git
```
git log
```

To send version/changes to github
```
git push origin main
```

To check remote url 
```
git remote -v

-------------------------------------------
To setup CI/CD Pipeine with heroku ;
-------------------------------------------
local files required:
    1. Dockerfile 
    2. github\workflows\main.yaml

create an app in Heroku
copy the API key forom setting:

1. HEROKU_EMAIL: <emailid>
2. HEROKU_API_KEY:<heroku api key>
3. HEROKU_APP_NAME : stockprice_pred

run the app :
open app in heroku
app opens in browser .
share the link in browser 
-------------------------------------------

********************************************************
A separate execution with Docker:
- docker needs to be installed in your system
steps:
--------------------------------
BUILD DOCKER IMAGE
--------------------------------
docker build -t <image_name>:<tagname> . # dot to bring in all the file in to the docker imagedocker 
Note: Image name for docker must be lowercase
'''''''''''''''''''
To list docker image
docker images
'''''''''''''''''''
Run docker image
docker run -p 5000:5000 -e PORT=5000 <image_id>  # passing a environment variable port=5000
''''''''''''''''''''
Run on web :
localhost:5000
'''''''''''''''''''
To check running containers in docker
docker ps
'''''''''''''''''''
Tos stop docker conatiner
docker stop <container_id>
'''''''''''''''''''
**********************************************************

Preface
'Investment prediction' here vis-a-vis Stock Market prediction  predict the stock's price considering various aspects of the stock market that can influence the price..
In this project I am considering the historical prices to predict the price on a future day.

Build Stock Market Prediction model using Machine Learning:

Target : what will be the price of the stock next day

Machine learning uses Optimization algorithms, Cross-Validation technique, advanced mathematical algorithms generally requires enormous computational power to come with rulst,
with result being higly accurate( but low in interpretability)

Unspervised learning setup can  used to group silimar performing stocks together.
Time Series algorithms: Stock market prices are affected by time factors such as time of day, previous day performance etc.
Regression based algorithms: can be used in combination or separately.

Types of useful data:
time series-based algorithm: expects data should be indexed by continuous stretches of time sothat trend seasonality, cyclicity and simliar such time-base components can be captured to understand what the stock price should be.
regression-based algorithm: large no of inputs can be provided

ML techniques:
Creating a good stock price prediction model is particularly challenging because it is non-linear

1. Linear Regression:
    advantages: high in interpretability as user can know which fator influences the price of stock more and how much.
    disadvantages: it is highly limited in its scope. Many predictors cannot be used

2. ARIMA famliy of techniques: stands for Auto-Regressive Integrated Moving average
    advanteages: consider time component

    parameters:  AR, I, MA  values are p,q - numbers of last values and erros considering for forecasting values
                                        d is the diffrence to make the data stationary

3. Prophet: Developed by facebook. advanced version of ARIMA
    advantages: requires little data preparation and can work with large datasets.
    disadvantages: abysmal accuracy compared to other techniques, especially deep learnin-based.


4. SVR:
    advantages: using kernels that can make this algorithm work in a non-linear manner.

5. KNN :
    advantages: allows the data scientist the opportunity to look for similar patterns and predict the target
    disadvantages: The major problem with this method is that it will consider all the variables that we provide; thus, it gives equal importance to all the predictors all the time
                    The prediction is highly sensitive towards the value of K and the chosen distance metric, which can hugely alter the results, thus making the technique rigid and not as dynamic as needed.
6. Randomforest:
     advantages: predict the stock process as they can also solve regression-based problems. It uses bootstrapping and pasting techniques. It randomly picks different features and creates multiple Decision, Tree models
        being highly interpretable
independent variable: 
