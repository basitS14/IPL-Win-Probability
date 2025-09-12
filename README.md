## IPL Data Analysis and Model Building

Developed a machine learning model to predict real-time win probabilities for IPL matches. To achieve this, I conducted an in-depth analysis of 13 seasons of IPL data (2008-2020) to uncover key performance indicators. These insights were then used to engineer novel features, significantly enhancing the model's predictive accuracy. Acheived 81% accuracy on test set.

### Quick Links
- Check out the Streamlit dashboard [here.](https://ipl-win-prediction-probalities.streamlit.app/)
- Checkout the full analysis [here.](notebooks/IPL_analysis.ipynb)


### Approach
- Collected the IPL dataset from 2008 to 2020 from Kaggle.
- Analysed the dataset to understand the patterns and reveal some insights about players, teams and match events.
- Performed feature engineering to create new features that were needed to achieve out object.
- Selected logistic regression to train our model because our objective was to predict probabilities, and in a certain way, the dataset is linear; these condition suits Logistic regression.

### Project Structure

* `IPL_analysis.ipynb`: This notebook focuses on exploratory data analysis (EDA), data cleaning, and feature engineering of the IPL datasets.
* `Model_Building.ipynb`: This notebook utilizes the processed data from `IPL_analysis.ipynb` to build and save a machine learning model.
* `app.py`: contains streamlit code.

### Setup and Usage

To run these notebooks, ensure you have Jupyter Notebook or JupyterLab installed.

1.  **Clone the repository** (if applicable).
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Place data files**: Ensure `IPL Ball-by-Ball 2008-2020.csv` and `IPL Matches 2008-2020.csv` are in the `../datasets/` directory relative to the notebooks, or update the file paths in `IPL_analysis.ipynb` accordingly.
4.  **Run `IPL_analysis.ipynb`**: Execute all cells to perform data analysis and generate the intermediate CSV files (`ball_to_ball_data.csv` and `match_to_match_data.csv`).
5.  **Run `Model_Building.ipynb`**: Execute all cells to train and save the predictive model (`pipe.pkl`).


![Screenshot (884)](https://github.com/user-attachments/assets/d24eec8c-8b5d-46ab-b1fd-c3edbcd27a09)

![Screenshot (885)](https://github.com/user-attachments/assets/5fba7a31-abd2-451f-9c1a-76db103182d7)
