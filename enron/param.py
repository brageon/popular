tree_pipe = Pipeline([ ('select_features', SelectKBest(k=19)),
    ('classify', DecisionTreeClassifier()), ])
param_grid = dict(classify__criterion = ['gini', 'entropy'] , classify__min_samples_split = [2, 4, 6, 8, 10, 20], classify__max_depth = [None, 5, 10, 15, 20], classify__max_features = [None, 'sqrt', 'log2', 'auto'])
tree_clf = GridSearchCV(tree_pipe, param_grid = param_grid, scoring='f1', cv=10)
tree_clf.fit(features, labels)
tree_clf.best_params_
tree_clf = Pipeline([ ('select_features', SelectKBest(k=20)),
    ('classify', DecisionTreeClassifier(criterion='entropy', max_depth=None, max_features=None, min_samples_split=20)) ])
tester.dump_classifier_and_data(tree_clf, my_dataset, features_list)
tester.main()
ada_pipe = Pipeline([('select_features', SelectKBest(k=20)), ('classify', AdaBoostClassifier()) ])
param_grid = dict(classify__base_estimator=[DecisionTreeClassifier(), RandomForestClassifier(), GaussianNB()], classify__n_estimators = [30, 50, 70, 120], classify__learning_rate = [0.5, 1, 1.5, 2, 4])
ada_clf = GridSearchCV(ada_pipe, param_grid=param_grid, scoring='f1', cv=10)
ada_clf.fit(features, labels)
ada_clf.best_params_
tree_clf = Pipeline([ ('select_features', SelectKBest(k=19)),
    ('classify', DecisionTreeClassifier(criterion='entropy', max_depth=None, max_features=None, min_samples_split=20)) ])
tester.dump_classifier_and_data(tree_clf, my_dataset, features_list)
tester.main()
ada_clf = Pipeline([('select_features', SelectKBest(k=23)), ('classify', AdaBoostClassifier(base_estimator=DecisionTreeClassifier(), learning_rate=1, n_estimators=70)) ])
tester.dump_classifier_and_data(ada_clf, my_dataset, features_list)
tester.main()