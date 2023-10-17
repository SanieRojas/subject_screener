
"""Functions to setup the instance of a google news search engine, define its period time frame, 
retrive the results and store them in a file."""

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
    Performs a search of "period" days of news for any selected subject theme and, 
    if prompted, saves it into a database. 

    :monitor: Yes if you want to keep your results. 
    :type: Boolean
    
    :category: Category of search subject
    :type: String

    :subject: Subject of interest
    :rtype: String

    :return: Newsfeed dataframe
    :rtype: pandas dataframe  
    """
    # Quick off search
    api.get_news(subject)
    results = api.results(sort=True)
    newsfeed = pd.DataFrame(results)
    newsfeed = newsfeed.sort_values(by=["datetime"], ascending=False)

    if monitor == "yes":
        file_name = 'news_data.csv'
        newsfeed.to_csv(file_name, index=False)
        print("Corpus succesfully saved to file.")
    else:
        pass

    # If the function returns a value, use the "return" statement
    return newsfeed


if __name__ == "__main__":
    step1 = setup_engine("1d")
    step2 = setup_subject(step1, "Apple", "no")