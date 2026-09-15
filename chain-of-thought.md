At first glance what I did was to added the raw data set and the libraries I need.

I added my InvalidScoreError(Exception) to catch if the student has a score below 0 and above 100. If they have an invalid scores.
I also added StudentRecordLockedError(Exception)

I added my Score checker that checks if the score is less than 0 and above or equal to 101. If the scores are invalid they will be given an InvalidScore Error. There's a mistake somewhere in the code tho.

I added StudentRecordLockedError 

I added a Student class to instantiate student name and scores. I added __init__, __str__ to make a human readable output, __repr__ for checking