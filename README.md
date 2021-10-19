# Background and Purpose
Most utility companies currently use static power transformer rating assumption, in many cases the nameplate ratings for long-term system planning.These assumptions can be overly conservative or inaccurate as they do not reflect the dynamic temperature conditions in the planning region throughout a year. This is especially true for relatively cold areas such as Canada where the ambient temperatures are relatively low. Proper combinations of dynamic loading and ambient temperature could safely allow transformer loading to exceed the nameplate rating without causing any damage. Therefore, to improve the cost-effectiveness of planning decisions, a scientific and realistic way to establish annual continuous dynamic rating for power transformers is required. In response, this project aims to use a data-driven method for producing annual continuous dynamic rating of power transformers to serve the long-term planning purpose. 
# Modeling Method
The flowchart of the modeling method is shown in Fig.1. First of all, analyze the past 5-year temperature, loading and load composition data of existing power transformers in a planning region. Based on such data and the forecasted area load composition, a future power transformer’s loading profile can be constructed by using Gaussian Mixture Model. Then a power transformer thermal aging model can be established to incorporate future loading and temperature profiles. As a result, annual continuous dynamic rating profiles under different temperature scenarios can be determined. The profiles can reflect the long-term thermal overloading risk in a much more realistic and granular way, which can significantly improve the accuracy of power transformer planning.

![Alt text](https://github.com/jsun66/Dynamic-Rating-Forecast-for-Long-term-Power-Transformer-Planning/blob/main/Tables%20and%20Figures/Fig.1.%20Flowchart.png)
Fig.1. Workflow of the modeling method
# Constructing Normalized 24-hr Loading Profile for the Future Transformer
By using GMM, existing transformers within the 5 days along with the future transformer are clustered together based on their load composition features. An example of clustering result based on residential load percentage and commercial load percentage features for 80 transformers in 5 days with 6 clusters is shown in Fig.2.
![Alt text](https://github.com/jsun66/Dynamic-Rating-Forecast-for-Long-term-Power-Transformer-Planning/blob/main/Tables%20and%20Figures/Fig.2.%20Transformer%20GMM%20clustering%20result.png)

Fig.2. An example of transformer GMM clustering result

An example of constructed normalized 24-hr loading profile versus 6 cluster centroid normalized profiles is plotted in Fig.3.
![Alt text](https://github.com/jsun66/Dynamic-Rating-Forecast-for-Long-term-Power-Transformer-Planning/blob/main/Tables%20and%20Figures/Fig.3.%20loading%20profile.png)

Fig.3. An example of constructing normalized 24-hr loading profile
# Results of Annual Dynamic Rating Profiles
By using the method, three annual dynamic rating profiles in 2023 with an assumed future load composition (60%, 30%) for a 50MVA ONAF power transformer typically used by the utility is given in Fig.4. In general, the summer months (May to Sep.) have lower rating than winter months (Oct. to Apr.) and this is because summer has higher ambient temperatures. Also, the high temperature scenario yields low dynamic rating and vice versa.
![Alt text](https://github.com/jsun66/Dynamic-Rating-Forecast-for-Long-term-Power-Transformer-Planning/blob/main/Tables%20and%20Figures/Fig.4.%20Forecasted%20rating%20profiles.png)
Fig.4. Forecasted transformer annual dynamic rating profiles in 2023
