# Data Analytics Django Application

This Django application provides a set of APIs for performing various data analytics tasks on Excel files. It allows you to upload Excel files, convert them to CSV format, and perform operations like data analysis, data visualization, and more.

## Getting Started

To run this application, follow these steps:

1. Clone the repository to your local machine.

2. Install the required Python packages using `pip`:

   ```bash
   pip install django djangorestframework pandas plotly regex
   ```

3. Run migrations to create the database tables:

   ```bash
   python manage.py migrate
   ```

4. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

5. Access the API endpoints in your web browser or API client.

## API Endpoints

### 1. Upload Excel File

- **URL**: `/api/upload/`
- **HTTP Method**: POST
- **Description**: Upload an Excel file, which will be converted to CSV format and stored in the database.

### 2. List Excel Files

- **URL**: `/api/files/`
- **HTTP Method**: GET
- **Description**: Retrieve a list of all uploaded Excel files.

### 3. Get Columns of CSV File

- **URL**: `/api/columns/<int:pk>/`
- **HTTP Method**: GET
- **Description**: Retrieve the column names of the associated CSV file for a specific Excel file.

### 4. Data Analysis

- **URL**: `/api/analysis/<int:pk>`
- **HTTP Method**: GET
- **Parameters**:
  - `function` (string): The data analysis function to perform (e.g., 'avg', 'sum', 'min', 'max', 'mult').
  - `column_name` (string): The name of the column on which the analysis should be performed.
- **Description**: Perform data analysis operations like average, sum, min, max, or multiplication on a specific column of the associated CSV file.

### 5. Data Visualization

- **URL**: `/api/visualization/<int:pk>/`
- **HTTP Method**: GET
- **Parameters**:
  - `pattern` (string): A regular expression pattern for filtering data.
- **Description**: Generate a data visualization plot (line chart) for the income and expense columns of the associated CSV file.

### 6. Open Document

- **URL**: `/api/doc/<int:pk>/`
- **HTTP Method**: GET
- **Parameters**:
  - `function` (string): The document view function (not required).
  - `column_name` (string): The name of the column (not required).
- **Description**: View the document (first 15 records) of the associated CSV file or perform specific operations on the data, such as calculating the average, sum, min, max, or multiplication of a column.

## Folder Structure

- `excel_api`: Contains the Django application code, including models, views, and serializers.

## Dependencies

- Django: The web framework for building the application.
- Django Rest Framework: Provides tools for building RESTful APIs.
- pandas: Used for data manipulation and analysis.
- plotly: Used for data visualization.
- regex: Used for regular expression pattern matching.

## Usage

1. Upload an Excel file using the `/api/upload/` endpoint.
2. Use the other API endpoints to perform various data analytics operations on the uploaded Excel files.

## Authors

- StanDo

## License

This project is licensed under the [License Name] - see the [LICENSE.md](LICENSE.md) file for details.
