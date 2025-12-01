# E-commerce-Product-Delivery-Prediction
Develope robust machine learning models to accurately predict product delivery timeliness. By utilizing these models, the company aims to improve customer satisfaction, optimize logistics, and gain insights into factors affecting delivery performance.

## **Introduction** 
In today’s highly competitive e-commerce market, customer retention is essential for long-term business success and sustainable growth. 
This project aims to enhance the understanding of product delivery patterns and customer behaviour for an international e-commerce company specializing in electronic products. 
The goal is to develop robust machine learning models to accurately predict product delivery timeliness, enabling the company to improve customer satisfaction, optimize logistics, and gain insights into factors affecting delivery performance.
The dataset used includes customer care calls, customer rating, prior purchases, Mode of Shipments, Cost of the Product, Product Importance, Weight etc. 

## **Deployment Flow** 
<img width="772" height="362" alt="image" src="https://github.com/user-attachments/assets/cc8d996c-d5f0-4c28-a0d5-0794a519c325" />

## **Dataset Overview** 
<img width="953" height="437" alt="image" src="https://github.com/user-attachments/assets/474b5509-222b-4254-a398-b151d0d076df" />

## **Data Preprocessing**
* **Checked for missing values:  No missing data was found.**
* **Detecting and removing Outlier (Weight in gms).**
* **Converted categorical features to numerical using encoding (Label encoding for Gender, Warehouse Block, Product Importance, Mode of shipment).**
* **Normalized Numerical features (Cost of the Product, Discount Offered, Weight in gms, Customer care call, Customer Ratings).**
* **Split data into training (75%) and testing (25%) sets for model building. ** 

## **Visualization on Power BI**
<img width="1369" height="774" alt="image" src="https://github.com/user-attachments/assets/cc6daa7c-a23d-4474-a3fd-a938d2e2b9a5" />

## **Machine Learning Models**
All models were evaluated using accuracy, precision, recall, and F1-score to ensure robust performance comparison.

### **Logistic Regression**
* **Interpreted linear relationships between features (Accuracy - 64%).**
### **Decision Tree Classifier**
* **Selected optimal parameters via grid search (Accuracy - 67%).**
* **Grid Search in Decision Tree: Accuracy - 68%.**
* **Max depth:4, minimum samples leaf: 1, minimum samples split: 2.**
### **Random Forest Classifier**
* **Explored ensemble learning for improved accuracy (Accuracy - 67%).**
* **Max depth:4, minimum samples leaf: 2, minimum samples split: 2.**
* **Grid search in random forest: Accuracy - 68%.**
### **K-Nearest Neighbors**
* **Examined proximity-based decision-making (Accuracy - 65%).**


## **Conclusion**
* **The project's objective was to forecast on-time delivery for an e-commerce company's products and to explore factors influencing delivery times and customer behaviour.**
* **The exploratory analysis highlighted that product weight and cost are crucial to delivery success, with products in the 4000-6000 gms range and priced approximately $300 being more likely to arrive on time. A significant volume of products was dispatched from warehouse F using shipping, suggesting its proximity to a seaport.**
* **Customer behaviour also sheds light on delivery outcomes. An increase in customer care calls often correlates with delivery delays.**
* **In contrast, customers with a history of multiple purchases tend to experience more punctual deliveries, which might explain their repeat business.**
* **Products with discounts ranging from 0-10% tend to arrive on time. Meanwhile, products with discounts above 10% are more likely to not arrive on time.**



