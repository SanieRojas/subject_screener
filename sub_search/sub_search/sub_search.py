
"""Functions to setup the instance of a google news search engine, define its period time frame, 
retrive the results and store them in a file."""
from datetime import datetime
from GoogleNews import GoogleNews
import pandas as pd


def setup_engine(period):
    """
    Set up the google engine to retrieve news of a given period. 
    Documentation -> https://pypi.org/project/GoogleNews/

    :period: defines how much time to search news for. 
    :type: 7d [quantity of days + "d"] 

    :return: instance of a search engine
    """
    # Quick off instance
    api = GoogleNews()
    api.set_lang("en")
    api.set_encode("utf-8")
    api.set_period(period)

    return api

def setup_subject(api, subject, monitor):
    """
    Performs a search of news for any selected subject theme and, 
    if prompted, saves it into a database. Inherits the period stablished in the setup_engine function.

    :monitor: Yes if you want to keep your results. 
    :type: Boolean

    :subject: Subject of interest
    :rtype: String

    :return: Newsfeed dataframe
    :rtype: pandas dataframe  
    """
    # Setup log records
    log_text = str(datetime.now().timestamp())[:10]
    log2 = datetime.now().timestamp()
    log_date = datetime.fromtimestamp(log2)
    #Set up api to retrieve news results
    api.get_news(subject)
    results = api.results(sort=True)
    #Save to dataframe and file
    newsfeed = pd.DataFrame(results)
    newsfeed[log_date] = log_date
    newsfeed = newsfeed.sort_values(by=["datetime"], ascending=False)

    if monitor == "yes":
        file_name = f'./file_store_search/news_data_{subject}_{log_text}.csv'
        newsfeed.to_csv(file_name, index=False)
        print("Corpus succesfully saved to file ->  ", file_name, "on", log_date)
    else:
        pass

    # Returns a pandas dataframe with the newsfeed gathered and the log_date
    return newsfeed, log_date


if __name__ == "__main__":
    step1 = setup_engine("1d")
    user_input_subject = input("Please, indicate what subject would you like to explore.")
    user_input_keep = input("Indicate (yes/no) if you want to keep this subject for monitoring.")
    step2 = setup_subject(step1, user_input_subject, user_input_keep)
    print("Subject retrieved.")
    print("Amount of records retrieved -> ", len(step2))
    