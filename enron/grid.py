from sklearn.model_selection import GridSearchCV
n_features = np.arange(1, len(features_list))
pipe = Pipeline([ ('select_features', SelectKBest()),
    ('classify', DecisionTreeClassifier()) ])
param_grid = [{ 'select_features__k': n_features }]
tree_clf= GridSearchCV(pipe, param_grid=param_grid, scoring='f1', cv = 10)
tree_clf.fit(features, labels);
n_features = np.arange(1, len(features_list))
pipe = Pipeline([ ('select_features', SelectKBest()),
    ('classify', AdaBoostClassifier()) ])
param_grid = [{ 'select_features__k': n_features }]
ada_clf= GridSearchCV(pipe, param_grid=param_grid, scoring='f1', cv =10)
ada_clf.fit(features, labels)
