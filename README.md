# Movie-recommendation-system
The dataset used for the Movie Recommendation System is a 5k rating dataset. This dataset includes: 
1) Movie Id
2) Rating
3) Genres
4) Actor's Name
5) Director's Name
6) Year of Release
7) Popularity 
8) Run Time
9) Budget
10) Revenue

Our project contains an interface through which the user can interact with the project. In the user interface the user can enter the name of the movie that the user has watched recently.
So now the machine will get a list of movies that are similar to the movie the user entered. The list is based on features that are similar to the movie the user entered.

Approach Used:


* classification

we cant use the classifiaction technique because we cannot recommend the movie using bi-class classifiaction. so it is not more suitable method to recommend.

* regression

even by using regression models we cant recommend the movie to the user .because it is used to predict but we need to recommend the movie . so it is not useful method to recommend the movie.

* Clustering

To recommend a list of movies to the user we used the clustering technique. The movies in the dataset are divided into clusters based on features Rating, Genres, Actor's names, Director name, Year of Release.   
By using these features weights are generated. Based on these weights the movies in the dataset are divided into clusters. Once the user inputs the name or names of the movies watched
recently, it finds the cluster to which the input movie belongs. And it finds the cluster which has the maximum repetition. 

From this, it will calculate the cosine similarity between user input and cluster. Now we will get a shortlist of movies that are having cosine similarity greater than 0.57.
Form this shortlist it will recommend random 5 movies.

These movies will be displayed in the user interface.


