#  Student Score Predictor

A Machine Learning web application that predicts a student's exam score based on study hours, attendance percentage, and previous scores.

##  Features

- Predict student exam scores using Machine Learning
- User-friendly Flask web interface
- Trained using Linear Regression
- Stores prediction history in SQLite database
- Responsive and simple UI

## Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- SQLite
- HTML/CSS

## Dataset Features

The model uses the following inputs:

- Study Hours
- Attendance Percentage
- Previous Score

### Example Input

| Study Hours | Attendance | Previous Score |
|------------|------------|---------------|
| 5 | 85 | 78 |

### Example Output

```text
Predicted Score: 82.4
```

##  Project Structure

```text
student-score-predictor/
│
├── app.py
├── train.py
├── student_dummy_data_200.csv
├── requirements.txt
├── templates/
│   └── index.html
├── .gitignore
└── README.md
```

## Installation

### 1. Clone Repository

```bash
git clone <your-repository-url>
cd student-score-predictor
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Train Model

```bash
python train.py
```

### 6. Run Flask Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

##  Machine Learning Model

This project uses:

- Linear Regression
- Train/Test Split
- Model Serialization with Pickle

### Evaluation Metrics

- Mean Absolute Error (MAE)
- R² Score


##  Future Improvements

- Multiple ML algorithms comparison
- User authentication
- Prediction history dashboard
- Data visualization charts
- Deployment on Render or Railway
- Export predictions to CSV

##  Author

**Naveen Bamrara**
linkedin:-
https://www.linkedin.com/in/naveen-bamrara-857414260/
Python Developer | Flask Developer | Machine Learning Enthusiast





---

 If you like this project, give it a star on GitHub!
