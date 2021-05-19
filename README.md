# MarksEntryAndTabulationSystem
This is a Django Based Entry system which inputs the marks of students and automatically calculates the Total and Percentage and then makes a leaderboard of all the students which is initially sorted A/c to Percentages by can be sorted as desired by buttons given and also searching facility is provided too.

<hr>
 
To keep it simple I had not added the concepts of login and registration. 

Concepts of Databases and Filtering and performing other operations on it is maintained.

# Frontend:
## Homepage having 2 choices:
- Enter marks
- View Leaderboard
### Enter marks page:
- Following inputs should be taken from the frontend:
- Roll No
- Name
- Marks in Maths (out of 100)
- Marks in Physics (out of 100)
- Marks in Chemistry (out of 100)
- Total (Automatically calculated)
- Percentage (Automatically calculated)
#### Basic validation on the input fields is also present.
### View Leaderboard Page
- Grid to display the rankings of the students based on percentage by default
- Having sorting and searching functionality.

# Backend:
- Python (Django), POST marks and GET results for theleaderboard.
- SQLLite Datastore for storing marks

# DEPLOYED (Heroku)
