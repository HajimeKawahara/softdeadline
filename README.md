# softdeadline
soft deadline function for class reports.


```python3
    import datetime
    from softdeadline.deadline_function import gauss_deadline 

    deadline = datetime.datetime(2022, 7, 17, 23, 59, 59)
    submission_datetime = datetime.datetime(2022, 7, 18, 03, 12) 
    val = gauss_deadline(deadline, submission_datetime = submission_datetime)

    raw_expectation_score = 90.0
    print("predicted score = ",val*raw_expectation_score)
    # predicted score =  86.8556844299459
```