import joblib
from pathlib import Path
from django.shortcuts import render
from .models import Prediction   # <-- import your model

# Locate model file relative to this file
MODEL_PATH = Path(__file__).resolve().parent / "house_price_model.pkl"

# Load or train model if missing
if MODEL_PATH.exists():
    model = joblib.load(MODEL_PATH)
else:
    # Train a simple model and save it
    try:
        import pandas as pd
        from sklearn.linear_model import LinearRegression
    except Exception:
        raise
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
    joblib.dump(model, MODEL_PATH)
    print(f"Model trained and saved at {MODEL_PATH}")

def predict_price(request):
    if request.method == "POST":
        area = float(request.POST['area'])
        bedrooms = int(request.POST['bedrooms'])
        bathrooms = int(request.POST['bathrooms'])
        age = int(request.POST['age'])

        prediction = model.predict([[area, bedrooms, bathrooms, age]])[0]

        # Save to DB
        Prediction.objects.create(
            area=area,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            age=age,
            price=prediction
        )

        return render(request, "predictor/result.html", {"price": prediction})
    return render(request, "predictor/form.html")
