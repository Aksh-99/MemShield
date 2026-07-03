#Import the dependencies
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
import seaborn as sns
import pickle
import matplotlib.pyplot as plt
#Load the data
df = pd.read_csv('Obfuscated-MalMem2022.csv')

#EDA
print(df.shape)
print(df.head())
print(df.isnull().sum().sum())   # how many missing values
print(df['Category'].value_counts())  # class distribution
print(df.dtypes.value_counts())  # what types of columns
print(df.columns.tolist())

#Label Data
X = df.drop(['Category','Class'], axis=1).values
Y = (df['Category'] != 'Benign').astype(int).values  # 1=malware, 0=benign

#Training and Testing Data
X_train, X_test, Y_train, Y_test= train_test_split(X,Y,test_size=0.1,stratify=Y,random_state=1)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
print(X.shape,X_train.shape,X_test.shape)

# Model training (using Logistic Regression)
model = LogisticRegression(max_iter=10000, solver='saga')
model.fit(X_train,Y_train)

# Model Evaluation
X_train_pred=model.predict(X_train)
train_accuracy=accuracy_score(X_train_pred,Y_train)
print("Training Accuracy :", train_accuracy)

X_test_pred=model.predict(X_test)
test_accuracy=accuracy_score(X_test_pred,Y_test)
print("Testing Accuracy :", test_accuracy)

#Predicting System by input data
input_data=X_test[0]
input_data_np=np.asarray(input_data)
input_data_reshape=input_data_np.reshape(1,-1)
predict_data=model.predict(input_data_reshape)
print("Is it Malware or not?",predict_data)

#Confusion matrix
Y_pred = model.predict(X_test)
cf_matrix = confusion_matrix(Y_test, Y_pred)
print("Confusion Matrix:\n",cf_matrix)
sns.heatmap(
    cf_matrix,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=['Benign', 'Malware'],
    yticklabels=['Benign', 'Malware']
)
plt.savefig('confusion_matrix.png', bbox_inches='tight')

#Save the model
with open('memshield_model.pkl', 'wb') as f:
    pickle.dump({'model': model, 'scaler': scaler}, f)

print("Model saved!")