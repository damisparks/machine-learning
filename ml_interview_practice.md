# Machine Learning Interview Question.
First, it is important that you find **_`Find a job posting`_**.
Make you meet at least **70%** of the requirement. Then, answer the question as you would do at the interview.

# Sample Job Description.
## Data Scientist
- Location : Lisbon
- Company name : Accenture
Accenture is a leading global professional services company, providing a broad range of services and solutions in strategy, consulting, digital, technology and operations. Accenture works in the intersection of business and technology to help clients improve their performance and create sustainable value for their stakeholders. With approximately 425,000 people serving clients in more than 120 countries, Accenture drives innovation to improve the way the world works and lives. [Visit us](www.accenture.com.).

## Job Description
This is an opportunity to join **`ACCENTURE DIGITAL`** as a `Junior Data Scientist` within the APPLIED INTELLIGENCE practice.

- Applied Intelligence is the intelligent technology and human ingenuity applied to the core of business - across every function and process - to address our clients' most complex challenges.

- They combine artificial intelligence with deep industry and analytic expertise to help our clients embrace intelligent technologies confidently and responsibly.

### Mandatory Qualification
- 1-2 years of experience doing quantitative analysis
- Understanding of statistics (eg, hypothesis testing, regressions, etc ...)
- Organisational, communication, writing and interpersonal skills
- Knowledge in SQL or other programming languages.
- Experience in any scripting language (Hadoop, R, SAS Miner, Python, Matlab, SSPS).
- BA / BS in Computer Science, Math, Physics, Engineering, Statistics or other technical field

## Questions
Instruction :
_For each of the questions below, answer as if you were in an interview, explaining and justifying your answer with two to three paragraphs as you see fit. For coding answers, explain the relevant choices you made writing the code._

### Question 1.
We A/B tested two styles for a sign-up button on our company's product page. 100 visitors viewed page **`A`**, out of which 20 clicked on the button; whereas, 70 visitors viewed page **`B`**, and only 15 of them clicked on the button. Can you confidently say that page **`A`** is a better choice, or page **`B`**? Why?

### Solution 1:
- for Page **A**, given `100 visitors` , we have `20 clicks`
- for Page **B**, given `70 visitors`, we have `15 clicks`

Looking at the question alone, I think it will be a **bias conclusion** to say that **`A`** is better choice than **`B`**.
Given that this has been tested, we cannot come to a conclusion. If we run the test again, we might arrive at a different outcome.
One thing to do here is to use _probability_.

#### NOTE:
> _I do not know if the pages were tested at the same time or separately. It could that two different pages where made and tested differently_


- with a total of `100 visits` and `20 clicks`, i will say a `1/5` is the probability that page **`A`** was clicked.
- with a total of `70 visits` and `15 clicks` occurred,  `3/14` is the probability that page **`B`** was clicked.

One thing i will experiment here is to combine the probability (`PR` _to denote probability_).

So now, we have a total of `170` and `35` for **pages** and **visits** respectively.

![Solution 1](/solution_image/solution_1.jpg)


Given this, I think the positioning of button on Page A has a greater probability of being clicked than the position of button on Page B.

### Question 2.
Can you devise a scheme to group Twitter users by looking only at their tweets? No demographic, geographic or other identifying information is available to you, just the messages they’ve posted, in plain text, and a timestamp for each message.

In JSON format, they look like this:
```json
{
    "user_id": 3,
    "timestamp": "2016-03-22_11-31-20",
    "tweet": "It's #dinner-time!"
}
```
Assuming you have a stream of these tweets coming in, describe the process of collecting and analysing them, what transformations/algorithms you would apply, how you would train and test your model, and present the results.

### Solution 2.
Based on the assumption that i have stream of tweets coming in, there is no data shortage.

#### Collection of data
It is important to know how to collect the data you want. In this case, we need data collection on Tweeter. To collect data on Twitter, my suggestion is to create an account and then go to [Twitter API](apps.twitter.com) to create an app that allows you to collect Twitter data. Just make sure you don't ask too much, because there is a limit on how many times you can request Twitter data.

+ If you want to do a one-time collection of tweets, you should use the **REST API**.
+ If you want to do a continuous collection of tweets for a specific time period, you should use the **streaming API**.
+ It is required that you have a private key and token.
For more information about getting information on Twitter, please checkout this [Twitter Developer Search Tweets](https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets.html)

**NOTE** :
> _The assumption is that we are not given the demographical information._


#### Analysing the data.
We need to group the data we have. Since we have the geographical information and other identifying information we can do some clustering. Below are ways i will group the data :
- **Location** : Location is one important way of grouping the data. One thing i will take into consideration is the _Latitude and Longitude_. Normally, when we tweet, i believe there is a timestamp and location are well. Given if you disabled the phone GPS or location services, Twitter will still classify tweets using satellite services or use the phone/device IP-address. The only issue here is the accuracy may be nearest in metres.
- **Time** : My intuition here is that tweets could grouped based on time they were tweets, retweeted and more. For instance, if i am interested in knowing what time of the day, do users tweet the most ? I could use the timestamp. I could also use it in combination with location if i want to know what time of the day, week, month do users tweet the most in a region.
- **Usage** : Usage is how often Twitter is used. e.g _How many  tweets, retweets, mentioned, many more._ I also think that what users interact with could be used here. e.g _now all users on Twitter tweets every day, but most do interact with the application, website, or view others tweets as well._ It also contains how active the user is.

#### Algorithms
After getting the features, it is important to state the kind of algorithm to be used.
In this scenario, i will use a **clustering algorithm** such as **`k-Means`** or **`gaussian mixture models`**. We can optimise the algorithm in order to have the best separation between specified groups.

#### Training, Testing and Communicating Results.
One of the golden rule in machine learning is not to train your model with a testing set.
It is very important to divide your dataset into sets. That is you will have your `training dataset`, `testing dataset`, and `validation set`. Normally, i use divide the dataset using a percentage of `70,20,10`. Presenting the result would be done using different data visualization libraries like [seaborn](https://seaborn.pydata.org/), [Matplotlip](https://matplotlib.org/) etc.

_working in progress_
