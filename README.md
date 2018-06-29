# UpgradWC2018


About code

Please change the index18 and result18 file location as per your requirement. Means give proper location of the files.
f=pd.read_csv('C:/Users/ASUS/Desktop/upgrad/2018wc/result18.csv',',',)
and
v=pd.read_csv('C:/Users/ASUS/Desktop/upgrad/2018wc/index18.csv',',')

Data selection

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


Data cleaning process: -

In case of index18 file
1st  convert the data in excel format by below link
https://convertio.co/document-converter/
after that clean the data using replace, find, Remove duplicate data, Text to columns, filter etc.
For changing the point range of every teams, Point divided by 1000.
After that change this excel file to csv file.

In case of result18 file
Filter and select last 4 years of data.
Add world cup 2018 data into it. Find the winning team, loser team or TIE by goals. Add this data in new columns.
