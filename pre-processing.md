**Overall Sequence of Steps**

1.  **Data Loading**
    
    We begin by importing the necessary libraries for data manipulation and analysis. 
We then load the match details dataset from a CSV file into a DataFrame for processing. 
Then we inspect and verify the structure of the dataset to ensure all required information is present and correctly loaded.
    
2.  **Data Preparation**
    
    We define comprehensive lists of team name variations to account for different representations in the data (e.g., "Manchester United", "Man United"). 
Then we create a mapping dictionary that associates each variation with a standardized team label (e.g., "Team_1", "Team_2").
    
3.  **Data Masking**
    
    - We apply masking to replace team names 
in the 'Home', 'Away', 'events', and 'summary' columns with the standardized team labels. 
This standardization ensures consistency and aids in anonymizing the data. 
We reckon this will help us be more objective and reduce bias towards certain teams.
    - Then we check and verify that the masked text for any unmasked team names to ensure that all instances have been successfully replaced. 
We display and review any rows where masking failed to correct issues in the mapping or masking function.
    
4.  **Feature Engineering**
    
    We define keyword lists that indicate high-stakes matches (e.g., "title race", "relegation battle") and exciting matches (e.g., "red card", "penalty"). 
We create a labeling function that scans the masked text for these keywords and assigns appropriate labels based on their presence.
This is so that we can introduce the concept of 'classification' and help us differentiate. Using online sources and our own football knowledge, we label games that are interesting.
    
5.  **Data Labeling**
    
    We apply the labeling function to categorize each match into labels such as "High Stakes", "Exciting", "High Stakes & Exciting", or "Normal". We add these labels as a new column in the DataFrame.
    
6.  **Data Visualization**
    
    We generate visualizations to understand the distribution of match labels. This is explorational and to help us understand/balance the dataset better.
    
7.  **Data Exporting**
 
    We prepare the data for export by selecting relevant columns, including masked team names, match details, masked text, and assigned labels. 
We then save the processed DataFrame to a TSV file.
