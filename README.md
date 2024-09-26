## Used-Cars-EDA-and-business-questions

# 🎯Project Overview
  - Craigslist is one of the largest platforms for used vehicle sales in the United States.
  -  This project aims to analyze a dataset scraped from Craigslist to extract valuable insights regarding the used car market, which can be beneficial for buyers, sellers, and car dealers.

  - The dataset includes detailed information such as price, condition, manufacturer, model, year, and more.
  - This project focuses on cleaning, analyzing, and answering key business questions using this data.

# 📊Dataset Information
  - The dataset was sourced from Kaggle and contains a comprehensive list of used vehicle entries from Craigslist across the United States.
  -  The main columns include:
     - id: Unique identifier for each listing
     - url: URL of the Craigslist listing
     - region: Region of the vehicle listing
     - price: Listed price of the vehicle
     - year: Year of manufacture
     - manufacturer: Car manufacturer
     - model: Car model
     - condition: Condition of the car (e.g., new, like new, good, fair, etc.)
     - cylinders: Number of engine cylinders
     - size: Size category of the vehicle
     - type: Type of vehicle (e.g., SUV, sedan, truck, etc.)
     - paint_color: Color of the car
     - state: The state where the car is listed
     - lat/long: Latitude and longitude of the listing location
     - posting_date: The date the listing was posted
       
# 📈Project Goals
  - Data Extraction: Download and extract the data from Kaggle.
  - Data Cleaning: Identify and resolve data quality issues.
  - Data Analysis: Answer business questions using data analysis techniques.
  - Visualization: Provide clear visualizations to illustrate the findings.
    
# 🧰Technologies Used
  - Programming Language: Python
  - Libraries: Pandas, NumPy, Matplotlib, Seaborn, Plotly
  - Jupyter Notebook: For documentation and step-by-step analysis
    
# 📂Project Structure
  - The project is organized as follows:
     - Craigslist-Used-Vehicles-Analysis
       
       ├── data
       
       ├── notebooks
        
       └── README.md
    
# ⚙️Data Cleaning Process
  - The following steps were taken to clean the dataset:
    - Handling Missing Values: Missing values were filled or removed as appropriate.
    - Converting Data Types: Ensured all columns had consistent data types.
    - Removing Duplicates: Removed any duplicate listings.
    - Standardizing Categorical Values: Cleaned and standardized text entries (e.g., manufacturer names, car conditions).
    - Business Questions and Insights
 - Here are the key business questions addressed in this analysis:
    - What are the most popular type?
    - What is the distribution of the number of cars according to title status?
    - What is the most common condition for cars?
    - What is the distribution of data over time?
    - What is the relationship between distance traveled and price?
    - How do prices compare between fuel types?

# 🤖Results and Visualizations
  - Example Visualization: The average price of vehicles by manufacturer showed that luxury brands generally have higher prices, while more common brands like Toyota and Ford are more affordable.
  - Finding: Vehicles in good condition have a higher average price, as expected, while "fair" condition cars are the most affordable.
  - All findings are documented .
    
# 🧑‍🔧Future Work
  - Enhance the dataset by adding external data sources, such as car valuation data.
  - Build predictive models to forecast car prices based on features like age, condition, and mileage.
  - Create an interactive dashboard using tools like Power BI or Tableau.
    
# 🤝Contributing
  - Contributions are welcome! If you'd like to contribute, please fork the repository and create a pull request.

# 💻 Authors
  - Abdul Rahman Ahmed 

  - abdulrahmannassar202@gmail.com

# 📌 Project link
  - https://github.com/Abdulrahman181/Used-Cars-EDA-and-business-questions




