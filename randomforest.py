### Owner:      David Huang
### Model:      Random Forest
### Date:       2019-01-23

############################################################ CHANGE LOG
# 2019-01-21    Created file
# 2019-01-23    Updated to run different features in one workflow

############################################################ LOAD & PREP

# Load packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set options
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)
pd.set_option('display.float_format', '{:,.5f}'.format)

# Load datasets
f1 = pd.read_csv('df_features_1.csv')       # Count data
f2 = pd.read_csv('df_features_2.csv')       # Normalized data

# Setting random state
SEED = 1234

############################################################ WORKFLOW FUNCTIONS

# Load packages
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error as MSE

# Create model workflow that prep, train, and test random forest model
def rando(df, city, y_var, n_trees, depth, max_feat):
    
    # Split data into training and test sets
    geo = df[df['City'] == city].dropna(axis = 'rows')
    X = geo.drop(['GEOID', 'City', 'Collisions', 
                   'PedeInjuries', 'PedeDeaths', 
                   'TotalInjuries', 'TotalDeaths'], axis = 1)
    y = geo[y_var]
    
    # Split data into
    X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size = 0.4, random_state = SEED)
    
    # Model fitting
    rf = RandomForestRegressor(
        n_estimators = n_trees, 
        max_depth = depth,
        max_features = max_feat,
        random_state = SEED)
    rf.fit(X_train, y_train)
    
    # Predict class probability using fitted model 
    y_pred = rf.predict(X_test)
    
    # Score calculation
    fit_score = rf.score(X_train, y_train)
    rmse_score = np.sqrt(MSE(y_test, y_pred))
    
    # Prin restuls
    print("***** MODEL OUTPUT *****")
    print("")
    print("Target City: {}".format(geo['City'].unique()))
    print("Target Variable: {}".format(y_var))
    print("Model Fit: {:.2f}".format(fit_score))
    print("Model RMSE: {:.2f}".format(rmse_score))
    print("Target Mean: {:.2f}".format(np.mean(y)))
    print("Target Stdev: {:.2f}".format(np.std(y)))
    
    # Visualizing features importances
    importances = pd.Series(
    	data = rf.feature_importances_,
    	index = X_train.columns)
    importances_sorted = importances.sort_values()
    importances_sorted.plot(kind = 'barh', color = 'lightgreen')
    plt.title('Features Importances')
    plt.show()
    
    # Spaceholder
    print("")
    print("***** END OF OUTPUT *****")
    print("")

############################################################ NYC, OVERALL COLLISION RISK

# Run random forest model on NYC, Total Injuries, Feature Set 1
rando(df = f1, 
      city = "NYC", 
      y_var = "TotalInjuries", 
      n_trees = 500, 
      depth = 5,
      max_feat = 0.5
      )

# Run random forest model on NYC, Total Deaths, Feature Set 1
rando(df = f1, 
      city = "NYC", 
      y_var = "TotalDeaths", 
      n_trees = 500, 
      depth = 5,
      max_feat = 0.5
      )

# Run random forest model on NYC, Total Injuries, Feature Set 1
rando(df = f2,
      city = "NYC", 
      y_var = "TotalInjuries", 
      n_trees = 500, 
      depth = 5,
      max_feat = 0.5
      )

# Run random forest model on NYC, Total Deaths, Feature Set 1
rando(df = f2, 
      city = "NYC", 
      y_var = "TotalDeaths", 
      n_trees = 500, 
      depth = 5,
      max_feat = 0.5
      )

############################################################ LA, OVERALL COLLISION RISK

# Run random forest model on LA, Total Injuries, Feature Set 1
rando(df = f1, 
      city = "LA", 
      y_var = "TotalInjuries", 
      n_trees = 500, 
      depth = 5,
      max_feat = 0.5
      )

# Run random forest model on LA, Total Deaths, Feature Set 1
rando(df = f1, 
      city = "LA", 
      y_var = "TotalDeaths", 
      n_trees = 500, 
      depth = 5,
      max_feat = 0.5
      )

# Run random forest model on LA, Total Injuries, Feature Set 1
rando(df = f2,
      city = "LA", 
      y_var = "TotalInjuries", 
      n_trees = 500, 
      depth = 5,
      max_feat = 0.5
      )

# Run random forest model on LA, Total Deaths, Feature Set 1
rando(df = f2, 
      city = "LA", 
      y_var = "TotalDeaths", 
      n_trees = 500, 
      depth = 5,
      max_feat = 0.5
      )

############################################################ NYC, PEDESTRIAN RISK

# Run random forest model on NYC, Pedestrian Injuries, Feature Set 2
rando(df = f1, 
      city = "NYC", 
      y_var = "PedeInjuries", 
      n_trees = 500, 
      depth = 5,
      max_feat = 0.5
      )

# Run random forest model on NYC, Pedestrian Deaths, Feature Set 2
rando(df = f1, 
      city = "NYC", 
      y_var = "PedeDeaths", 
      n_trees = 500, 
      depth = 5,
      max_feat = 0.5
      )

# Run random forest model on NYC, Pedestrian Injuries, Feature Set 2
rando(df = f2,
      city = "NYC", 
      y_var = "PedeInjuries", 
      n_trees = 500, 
      depth = 5,
      max_feat = 0.5
      )

# Run random forest model on NYC, Pedestrian Deaths, Feature Set 2
rando(df = f2, 
      city = "NYC", 
      y_var = "PedeDeaths", 
      n_trees = 500, 
      depth = 5,
      max_feat = 0.5
      )

############################################################ LA, PEDESTRIAN RISK

# Run random forest model on LA, Pedestrian Injuries, Feature Set 2
rando(df = f1, 
      city = "LA", 
      y_var = "PedeInjuries", 
      n_trees = 500, 
      depth = 5,
      max_feat = 0.5
      )

# Run random forest model on LA, Pedestrian Deaths, Feature Set 2
rando(df = f1, 
      city = "LA", 
      y_var = "PedeDeaths", 
      n_trees = 500, 
      depth = 5,
      max_feat = 0.5
      )

# Run random forest model on LA, Pedestrian Injuries, Feature Set 2
rando(df = f2,
      city = "LA", 
      y_var = "PedeInjuries", 
      n_trees = 500, 
      depth = 5,
      max_feat = 0.5
      )

# Run random forest model on LA, Pedestrian Deaths, Feature Set 2
rando(df = f2, 
      city = "LA", 
      y_var = "PedeDeaths", 
      n_trees = 500, 
      depth = 5,
      max_feat = 0.5
      )


