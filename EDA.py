import io
import pandas as pd
import re
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
from PIL import Image

# analyze_data?

def read_csv_file(file_path):
    with open(file_path, 'rb') as file:
        df = pd.read_csv(io.BytesIO(file.read()))
    return df

def calculate_numeric_columns(data_frame):
    global numeric_columns
    numeric_columns = data_frame.select_dtypes(include=['float', 'integer'])

file_path = 'human_resources.csv'
df = read_csv_file(file_path)
calculate_numeric_columns(df)

def get_overall_info():
    print("DataFrame Information:")
    df.info()
    print("\nDataFrame Shape:")
    print(df.shape)
    print("\nDataFrame Head:")
    print(df.head())
    print("\nDataFrame Tail:")
    print(df.tail())
    print("\nDataFrame Description:")
    print(df.describe())

def calculate_mean():
    mean_values = numeric_columns.mean()
    return mean_values

def calculate_median():
    median_values = numeric_columns.median()
    return median_values

def calculate_mode():
    mode_values = df.mode().iloc[0]
    return mode_values

def calculate_range():
    data_range = numeric_columns.max() - numeric_columns.min()
    return data_range

def calculate_variance():
    variance_values = numeric_columns.var()
    return variance_values

def calculate_standard_deviation():
    std_values = numeric_columns.std()
    return std_values

def calculate_quartiles():
    quartiles = numeric_columns.quantile([0, 0.25, 0.5, 0.75, 1])
    return quartiles

def check_outliers():
    q1, q3 = numeric_columns.quantile(0.25), numeric_columns.quantile(0.75)
    iqr = q3 - q1
    lower_limit = q1 - 1.5 * iqr
    upper_limit = q3 + 1.5 * iqr
    outliers = {
        'lower_limit': lower_limit,
        'upper_limit': upper_limit,
        'outliers_count': ((numeric_columns < lower_limit) | (numeric_columns > upper_limit)).sum()
    }
    return outliers

def calculate_skewness():
    skewness_values = numeric_columns.apply(stats.skew)
    return skewness_values

def calculate_kurtosis():
    kurtosis_values = numeric_columns.apply(stats.kurtosis)
    return kurtosis_values

def visualize_skewness(column_name):
    plt.figure(figsize=(8, 6))
    sns.histplot(df[column_name], kde=True)
    plt.title('Skewness - Distribution of ' + column_name)
    plt.xlabel(column_name)
    plt.ylabel('Count')
    plt.show()

def visualize_kurtosis(column_name):
    plt.figure(figsize=(8, 6))
    sns.histplot(df[column_name], kde=True)
    plt.title('Kurtosis - Distribution of ' + column_name)
    plt.xlabel(column_name)
    plt.ylabel('Count')
    plt.show()

def frequency_word_cloud():
    text = open(file_path, 'r').read()
    word_counter = Counter(text.split())
    # Determine the maximum and minimum frequencies
    max_frequency = max(word_counter.values())
    min_frequency = min(word_counter.values())
    wordcloud = WordCloud(
        width=800,
        height=600,
        min_font_size=10,
        max_font_size=100,
        relative_scaling=0.5  # Adjust this value to control the size variation
    ).generate_from_frequencies(word_counter)
    plt.figure(figsize=(8, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud')
    image_buffer = io.BytesIO()
    plt.savefig(image_buffer, format='png')
    plt.close()
    image_buffer.seek(0)
    word_cloud_image = Image.open(image_buffer)
    word_cloud_image.show()

def generate_word_cloud():
    text = open(file_path, 'r').read()
    wordcloud = WordCloud().generate(text)
    plt.figure(figsize=(8, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud')
    image_buffer = io.BytesIO()
    plt.savefig(image_buffer, format='png')
    plt.close()
    image_buffer.seek(0)
    return image_buffer

def generate_pie_chart(column):
    category_counts = df[column].value_counts()
    plt.figure(figsize=(8, 6))
    plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%')
    plt.title(f'Distribution of {column.capitalize()}')
    plt.axis('equal')
    plt.legend()
    image_buffer = io.BytesIO()
    plt.savefig(image_buffer, format='png')
    plt.close()
    image_buffer.seek(0)
    return image_buffer

def cleanse_text(text):
    cleansed_text = re.sub(r'[^a-zA-Z0-9]', ' ', text)
    result = {'cleansed_text': cleansed_text}
    return result

def cleanse_text_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    cleansed_text = re.sub(r'[^a-zA-Z0-9]', ' ', text)
    result = {'cleansed_text': cleansed_text}
    return result

def reverse_text(text):
    reversed_text = text[::-1]
    result = {'reversed_text': reversed_text}
    return result

def count_words(text):
    word_count = len(text.split())
    result = {'word_count':word_count}
    return result

def add_column():
    column_name = input("Enter the name of the new column: ")
    if column_name in df.columns:
        print(f"Column '{column_name}' already exists. Please choose a different name.")
        return
    num_rows = int(input(f"How many rows do you want to edit (0-{len(df)}): "))
    if num_rows < 0 or num_rows > len(df):
        print("Invalid number of rows. Please try again.")
        return
    values = input(f"Enter the values for the new column for the first {num_rows} rows (comma-separated): ").split(',')
    if len(values) == 0:
        print("No values provided. The new column will contain NaN values.")
        df[column_name] = None
    else:
        if len(values) < num_rows:
            print("Insufficient number of values provided. The new column will contain NaN values for the remaining rows.")
            values.extend([None] * (num_rows - len(values)))
        elif len(values) > num_rows:
            print("Too many values provided. Only the first", num_rows, "values will be used.")
        df.loc[:num_rows-1, column_name] = values[:num_rows]
    df.to_csv(file_path, index=False)  
    print(f"New column '{column_name}' added to the DataFrame and the CSV file has been updated.")

def delete_column(column_name):
    if column_name not in df.columns:
        print("Column not found. Please try again.")
        return
    df.drop(column_name, axis=1, inplace=True)
    df.to_csv(file_path, index=False) 
    print(f"Column '{column_name}' has been deleted from the DataFrame and the CSV file has been updated.")

def check_missing_values():
    missing_values = df.isnull().sum()
    missing_positions = {}
    for column in missing_values.index:
        indices = df[df[column].isnull()].index.tolist()
        if indices:
            missing_positions[column] = indices
    return missing_positions

def handle_duplicates():
    duplicate_columns = df.columns[df.columns.duplicated()]
    if duplicate_columns.empty:
        print("No duplicate columns found.")
        return
    print("Duplicate Columns:")
    for column in duplicate_columns:
        duplicate_indices = df.columns.get_duplicates()[column]
        print(f"Column '{column}' is duplicated at indices: {duplicate_indices}")

def visualize_histogram(column_name):
    if column_name not in df.columns:
        print(f"Error: Column '{column_name}' does not exist in the DataFrame.")
        return
    plt.figure(figsize=(8, 6))
    sns.histplot(df[column_name], kde=True)
    plt.title('Histogram with Smooth Line - ' + column_name)
    plt.xlabel(column_name)
    plt.ylabel('Count')
    plt.show()

def correlation_analysis():
    correlation_matrix = numeric_columns.corr()
    print("Correlation Matrix:")
    print(correlation_matrix)

def scatterplot(column1, column2):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x=column1, y=column2)
    plt.title('Scatterplot')
    plt.show()

def heatmap_visualization():
    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_columns.corr(), annot=True, cmap='coolwarm')
    plt.title('Heatmap Visualization')
    plt.show()

def boxplot_visualization(column_name):
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, x=column_name)
    plt.title('Boxplot Visualization - ' + column_name)
    plt.xlabel(column_name)
    plt.show()

def countplot_visualization(column_name):
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x=column_name)
    plt.title('Countplot Visualization - ' + column_name)
    plt.xlabel(column_name)
    plt.ylabel('Count')
    plt.show()

menu = """
Please choose an option:

• Text-related functions:
    1. Cleanse text
    2. Cleanse text from file
    3. Reverse text
    4. Count words

• Statistical calculations:
    5. Calculate mean
    6. Calculate median
    7. Calculate mode
    8. Calculate range
    9. Calculate variance
    10. Calculate standard deviation
    11. Calculate quartiles
    12. Check outliers
    13. Calculate skewness
    14. Calculate kurtosis

• Data visualization:
    15. Visualize skewness
    16. Visualize kurtosis
    17. Frequency wordcloud
    18. Generate wordcloud
    19. Generate pie chart
    20. Visualize column
    21. Scatterplot
    22. Heatmap
    23. Boxplot
    24. Countplot

• Data manipulation:
    25. Add column
    26. Delete column
    27. Check missing values
    28. Handle duplicate columns
    29. Correlation analysis

30. Get overall information
0. Exit
"""

while True:
    print(menu)
    choice = input("Enter your choice (0-30): ")
    if choice == "1":
        text = input("Enter the text to cleanse: ")
        result = cleanse_text(text)
        print("Cleansed text:")
        print(result['cleansed_text'])
    elif choice == "2":
        file_path = input("Enter the file path of the text file to cleanse: ")
        result = cleanse_text_file(file_path)
        print("Cleansed text:")
        print(result['cleansed_text'])
    elif choice == "3":
        reversetext = input("Enter the text to reverse: ")
        result = reverse_text(reversetext)
        print("Reversed text: ")
        print(result['reversed_text'])
    elif choice == "4":
        counttext = input("Enter text to count words: ")
        result = count_words(counttext)
        print("Total words: ")
        print(result['word_count'])
    elif choice == "5":
        mean_values = calculate_mean()
        print("Mean values are:")
        print(mean_values)
    elif choice == "6":
        median_values = calculate_median()
        print("Median values are:")
        print(median_values)
    elif choice == "7":
        mode_values = calculate_mode()
        print("Mode values are:")
        print(mode_values)
    elif choice == "8":
        data_range = calculate_range()
        print("The range of the data is:")
        print(data_range)
    elif choice == "9":
        variance_values = calculate_variance()
        print("Variance values are:")
        print(variance_values)
    elif choice == "10":
        std_values = calculate_standard_deviation()
        print("Standard deviation values are:")
        print(std_values)
    elif choice == "11":
        quartiles = calculate_quartiles()
        print("Quartiles are:")
        print(quartiles)
    elif choice == "12":
        outliers = check_outliers()
        print("Outliers:")
        print(outliers)
    elif choice == "13":
        skewness_values = calculate_skewness()
        print("Skewness values are:")
        print(skewness_values)
    elif choice == "14":
        kurtosis_values = calculate_kurtosis()
        print("Kurtosis values are:")
        print(kurtosis_values)
    elif choice == "15":
        column_name = input("Enter the column name to visualize skewness: ")
        visualize_skewness(column_name)
    elif choice == "16":
        column_name = input("Enter the column name to visualize kurtosis: ")
        visualize_kurtosis(column_name)
    elif choice == "17":
        frequency_word_cloud()
        print("Word cloud generated and displayed.")
    elif choice == "18":
        image_buffer = generate_word_cloud()
        word_cloud_image = Image.open(image_buffer)
        word_cloud_image.show()
        print("Word cloud generated and displayed.")
    elif choice == "19":
        column_name = input("Enter the column name for the pie chart: ")
        image_buffer = generate_pie_chart(column_name)
        pie_chart_image = Image.open(image_buffer)
        pie_chart_image.show()
        print("Pie chart generated and displayed.")
    elif choice == "20":
        column_name = input("Enter the column name to visualize with histogram and smooth line: ")
        visualize_histogram(column_name)
    elif choice == "21":
        column1 = input("Enter the name of the first column for scatterplot: ")
        column2 = input("Enter the name of the second column for scatterplot: ")
        scatterplot(column1, column2)
    elif choice == "22":
        heatmap_visualization()
    elif choice == "23":
        column_name = input("Enter the name of the column for boxplot visualization: ")
        boxplot_visualization(column_name)
    elif choice == "24":
        column_name = input("Enter the name of the column for countplot visualization: ")
        countplot_visualization(column_name)
    elif choice == "25":
        add_column()
    elif choice == "26":
        column_name = input("Enter the name of the column to delete: ")
        delete_column(column_name)
    elif choice == "27":
        missing_positions = check_missing_values()
        print("Missing Values:")
        for column, positions in missing_positions.items():
            for position in positions:
                print(f"Missing value at row {position} at column {column}")
    elif choice == "28":
        handle_duplicates()
    elif choice == "29":
        correlation_analysis()
    elif choice == "30":
        get_overall_info()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")