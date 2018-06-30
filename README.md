# UpgradWC2018


# About code

Please change the index18 and result18 file location as per your requirement. Means give proper location of the files.
f=pd.read_csv('C:/Users/ASUS/Desktop/upgrad/2018wc/result18.csv',',',)
and
v=pd.read_csv('C:/Users/ASUS/Desktop/upgrad/2018wc/index18.csv',',')

# Data selection

We use two data tables.
1st:-FIFA ranking of all Teams with there points as per FIFA. 
Link:-
https://www.fifa.com/fifa-world-ranking/ranking-table/men/index.html
Excel file name:-Index18
2nd :-All national football match results of last 4 years including fifawc18 group stage results
Link:-
https://www.kaggle.com/martj42/international-football-results-from-1872-to-2017/version/32#_=_
and
https://www.eurosport.com/football/world-cup/2018/world-cup-2018-final-group-standings-results-and-last-16-draw-fixtures_sto6815861/story.shtml

Also knockout match table
link:- https://www.google.com/search?q=worldcup+2018+results&rlz=1C1GIGM_enIN793IN793&oq=worldcup+2018+results&aqs=chrome..69i57j0l5.19283j1j4&sourceid=chrome&ie=UTF-8#sie=lg;/m/06qjc4;2;/m/030q7;mt;fp;1


# Data cleaning process: -

In case of index18 file
1st  convert the data in excel format by below link
https://convertio.co/document-converter/
after that clean the data using replace, find, Remove duplicate data, Text to columns, filter etc.
For changing the point range of every teams, Point divided by 1000.
After that change this excel file to csv file.

In case of result18 file
Filter and select last 4 years of data.
Add world cup 2018 data into it. Find the winning team, loser team or TIE by goals. Add this data in new columns.




# Visualizations and Modelling

We visualize the data in from of numbers. In Excel if Team1 Goals are greater than  Team2 Goals Team1 is winning team if equal then TIE or if less team2 is winner. In Python we calculate a point for every teams which teams point is greater that teams wins against other team. 
 	We use panda and numpy in Python. At first create a list of all countries playing in fifa worldcup 2018,grouping  by team1 and team2 for getting total number of goal givens by a team. From that we evaluate the total goal diff as (gd).
	 Now create a for loop calling every team as a item one by one for calcutating there points. If  any team is winning any match against another team we give him points basis of the loser teams ranking and point in index18 chart.Index18 is taken from fifa ranking given by FIFA. IF any team wins against a top-ranking team we give him more points as per the index18 chart. Same logic for draw. For losing a game by a team we decide a parameter basis of winning team, If losing against a team which is in top losing parameter(lp) is less. We have added all winning ,TIE and losing points as p,dm and lp.
# Example:-
Spain wins against Belgium (point- 1.298) and Egypt(point- 0.649)
p=1.298+ 0.649  		{in code formula is p=p+(h[j][2]))
Spain TIE against Belgium (point- 1.298) and Sweden (point- 0.88)
  dm=1.298+0.88                              {in code formula is dm=dm+h[j][2]}
Spain lose against France (point- 1.198) and Sweden (point- 0.88)
Lp=1.5 - 1.198+ 1.5- 0.88           
{1.5 taken as a range as Germany  is in top in rank and his point is almost equle to 1.5
In code formula is lp=lp+1.5-(h[j][2])}

In the end we calculate total points for wining,TIE and losing. We multiply 6 for winning ,2 for TIE , 1 for loss and divided 10 from goal difference. Also divided the total point by total number of matches played by that team for get  a avg.

# Code for point calculation:-
    Point[i1]= round(((dm*2+p*6-lp+(gd/10))/len(play)),2 )
Save this data as a dictionary format.
Now we have all 32 teams along with there points in Point_new   dictionary.We sort the teams by there points.

OrderedDict([('SaudiArabia', 0.55), ('Panama', 0.86), ('Tunisia', 1.07), ('Egypt', 1.17), ('Nigeria', 1.2), ('CostaRica', 1.24), ('SouthKorea', 1.26), ('Iceland', 1.3), ('Serbia', 1.3), ('Morocco', 1.32), ('Australia', 1.33), ('Russia', 1.33), ('Japan', 1.45), ('Senegal', 1.66), ('Iran', 1.77), ('Sweden', 1.88), ('Switzerland', 2.27), ('Denmark', 2.29), ('Uruguay', 2.31), ('Poland', 2.31), ('Mexico', 2.38), ('Peru', 2.49), ('Croatia', 2.51), ('Colombia', 2.62), ('Germany', 2.73), ('Portugal', 2.79), ('England', 3.01), ('Argentina', 3.04), ('Belgium', 3.14), ('Spain', 3.23), ('France', 3.73), ('Brazil', 4.19)])
If point if higher winning chance is higher.
# Results:-
We already get round of 16 teams. Using for loop we compare each teams by there points and get the semi-finalist ,finalist and champion.
        Our Semi-finalist are 
 ['France', 'Brazil', 'Spain', 'England']
   Our finalist are 
   ['Brazil', 'Spain']
2018 worldcup champion is
              Brazil
![r](https://user-images.githubusercontent.com/38527656/42123237-34ca40a2-7c6c-11e8-89bd-db013944cb35.png)
	      
	      
# Code and Output: -
Please find the code from Project-report word file.

OUTPUT:-
runfile('C:/Users/ASUS/Desktop/upgradwc2018.py', wdir='C:/Users/ASUS/Desktop')
OrderedDict([('SaudiArabia', 0.55), ('Panama', 0.86), ('Tunisia', 1.07), ('Egypt', 1.17), ('Nigeria', 1.2), ('CostaRica', 1.24), ('SouthKorea', 1.26), ('Iceland', 1.3), ('Serbia', 1.3), ('Morocco', 1.32), ('Australia', 1.33), ('Russia', 1.33), ('Japan', 1.45), ('Senegal', 1.66), ('Iran', 1.77), ('Sweden', 1.88), ('Switzerland', 2.27), ('Denmark', 2.29), ('Uruguay', 2.31), ('Poland', 2.31), ('Mexico', 2.38), ('Peru', 2.49), ('Croatia', 2.51), ('Colombia', 2.62), ('Germany', 2.73), ('Portugal', 2.79), ('England', 3.01), ('Argentina', 3.04), ('Belgium', 3.14), ('Spain', 3.23), ('France', 3.73), ('Brazil', 4.19)])

 After round of 16 winning teams are:
 ['Portugal', 'France', 'Brazil', 'Belgium', 'Spain', 'Croatia', 'Switzerland', 'England']

 After round of 8 winning teams are:
 ['France', 'Brazil', 'Spain', 'England']


          Our Semi-finalist are 
 ['France', 'Brazil', 'Spain', 'England']


       Our finalist are 
     ['Brazil', 'Spain']

    2018 worldcup champion is
              Brazil
    
