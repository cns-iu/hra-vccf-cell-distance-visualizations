import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

# Load the dataset
data = pd.read_csv(r'G:\HuBMAP\Hickey\B004_training_dryad.csv')

# Select the necessary columns
features = data.iloc[:, 1:49]  # Features
labels = data['cell_type_A']  # Labels
regions = data['unique_region']

# Encode labels if they're not already numerical
label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(labels)

# Split the data based on the unique_region
train_data = features[regions.isin(['reg001_CL_B004', 'reg001_SB_B004', 'reg002_CL_B004', 'reg002_SB_B004', 'reg003_CL_B004', 'reg003_SB_B004'])]
train_labels = encoded_labels[regions.isin(['reg001_CL_B004', 'reg001_SB_B004', 'reg002_CL_B004', 'reg002_SB_B004', 'reg003_CL_B004', 'reg003_SB_B004'])]

val_data = features[regions.isin(['reg004_CL_B004', 'reg004_SB_B004'])]
val_labels = encoded_labels[regions.isin(['reg004_CL_B004', 'reg004_SB_B004'])]

# Initialize the Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, verbose=3, n_jobs=-1, random_state=42)

# Train the model
clf.fit(train_data, train_labels)

# Validate the model
val_predictions = clf.predict(val_data)

# Check accuracy
accuracy = accuracy_score(val_labels, val_predictions)
print(f"Validation Accuracy: {accuracy*100:.2f}%")

# If you want to explore feature importance
importances = clf.feature_importances_
sorted_indices = importances.argsort()[::-1]
print("Feature importance:")
for idx in sorted_indices:
    print(f"{features.columns[idx]}: {importances[idx]:.4f}")

# Print the classification report
print(classification_report(val_labels, val_predictions, target_names=label_encoder.classes_))
