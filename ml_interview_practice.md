# Here are some machine learning interview practice questions. 
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
- Organizational, communication, writing and interpersonal skills
- Knowledge in SQL or other programming languages.
- Experience in any scripting language (Hadoop, R, SAS Miner, Python, Matlab, SSPS).
- BA / BS in Computer Science, Math, Physics, Engineering, Statistics or other technical field

## Questions 
For each of the questions below, answer as if you were in an interview, explaining and justifying your answer with two to three paragraphs as you see fit. For coding answers, explain the relevant choices you made writing the code.

1. We A/B tested two styles for a sign-up button on our company's product page. 100 visitors viewed page **A**, out of which 20 clicked on the button; whereas, 70 visitors viewed page **B**, and only 15 of them clicked on the button. Can you confidently say that page **A** is a better choice, or page **B**? Why?

ANSWER : 
- for Page **A**, given `100 visitors` , we have `20 clicks`
- for Page **B**, given `70 visitors`, we have `15 clicks`

Looking at the question alone, I think it will be a **bias conclusion** to say that **`A`** is better choice than **`B`**. 

Given that this has been tested, we cannot come to a conclusion. If we run the test again, we might arrive at a different outcome. 

One thing to do here is to use _probability_.
**NOTE** : 
> _I do not know if the pages were tested at the same time or separately. It could that two different pages where made and tested differently_


- with a total of `100 visits` and `20 clicks`, i will say a `1/5` is the probability that page **`A`** was clicked. 
- with a total of `70 visits` and `15 clicks` occured,  `3/14` is the probability that page **`B`** was clicked. 

One thing i will experiment here is to combine the probability (`PR` _to denote probability_).

So now, we have a total of `170` and `35` for **pages** and **visits** respectively.

```TO BE CONTINUED```