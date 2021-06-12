# pingpong_app

This pingpong app keeps score of a pingpong game, as well as participating players. the players and their scores are saved in the database gameDatabase.db. The app runs through flask on local host. To play the game go to localhost:5000 and enter two names. Once one player reaches more than 10 points and has at least 2 points advantage over the opponent that player wins, the game is over, and the points are saved in the database. To get a list of players and their stats go to localhost:5000/players. 
