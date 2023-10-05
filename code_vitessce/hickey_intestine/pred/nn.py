import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn.metrics import classification_report

# Load your data
data = pd.read_csv(r'G:\HuBMAP\Hickey\B004_training_dryad.csv')

# Splitting the data into training and testing sets
train = data[(data['unique_region'] != 'reg004_CL_B004') & (data['unique_region'] != 'reg004_SB_B004')]
test = data[(data['unique_region'] == 'reg004_CL_B004') | (data['unique_region'] == 'reg004_SB_B004')]

# Feature columns
features = data.columns[1:49].tolist()

train_data = train[features].values
test_data = test[features].values

# Convert string labels to numbers
le = LabelEncoder()
train_labels = le.fit_transform(train['cell_type_A'])
test_labels = le.transform(test['cell_type_A'])

# Define the model
model = tf.keras.models.Sequential([
    tf.keras.layers.Input(shape=(48,)),  # Input layer
    tf.keras.layers.Dense(128, activation='relu'),  # Hidden layer with 128 units
    tf.keras.layers.Dropout(0.2),  # Dropout layer to reduce overfitting
    tf.keras.layers.Dense(21, activation='softmax')  # Output layer with 21 units (for 21 cell types)
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
history = model.fit(train_data, train_labels, epochs=10, validation_data=(test_data, test_labels), batch_size=32)

# Evaluate on the test set
loss, accuracy = model.evaluate(test_data, test_labels, verbose=2)
print("\nTest accuracy:", accuracy)

# report
predicted_probs = model.predict(test_data)
predicted_labels = predicted_probs.argmax(axis=-1)
print(classification_report(test_labels, predicted_labels, target_names=le.classes_))