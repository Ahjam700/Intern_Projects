# Welcome to My Imdb Api
A lightweight backend API for searching movies by genre, built with Flask. This project parses a CSV file to
filter movies based on a provided genre, delivering JSON responses.


## Task
-What is the problem? 
Movie search by genre requires handling and filtering a list of movie titles efficiently. 

-And where is the challenge?
Challenges include parsing CSV data, enabling case-insensitive search, and providing quick
JSON responses without a database.


## Description
-How have you solved the problem?
Using Python's Flask framework, this API serves filtered movie data by parsing a CSV file and
responding with JSON. It filters based on genre using case-insensitive matching, allowing smooth
search functionality without a database.


## Installation
-How to install your project? npm install? make? make re?
To set up this project, clone the repository and install the necessary dependencies by running.
bash pip install flask

## Usage 
-How does it work?
The API parses a movies.csv file containing titles and genres. When a genre query is passed in a GET
request to /. it filters and returns relevant movies in JSON. This simple design enables a functional
movie search by genre.


./my_project argument1 argument2


### The Core Team


<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>
