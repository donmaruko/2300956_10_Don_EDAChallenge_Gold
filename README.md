# Data Analysis and Text Manipulation

This Python script provides various data analysis and text manipulation functions for CSV data. It includes statistical calculations, data visualization, data manipulation, and text-related operations. The script is designed to be interactive, allowing you to choose and execute specific functions based on your needs.

## Installation

1. Clone this repository to your local machine:

```shell
git clone https://github.com/donmaruko/Python-EDA-Toolkit.git)https://github.com/donmaruko/Python-EDA-Toolkit.git
```

2. Install the required Python packages by running the following command in your project directory:

```shell
pip install -r requirements.txt
```

## Usage

1. Make sure you have completed the installation steps.

2. Start the script by running the following command:

```shell
python EDA.py
```

3. Follow the on-screen menu to select and execute the desired operations.

## Usage of `customers.csv`

The Python script in this project uses a sample CSV file called `customers.csv` for data analysis and manipulation. This CSV file represents customer data with various columns, including `customer_id`, `age`, `gender`, `location`, `product_category`, `revenue`, and `satisfaction_level`.

The code reads data from this CSV file using the `read_csv_file` function and stores it in a Pandas DataFrame for analysis. You can replace this sample data with your own dataset in the same CSV format to perform data analysis and manipulation using the provided functions in the script.

Before running the script, ensure that you have the `customers.csv` file in the same directory as the script or provide the correct file path to the `read_csv_file` function in the script to load your dataset.

Feel free to customize and use your own dataset for analysis with the provided code.

## Features

### Text-Related Functions:

- `Cleanse text`: Remove non-alphanumeric characters from text.
- `Cleanse text from file`: Cleanse text from a file and display the result.
- `Reverse text`: Reverse the order of characters in text.
- `Count words`: Count the number of words in a text.

### Statistical Calculations:

- `Calculate mean`: Compute the mean values of numeric columns.
- `Calculate median`: Compute the median values of numeric columns.
- `Calculate mode`: Compute the mode values of all columns.
- `Calculate range`: Calculate the data range for numeric columns.
- `Calculate variance`: Compute the variance of numeric columns.
- `Calculate standard deviation`: Calculate the standard deviation of numeric columns.
- `Calculate quartiles`: Compute quartiles (0%, 25%, 50%, 75%, 100%) for numeric columns.
- `Check outliers`: Identify and count outliers in numeric columns.
- `Calculate skewness`: Compute skewness values for numeric columns.
- `Calculate kurtosis`: Compute kurtosis values for numeric columns.

### Data Visualization:

- `Visualize skewness`: Generate histograms with a smooth line for numeric columns.
- `Visualize kurtosis`: Visualize kurtosis with histograms.
- `Frequency word cloud`: Generate a word cloud based on word frequencies.
- `Generate word cloud`: Create a word cloud visualization for text data.
- `Generate pie chart`: Generate a pie chart for a specific column.
- `Visualize column`: Visualize a column using a histogram with a smooth line.
- `Scatterplot`: Create a scatterplot between two columns.
- `Heatmap`: Generate a heatmap for correlation analysis.
- `Boxplot`: Visualize data distribution using boxplots.
- `Countplot`: Create count plots for categorical columns.

### Data Manipulation:

- `Add column`: Add a new column to the DataFrame.
- `Delete column`: Delete a specific column from the DataFrame.
- `Check missing values`: Identify and display missing values in the DataFrame.
- `Handle duplicate columns`: Identify and handle duplicate columns.
- `Correlation analysis`: Perform correlation analysis on numeric columns.
