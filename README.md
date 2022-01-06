IMPLMENTATION

Overview:
There are seven different modules in this genetic algorithm (6 required modules for the genetic algorithm and one main that calls the methods in the module
based on the genetic process).

Main.py:
There are two main purposes of the main function. 
Purpose 1: The first thing that the main is doin g is webscraping in the training data from HockeyDB.com. 
While I was coming up with this I noticed that the url for different drafts are the same other than the one part saying the year. Therfore I created a list 
of years that includes every year I want to include in the taining data and using a for loop I go through year by year importing the player number, position,
points scored, and games played. The results of a draft first get saved in a list of list (pool) for each year and then they get put into a list of list of
list, which is what will be passed in the fitness function later.

Purpose 2: The second purpose of the main.py is to run the genetic algorithm process. The first step is to initialize the population and evalute the 
fitness of each individual in the population. Next, the algorithm begins it's genetic process for generations at a time. The first while loop is accounting 
for that. It will run for the amount of generations that are intialized. Next, the parentSelection module is called in order to pick parents for the
respective generation. Now, once the parents are selected the next step is to generate the offspring. The offspring are generated unsing selected parents
in the mating pool. The crossover function is called to peform a cut-and-crossfill and generate offspring at a probability of 80%. If its does not get 
called the offspring will just be the parents. Next we preform mutation on the offspirng at a probability of 25%. Mutation will change a single point. 
Finally, the offspring will get appended into a list that will hold all the offspring and then the fitness will be evaluated. Now that there is a offspring
with a fitness value, the survivor selection function gets called and will replace the worst parents with the offspring. Finally, we find the generation 
with the highest fitness and select that as our outputed draft.

Initialization.py:
The initialization functions purpose is there because I cannot read in the data of the current pool of players for the draft (as they are protected and
you need a paid subscription to see their stats), I have decided to generate my own data. The representation
will be a list of list of list for the population (similar to assignment 2). Each list of list will be a draft pool in
order of first overall to 31st overall. Then inside the list we will have the first index be the player number, then
position then points they got. The number of points that each player gets is based off of their positions and what players in their position 
usually get. Therefore, a defenceman typically gets between 28-55 points and a forward gets between 30-100. However, a defensmans points are usually worth
more to scouts, therefore if there is a direct comparison of points it's usually +25 for defenceman. In terms of games played, it usually depends on the
amount of points. Those with over 85 points typically played over 300 games, those within 50-85 played between 100-299 and those with less than 50 points
played between 60-100. There usually is no players drafted in the first round who have played under 60 games.  

Fitness.py
newPlayers:
This function will assign a mistake score to the generate draft pool that is being passed in. It evalutes this by comparing each player's games played an
points scored with the players drafted before them. If the players drafted before them have less points or less games played then the mistake counter gets
incrmented by one. If two players have the same amount of points or games played, the mistake will only be incrmented if the player drafted later is a 
defenceman. This is because good defencman are harder to find and therefore, are more highly scouted. 
		
oldPlayers:
The oldPlayers function does the same process as newPlayers, except for the training data. The reason it's in a different function is because for the 
training data we pass the entire list of list of list and instead of returning one number for the mistake. it returns a list of mistakes. This is going to
be handy in the error calculation function.

error:
This function is where the sum of error is caluclated. The two parameters that are passed through is the mistake int from the newPlayers function and the
list of mistakes from the olPlayers function. The way that it calulates this error is by subtracting the mistake for newPlayers with each index in the list
of mistakes. It stores all those values in the temp list and then goes through the temp list and adds the values all up to a final fitness score. This 
fitness score is what is returned from this module. 
 
fitness:
This is the function that is called from main and it's purpose is just to call the functions within this modules in order and return the final fitness score.
The two parameters that are pass into this are the indivdual from the population and the entire list of list of list from the training data. 

Recombination.py
The recombination module will preform a cut and-crossfill crossover with the parents to produce a offspring. The crossover function takes in two parents 
that are list of list and picks a random index to split both of them in. It will append the first half of one parent to one offspring and the other half
of the other parent to the same offspring. Therefore, a offspring will be the front half of one parent and the back half of another parent.

Mutation.py
This function takes in a individual that is a list of list. The mutation function will pick two random indices from 0 to the length of the individual, it
will then store the values of the two indices. It then changes the values by putting one value at the others spot and vice versa.  

parentSelection.py
The parent selection method that I will use is going to be tournament without replacement. Now typically parent selection for genetic programs are done by 
fitness proportional selection, however I believe that tournament selection is going to be more useful to us. There are going to be three parameters passed
into the tournament funstion: the list of fitnesses, a integer that is the mating pool size and the length of the tournament that is also a integer. How 
this will work is we will run the tournament to find the highest possible fitness between 4 randomly selected indices. In order to do this we will run one
for loop that will go through the mating pool size and then a nested for loop for the 4 tournament sizes. Inside the nested for loop we will find store the
one with the highest fitness and that will be the winner of the tournament. The winner will then be added to a list that will store all the winners and that
will be returned back to main. 

survivorSelection.py
The survivor selection method that is being implmented is generational replacment. What that does is it will first record the length of the offspring and 
then replace the worst fitness's in the population with the offspring. It does this for the worst to length of offspring, which means that the population
size will not change.
