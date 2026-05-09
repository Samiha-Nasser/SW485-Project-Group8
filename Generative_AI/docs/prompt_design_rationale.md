The following section explains the design rationale and thought process behind each prompt template, along with how domain knowledge and prompt engineering principles influenced their development. It also summarizes key insights obtained during testing and evaluation.

The Thought Process Behind Each Template

The Fraud Explanation Template (T1) was designed to transform the output of fraud detection models from a binary classification (Fraud / Not Fraud) into a human-understandable explanation. The design focuses on enhancing interpretability by linking the model’s prediction to transaction features, allowing the decision to be expressed in a clear and understandable textual form. This ensures that model outputs are not presented as opaque results, but rather as meaningful explanations grounded in observable transaction characteristics.

The User Advice Template (T2) was developed to address the limitation that detection outputs alone are not sufficient for practical use. In real-world fraud detection systems, identifying suspicious activity must be followed by immediate and actionable responses. Therefore, this template converts the model’s prediction into direct security instructions, such as account protection steps or risk mitigation actions. This design reflects standard practices in fraud prevention systems where analytical outputs are operationalized into user-facing guidance.

The Fraud Risk Scoring Template (T3) was introduced to overcome the limitations of binary classification by providing a graded representation of risk. In fraud management, risk is not strictly binary but varies depending on context. Accordingly, this template integrates model outputs with transaction features to produce a simplified risk level (Low, Medium, High), enabling clearer interpretation of severity and supporting decision-making processes.

The Comparative Fraud Analysis Template (T4) is based on the principle that fraudulent behavior often follows recurring and identifiable patterns. These patterns can be observed through transaction attributes such as timing, amount, and deviations from normal user behavior. This template therefore compares the current transaction against known fraud patterns to highlight similarities that support the model’s prediction, providing a more contextual and structured explanation of why a transaction is considered suspicious.


How Domain Knowledge Influenced the Design

The design of these templates is grounded in established principles in modern fraud detection systems. The literature indicates that such systems do not rely solely on predictive accuracy, but also require explainability as a fundamental component in high-risk environments. Explainability plays a critical role in enabling fraud analysts and regulatory stakeholders to understand and justify model decisions, thereby improving transparency, trust, and regulatory compliance.

Furthermore, prior research shows that fraud typically manifests through anomalous behavioral patterns that deviate from normal user behavior. This supports the inclusion of both explanation-based and pattern-comparison templates, allowing each transaction to be analyzed within its behavioral context rather than relying solely on a final classification output.

Building on this, the template design supports multiple levels of decision-making. This includes a Fraud Risk Scoring Template that provides a graded representation of risk (Low, Medium, High) instead of a binary decision, aligning with real-world risk management practices in financial systems. In addition, the User Advice Template translates analytical outputs into actionable recommendations such as requesting additional verification or escalating cases for human review. This ensures that the system output is not limited to prediction and explanation, but is also operationally useful in practical fraud detection workflows.


Lessons learned during prompt testing 

The testing and analysis stage for the Generative AI component proved to be educational as numerous insights were obtained in relation to prompt creation, output analysis, and how AI behaves in fraud detection situations. Testing was performed by inputting four different prompts into multiple cases of either fraud or legitimate transactions and analyzing the resulting output.

1. Prompt Structure Strongly Influences AI Responses
It was observed that the structure and wording of a prompt had a significant impact on the generated response. Clear instructions and organized formatting on templates consistently led to accurate, detailed and understandable explanations. There was often a significant difference in tone, clarity and completeness due to small changes in wording.

2. Specialized Prompts Perform Better Than Generic Prompts
As demonstrated by the testing, prompts created for a specific purpose were more effective than general purpose prompts. For example:
The Fraud Explanation template resulted in better explanations of suspicious transactions.
The User Advice template produced more useful suggestions for the users.
The Risk Scoring template generated more analytical responses that were geared towards transaction severity. 
The Comparative Analysis template proved to provide more in-depth analysis, although sometimes produced unnecessarily complicated explanations.
This demonstrated that prompt specialization improves output quality and alignment with system goals.

3. Readability and Detail Must Be Balanced
The responses that were very detailed were sometimes more informative but were more difficult to understand by the non-technical users. Responses were simplified for better readability but were not always detailed enough. The testing process revealed the need to balance technical depth, Simplicity, User readability and Explanation completeness.


References to prompt engineering best practices

The prompt templates in this work were designed based on several best practices in Prompt Engineering that were studied. First, clarity and specificity were applied by defining the model as a financial fraud detection assistant, which helps constrain the context and improve response accuracy. Second, clear and structured information was provided to the model, such as transaction features and prediction results, which helps it better understand the task and generate more accurate and relevant outputs. In addition, a controlled output format was enforced, such as defining risk levels (Low, Medium, High) or requiring short and clear responses, which makes the results more suitable for use in decision-making systems.
