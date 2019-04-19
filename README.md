# Topic Modeling US Top 40 Song Lyrics From 1960-Today To Analyze Trends In American Culture

I wanted to analyze the changes in american culture by looking at the Top 40 songs lyrics. I used Latent Semantic Analysis to topic model and Tableau to visualize the changes. This project was completed in 2 weeks, including time to prepare for a presentation. I used a Billboard API and Genius Lyrics API to pull in the top 40 music and its lyrics respectively. I stored the lyrics in a NoSQL database and used Spacy to lematize the lyric words, along with some of my own preprocessing. I attempted LSA, LDA, and NNF to find topics, and used different natural language information retrieval techniques such as Word2Vec and gramming word combinations, however a simple count worked best for topic modeling. I then used Latent Dirichlet Allocation, Latent Semantic Analysis, Non-Negative Matrix Factorization, and even a K-Means Clustering with further topic modeling to find distinct topics, LSA ended up working best. With my topics finalized, I visualized the change in topic popularity over the decades using Tableau and found the most similar songs for each topic.

## Tools Used During Project

API: Billboard and Genius Lyrics  
Data Storage: MongoDB and Google Cloud  
Text Processing: Spacy  
Modeling: SKLearn  
Graphing: Tableau  

## Authors

* **Jack Olmstead** - [LinkedIn](https://www.linkedin.com/in/jolmstead495/)
