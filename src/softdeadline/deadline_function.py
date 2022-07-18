import datetime
import numpy as np

def gauss_deadline(deadline, timescale_hr=12, submission_datetime=None):
    """_summary_

    Args:
        deadline (datetime.datetime): deadline date
        timescale_hr (float, optional): decay timescale in hour. Defaults to 12.
        submission_datetime (datetime.datetime, optional): current date . Defaults to None.
        
    Returns:
        throughput of the score of the report.    
    
    """
    if submission_datetime is None:
        submission_datetime = datetime.datetime.now()

    if submission_datetime < deadline:
        return 1.0
    
    dt = (submission_datetime - deadline)
    dx = dt.seconds/(timescale_hr*3600.)
    return np.exp(-dx**2/2.0)


if __name__ == "__main__":
    
    deadline = datetime.datetime(2022, 7, 17, 23, 59, 59)
    submission_datetime = datetime.datetime(2022, 7, 18, 3, 12) 
    val = gauss_deadline(deadline, submission_datetime = submission_datetime)

    raw_expectation_score = 90.0
    print("predicted score = ",val*raw_expectation_score)
    