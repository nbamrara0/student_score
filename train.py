import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
   
data = pd.read_csv("student_dummy_data_200.csv")
   

X = data[["hours_studied", "attendance", "previous_score"]]
y = data["final_score"]

X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("R² Score:", r2_score(y_test, predictions))
mae = mean_absolute_error(y_test, predictions)
print("MAE:", mae)
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

print("Correlation Matrix:")
print(data.corr())
pickle.dump(model, open("student_score_model.pkl", "wb"))

print("Model trained successfully!")
  
