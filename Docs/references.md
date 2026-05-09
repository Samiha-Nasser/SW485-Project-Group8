# References
[1] Scikit-learn Documentation. "Logistic Regression." [Online]. Available: https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression

[2] GeeksforGeeks. "Random Forest Algorithm in Machine Learning." [Online]. Available: https://www.geeksforgeeks.org/machine-learning/random-forest-algorithm-in-machine-learning/.


[4] ttps://www.coursera.org/learn/advanced-learning-algorithms

[5] Scikit-learn Documentation. "Hyperparameter tuning using GridSearchCV and RandomizedSearchCV." [Online]. Available: https://scikit-learn.org/stable/modules/grid_search.html 

[6] Meta AI. (2024). Llama 3: Open Foundation and Fine-Tuned Chat Models. Retrieved from https://ai.meta.com/llama/

[7] Groq. (2024). Groq API Documentation. Retrieved from https://console.groq.com/docs

[8] A. Author(s), “Methodological challenges in explainable AI for fraud detection: a systematic literature review,” Artificial Intelligence Review, Springer, 2026. [Online]. Available: https://link.springer.com/article/10.1007/s10462-026-11516-7 .

[9] Chandola, V., Banerjee, A., & Kumar, V. (2009). "Anomaly detection: A survey." *ACM Computing Surveys*, 41(3), 1–58.  
*Used in: Section 1 (motivation for clustering in fraud detection), Section 1 GMM limitation (class imbalance and EM domination), Section 8.1 (class imbalance challenge), Section 8.3 (feature interpretability).*

[10] MacQueen, J. (1967). "Some Methods for Classification and Analysis of Multivariate Observations." *Proceedings of the 5th Berkeley Symposium*, 281–297.  
*Used in: Section 1 K-Means justification (scalability O(n·k·i), feature compatibility, hard assignments, k=2 rationale), Section 4.1 (WCSS definition, n_init, algorithm='lloyd'), Section 7 Strategy 1, Section 8.4.*

[11] GeeksforGeeks. "What is Silhouette Score in Machine Learning?" Available at: https://www.geeksforgeeks.org/machine-learning-what-is-silhouette-score/

Used in: Section 5.1 (Internal Metrics definition and algorithm-level evaluation).

[12] GeeksforGeeks. "Davies-Bouldin Index for Cluster Evaluation." Available at: https://www.geeksforgeeks.org/machine-learning-davies-bouldin-index/

Used in: Section 5.1 (Cross-algorithm geometric performance comparison)
[13] Ester, M., Kriegel, H. P., Sander, J., & Xu, X. (1996). "A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise." *KDD-96*, 226–231.  
*Used in: Section 1 Why Not Other Algorithms (DBSCAN O(n²) rejection rationale).*

[14] Pedregosa, F., et al. (2011). "Scikit-learn: Machine Learning in Python." *JMLR*, 12, 2825–2830.  
*Used in: Section 2 (KMeans, GaussianMixture, RobustScaler imports), Section 3 Step 4 (RobustScaler median/IQR rationale for fraud outliers, necessity for both K-Means distance and GMM covariance estimation).*

[15] Jolliffe, I. T. (2002). *Principal Component Analysis* (2nd ed.). Springer.  
*Used in: Section 2 (PCA import), Section 3 Step 5 (PCA for visualization only — explicit statement that clustering uses full 29D features), Section 5 Visualization 1, Section 8.4 (loss of semantic interpretability caused by PCA-transformed features).*

[16] Rousseeuw, P. J. (1987). "Silhouettes: A graphical aid to the interpretation and validation of cluster analysis." *Journal of Computational and Applied Mathematics*, 20, 53–65.  
*Used in: Section 2 (silhouette_score import), Section 4.1 (Silhouette Score as k-selection method, definition), Section 5 (internal metric definition),  Section 6.3 (cross-algorithm comparison discussion).*

[17] Davies, D. L., & Bouldin, D. W. (1979). "A cluster separation measure." *IEEE TPAMI*, 1(2), 224–227.  
*Used in: Section 2 (davies_bouldin_score import), Section 4.1 (Davies-Bouldin Index as k-selection method, definition), Section 5 (internal metric definition), Section 6.3 (cross-algorithm comparison discussion).*

[18] Hubert, L., & Arabie, P. (1985). "Comparing partitions." *Journal of Classification*, 2(1), 193–218.  
*Used in: Section 2 (ARI, homogeneity, completeness imports), Section 5 (external metric definitions, post-hoc only clarification), Section 6.3 (comparison interpretation), Section 8.5 (expected low external scores under severe class imbalance).*


