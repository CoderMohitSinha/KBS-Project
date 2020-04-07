# Analysis of air quality 
1) Research question:  what is the group trying to learn or question to answer? Who is interested (audience)?

We are trying to learn how learn about the air quality across United states based on the historical date and determine the factors affecting it .This analysis can provide insight on which areas are affected most by air pollution and such analysis can help Environmental Protection Agency to take appropriate action to control the pollution.We are also trying to combine the analysis with respiratory disease data set to find how air pollution have effect on respiratory diseases 
Research 
1. https://www.airnow.gov/index.cfm?action=aqi_brochure.index
2. https://www.technicaljournalsonline.com/ijeat/VOL%20I/IJAET%20VOL%20I%20ISSUE%20II%20JULY%20SEPTEMBER%202010/Article%2011.pdf
3. https://www.annualreviews.org/doi/pdf/10.1146/annurev.pu.15.050194.000543 

2)  Domain and Data: 
Domain:Climate and Health care

Data source: Historical Air Quality
https://console.cloud.google.com/marketplace/details/epa/historical-air-quality?filter=solution-type:dataset&q=air&id=198c2178-3986-4182-a7c7-4c9ae81dfc5d

      a)  preprocessing that may be necessary (careful here)
      Most of the data is almost cleaned as it is almost clean as we are using data from google public datasets

      b)  size of data - data must be “big” data (millions of records)
            Its a Big data from google public datasets

      c)  tentative plan for analysis on GCP

           1)  EDA and Preprocessing
            we will check if we need any transformation or conversion of data and plot various graphs and plots to analyze the
            data.
           2)  Dashboard for User group, Dashboard for Data Engineers
               we will create a dashboard to visualize the outcome of our analysis
           User group:
           - Visualization to that displays events on a map with timeline slider.
           - Correlation matrices between event types and observation percentages in relation to time
           Data Engineers
           - Visualizations with additional attributes such as metrics and methods used in measuring air quality (helps make sure that               everything is consistent for user group)
           - Filtering tools for certification indicators (attribute used to validate accuracy of information)
           
           3)  GCP further processing - ML
             We will try to predict the  air quality based on the historic  

           4) plan for data ingest
           The data will be stored in gcp bucket and will be queried using BigQuery to get filtered dataset,
            
           Evaluation of results
             We will test the model with testing dataset and find the accuracy of the model using various error metrics like absolute mean error or root mean square eror . The lower error metric value, the better the model predicts the response
             
           5)  Steps for production model
           - build model  we will use pySpark to read and write data from and to BigQuery 
           - test model with cross validation
           - upload model to the cloud pipeline
           - optimize model if necessary
          
           6)  Final Dashboard for User Group
           - Visualization to that displays events on a map with timeline slider.
           - Correlation matrices between event types and observation percentages in relation to time
 

           The data will be stored in gcp bucket and will be queried using BigQuery to get filtered dataset,
