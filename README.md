## IPL Data Analysis and Model Building

This repository contains a comprehensive analysis of IPL matches and ball-by-ball data from 2008 to 2020, followed by the development of a predictive model.

### Project Structure

* `IPL_analysis.ipynb`: This notebook focuses on exploratory data analysis (EDA), data cleaning, and feature engineering of the IPL datasets.
* `Model_Building.ipynb`: This notebook utilizes the processed data from `IPL_analysis.ipynb` to build and save a machine learning model.

### `IPL_analysis.ipynb` - IPL Data Analysis

This notebook performs the following key steps:

1.  **Data Loading**: Reads two primary datasets:
    * `IPL Ball-by-Ball 2008-2020.csv`
    * `IPL Matches 2008-2020.csv`
2.  **Initial Data Inspection**: Provides basic information, shape, and descriptive statistics for both datasets.
3.  **Data Cleaning and Preprocessing**:
    * Handles missing values, specifically for the 'method' column (e.g., D/L method) by filling `NaN` values with 'Regular'.
    * Corrects inconsistencies in team names (e.g., 'Rising Pune Supergiant' replaced with 'Rising Pune Supergiants').
    * Fills missing `result_margin` values for 'tie' matches with 0.
    * Drops rows with remaining null values, ensuring a clean dataset for analysis.
4.  **Exploratory Data Analysis (EDA)**:
    * Investigates the relationship between winning the toss and winning the match, calculating the percentage of times the toss winner also won the match.
5.  **Data Export**: Exports the cleaned and processed dataframes for further use:
    * `df_details` is saved as `ball_to_ball_data.csv`.
    * `df_match` is saved as `match_to_match_data.csv`.

### `Model_Building.ipynb` - Model Construction

This notebook is dedicated to building a predictive model using the refined data:

1.  **Data Import**: Loads the preprocessed data from `match_to_match_data.csv` and `ball_to_ball_data.csv`.
2.  **Feature Engineering and Preprocessing for Model**: Includes steps for preparing the data specifically for model training (e.g., handling categorical variables, creating new features relevant for prediction).
3.  **Model Training**: Trains a machine learning model using the prepared data.
4.  **Model Export**: Saves the trained model using `pickle` for future use and deployment.

### Libraries Used

The project extensively uses the following Python libraries:

* `pandas` for data manipulation and analysis
* `numpy` for numerical operations
* `datetime` for date and time handling
* `matplotlib.pyplot` for basic plotting
* `seaborn` for enhanced data visualizations
* `scipy.stats` for statistical functions
* `statistics` for statistical calculations
* `plotly` for interactive visualizations
* `pickle` for model serialization

### Setup and Usage

To run these notebooks, ensure you have Jupyter Notebook or JupyterLab installed.

1.  **Clone the repository** (if applicable).
2.  **Install dependencies**:
    ```bash
    pip install pandas numpy matplotlib seaborn scipy plotly
    ```
3.  **Place data files**: Ensure `IPL Ball-by-Ball 2008-2020.csv` and `IPL Matches 2008-2020.csv` are in the `../datasets/` directory relative to the notebooks, or update the file paths in `IPL_analysis.ipynb` accordingly.
4.  **Run `IPL_analysis.ipynb`**: Execute all cells to perform data analysis and generate the intermediate CSV files (`ball_to_ball_data.csv` and `match_to_match_data.csv`).
5.  **Run `Model_Building.ipynb`**: Execute all cells to train and save the predictive model (`pipe.pkl`).


![Screenshot (884)](https://github.com/user-attachments/assets/d24eec8c-8b5d-46ab-b1fd-c3edbcd27a09)

![Screenshot (885)](https://github.com/user-attachments/assets/5fba7a31-abd2-451f-9c1a-76db103182d7)
