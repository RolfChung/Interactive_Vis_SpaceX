# Interactive visualisation and analysis for SpaceX launch sites and launches

# **SpaceX Falcon 9 Launch Success Prediction**  
### *A Data Science Capstone Project*  

---

## **📌 Project Overview**  
This project aims to **predict whether SpaceX’s Falcon 9 first-stage rocket will land successfully**, a critical factor in determining launch costs. Unlike competitors charging **\$165M+ per launch**, SpaceX's reusability allows launches at **\$62M**, making accurate success prediction vital for cost estimation and competitive bidding.  

Using **machine learning and data analytics**, we analyze past launch data to build a predictive model, helping stakeholders optimize mission planning and risk management.  

---

## **🔍 Key Questions Answered**  
✅ **Can we predict Falcon 9 landing success with high accuracy?**  
✅ **What factors most influence landing success?**  
✅ **How does launch success impact cost estimation?**  
✅ **How can competitors (e.g., "Space Y") use this data for strategic decisions?**  

---

## **📊 Methodology & Insights**  

### **1. Data Collection & Preprocessing**  
- **Data Sources:**  
  - **SpaceX REST API** (`api.spacexdata.com/v4/launches/past`)  
  - **Web Scraping** (Wikipedia Falcon 9 launch tables)  
- **Key Steps:**  
  - Filtered Falcon 9 launches (excluded Falcon 1).  
  - Handled missing values (e.g., imputed `PayloadMass` with mean).  
  - Encoded categorical variables (e.g., `LaunchSite`, `LandingPad`).  

### **2. Interactive Visual Analytics**  
- **Folium Maps:** Analyzed launch site locations & success rates.  
- **Plotly Dash Dashboard:**  
  - Interactive dropdowns & sliders for dynamic filtering.  
  - Visualized trends in payload mass, launch sites, and success rates.  

### **3. Machine Learning Model**  
- **Best Model:** **Decision Tree (83.3% accuracy)** outperformed:  
  - Logistic Regression  
  - SVM  
  - KNN  
- **Key Metrics:**  
  - **Precision (Success Class): 92.3%**  
  - **Recall (Success Class): 85.7%**  
- **Business Impact:**  
  - Helps SpaceX optimize reusable launches.  
  - Enables competitors to estimate costs for competitive bids.  

---

## **🚀 Key Findings**  
✔ **Higher flight numbers** → **More successful landings**.  
✔ **VAFB-SLC launch site** never launched heavy payloads (>10,000 mass).  
✔ **ES-L1, GEO, HEO orbits** had the highest success rates.  
✔ **Success rates improved significantly from 2013–2020**, peaking in 2019.  

---

## **💡 Conclusion & Business Value**  
- The **Decision Tree model** is highly effective in predicting landing success.  
- **Accurate predictions** help:  
  - **SpaceX** reduce costs via reusable rockets.  
  - **Competitors** make data-driven bidding decisions.  
  - **Clients** assess mission risks and costs.  

---

## **🛠 Tools & Technologies**  
- **Python** (Pandas, NumPy, Scikit-learn)  
- **Data Collection:** SpaceX API, BeautifulSoup (Web Scraping)  
- **Visualization:** Matplotlib, Seaborn, Folium, Plotly Dash  
- **Machine Learning:** Decision Trees, Logistic Regression, SVM, KNN  

---

## **📂 Repository Structure**  
```
📦SpaceX-Launch-Prediction  
├── 📂data/                # Raw & processed datasets  
├── 📂notebooks/           # Jupyter notebooks (EDA, modeling)  
├── 📂scripts/             # Python scripts (API calls, scraping)  
├── 📂dash/                # Plotly Dash dashboard  
├── 📜README.md            # Project overview  
└── 📜requirements.txt     # Python dependencies  
```

---

## **🔗 How to Use This Project**  
1. **Clone the repo**:  
   ```bash  
   git clone https://github.com/your-repo/SpaceX-Launch-Prediction.git  
   ```  
2. **Install dependencies**:  
   ```bash  
   pip install -r requirements.txt  
   ```  
3. **Run Jupyter notebooks** for EDA, modeling, or launch the Dash app.  

---

**🌟 Contributions & feedback welcome!** Let’s make space data more accessible! 🚀  

--- 

Would you like any refinements or additional sections (e.g., "Future Work")?
