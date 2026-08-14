import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Dummy dataset
data = pd.DataFrame({
    "area": [1000, 1500, 2000, 2500],
    "bedrooms": [2, 3, 3, 4],
    "bathrooms": [1, 2, 2, 3],
    "age": [10, 5, 2, 1],
    "price": [100000, 150000, 200000, 250000]
})

X = data[['area','bedrooms','bathrooms','age']]
y = data['price']

model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "house_price_model.pkl")
print("✅ Model saved as house_price_model.pkl")
