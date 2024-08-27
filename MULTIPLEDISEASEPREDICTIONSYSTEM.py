import pickle
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant", layout="wide", page_icon="🧑‍⚕️")

# Page title
st.title("Our Team Details")

# Team details as a list of dictionaries
team_details = [
    {"Name": "Ganesh Pawar", "USN": "01FE22BEI051", "Roll No": 145},
    {"Name": "Aditya Narthi", "USN": "01FE22BEI014", "Roll No": 112},
    {"Name": "Shreyanand Darre", "USN": "01FE22BEI040", "Roll No": 134}
]

# Convert to DataFrame
df = pd.DataFrame(team_details)

# Display the DataFrame as a table
st.subheader("Team Members:")
st.table(df)

# Load pre-trained models using pickle
diabetes_model = pickle.load(open('C:/Users/Hp/Desktop/python/ML PROJECT/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('C:/Users/Hp/Desktop/python/ML PROJECT/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('C:/Users/Hp/Desktop/python/ML PROJECT/parkinsons_model.sav', 'rb'))

# Function to get diet plan based on age
def get_diet_plan(age):
    if age < 30:
        return (
            "For individuals under 30:\n"
            "- Focus on a balanced diet rich in whole grains, lean proteins, and healthy fats.\n"
            "- Include a variety of fruits and vegetables in your meals.\n"
            "- Avoid sugary snacks and processed foods.\n"
            "- Stay hydrated with plenty of water.\n"
            "- Examples: Grilled chicken salad, quinoa with veggies, fresh fruit."
        )
    elif 30 <= age < 50:
        return (
            "For individuals aged 30-50:\n"
            "- Maintain a diet that includes fiber-rich foods like vegetables, whole grains, and legumes.\n"
            "- Incorporate healthy fats and lean proteins.\n"
            "- Limit intake of refined carbs and sugary foods.\n"
            "- Monitor portion sizes to manage weight.\n"
            "- Examples: Baked salmon, lentil soup, mixed greens salad."
        )
    elif 50 <= age < 70:
        return (
            "For individuals aged 50-70:\n"
            "- Focus on heart-healthy foods including fruits, vegetables, whole grains, and lean proteins.\n"
            "- Incorporate omega-3 fatty acids from fish or flaxseeds.\n"
            "- Avoid excessive salt and sugary foods.\n"
            "- Ensure adequate hydration and fiber intake.\n"
            "- Examples: Oatmeal with berries, steamed broccoli with grilled chicken."
        )
    else:
        return (
            "For individuals over 70:\n"
            "- Prioritize nutrient-dense foods and maintain hydration.\n"
            "- Include a variety of soft, easy-to-digest foods with sufficient fiber.\n"
            "- Limit salt and sugar to manage blood pressure and blood sugar levels.\n"
            "- Examples: Soft-cooked vegetables, fish, and whole-grain porridge."
        )

# Function to get diet plan based on age for heart disease patients
def get_heart_disease_diet_plan(age):
    if age < 30:
        return (
            "For heart disease patients under 30:\n"
            "- Focus on heart-healthy foods, including lean proteins, whole grains, and vegetables.\n"
            "- Avoid trans fats, excessive salt, and sugary foods.\n"
            "- Maintain a diet rich in omega-3 fatty acids and antioxidants.\n"
            "- Examples: Grilled fish with quinoa, mixed vegetable salad, and fresh fruit."
        )
    elif 30 <= age < 50:
        return (
            "For heart disease patients aged 30-50:\n"
            "- Prioritize foods that lower cholesterol and blood pressure, such as oats, leafy greens, and fatty fish.\n"
            "- Include sources of soluble fiber like beans and lentils.\n"
            "- Minimize processed foods, refined carbs, and sodium.\n"
            "- Examples: Oatmeal with berries, roasted vegetables, and salmon."
        )
    elif 50 <= age < 70:
        return (
            "For heart disease patients aged 50-70:\n"
            "- Focus on foods that support cardiovascular health: whole grains, lean proteins, and fruits.\n"
            "- Reduce salt, limit alcohol, and stay hydrated.\n"
            "- Examples: Baked chicken with brown rice and steamed broccoli."
        )
    else:
        return (
            "For heart disease patients over 70:\n"
            "- Maintain a nutrient-rich diet with heart-healthy fats and lean proteins.\n"
            "- Soft and easy-to-digest foods are recommended.\n"
            "- Avoid foods high in saturated fats and sodium.\n"
            "- Examples: Steamed fish, whole-grain porridge, and lightly cooked vegetables."
        )

# Function to get dos and don'ts for diabetic patients
def get_diabetes_guidelines():
    return (
        "### Dos for Diabetic Patients:\n"
        "- **Monitor Blood Sugar Levels:** Regularly check blood sugar levels to stay informed about your health.\n"
        "- **Eat Balanced Meals:** Include a mix of proteins, fats, and carbohydrates in your meals.\n"
        "- **Choose Whole Foods:** Opt for whole grains, fresh vegetables, and fruits with a low glycemic index.\n"
        "- **Stay Hydrated:** Drink plenty of water throughout the day.\n"
        "- **Exercise Regularly:** Engage in regular physical activity to help manage blood sugar levels.\n"
        "- **Take Medications as Prescribed:** Follow your healthcare provider's advice on medication and insulin use.\n\n"
        "### Don'ts for Diabetic Patients:\n"
        "- **Avoid Sugary Foods:** Refrain from consuming foods high in sugar and refined carbohydrates.\n"
        "- **Don't Skip Meals:** Avoid skipping meals as it can affect blood sugar levels.\n"
        "- **Limit Processed Foods:** Reduce intake of processed and fast foods high in unhealthy fats and sodium.\n"
        "- **Avoid Excessive Alcohol:** Limit alcohol consumption, as it can interfere with blood sugar control.\n"
        "- **Don't Ignore Symptoms:** Pay attention to any symptoms of high or low blood sugar and seek medical advice if needed."
    )

# Function to get dos and don'ts for heart disease patients
def get_heart_disease_guidelines():
    return (
        "### Dos for Heart Disease Patients:\n"
        "- **Eat Heart-Healthy Foods:** Focus on fruits, vegetables, whole grains, and lean proteins.\n"
        "- **Monitor Cholesterol and Blood Pressure:** Keep track of these key health indicators.\n"
        "- **Stay Physically Active:** Engage in moderate exercise like walking or swimming.\n"
        "- **Take Medications as Prescribed:** Adhere to your healthcare provider’s recommendations.\n"
        "- **Manage Stress:** Practice relaxation techniques to lower stress.\n\n"
        "### Don'ts for Heart Disease Patients:\n"
        "- **Avoid Foods High in Saturated Fats:** Cut down on red meat and fried foods.\n"
        "- **Limit Sodium:** Reduce salt intake to manage blood pressure.\n"
        "- **Don’t Smoke or Drink Excessively:** Both smoking and alcohol can exacerbate heart conditions.\n"
        "- **Avoid Sedentary Lifestyle:** Sitting for long periods can worsen heart disease symptoms."
    )

# Sidebar with navigation menu
selected = option_menu(
    menu_title='MULTIPLE DISEASE PREDICTION SYSTEM',
    options=['DIABETES PREDICTION', 'HEART DISEASE PREDICTION', 'PARKINSONS PREDICTION'],
    icons=['activity', 'heart', 'person'],  
    default_index=0,
    orientation='horizontal'
)

# Diabetes Prediction Page
if selected == 'DIABETES PREDICTION':
    st.title('Diabetes Prediction using Machine Learning')

    # Create columns for better layout
    col1, col2, col3 = st.columns(3)

    # Input fields
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level (mg/dL)')
    with col3:
        BloodPressure = st.text_input('Blood Pressure (mm Hg)')

    with col1:
        SkinThickness = st.text_input('Skin Thickness (mm)')
    with col2:
        Insulin = st.text_input('Insulin Level (μU/ml)')
    with col3:
        BMI = st.text_input('Body Mass Index (BMI)')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
    with col2:
        Age = st.text_input('Age (years)')

    # Initialize variables for results
    diab_diagnosis = ''
    diet_plan = ''
    guidelines = ''

    # Button to get diabetes test result
    if st.button('Get Diabetes Test Result'):
        # Validate inputs and convert to float
        try:
            user_input = [float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness),
                          float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]
            
            # Check if any input is missing or invalid
            if all(val >= 0 for val in user_input):
                # Create DataFrame for prediction
                user_input_df = pd.DataFrame([user_input], columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
                                                                    'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])

                # Predict using the model
                diab_prediction = diabetes_model.predict(user_input_df)

                # Display results based on prediction
                if diab_prediction[0] == 1:
                    diab_diagnosis = 'The person is diabetic.'
                    diet_plan = get_diet_plan(float(Age))
                    guidelines = get_diabetes_guidelines()
                else:
                    diab_diagnosis = 'The person is not diabetic.'
            else:
                diab_diagnosis = 'Please ensure all input values are non-negative and valid.'
        except ValueError:
            diab_diagnosis = "Please ensure all inputs are numeric."

    # Display results
    st.success(diab_diagnosis)
    if diab_diagnosis == 'The person is diabetic.':
        st.subheader('Recommended Diet Plan:')
        st.write(diet_plan)
        st.subheader('Dos and Don’ts:')
        st.write(guidelines)

    # Button to explain diabetes and parameters
    if st.button('Learn About Diabetes and Parameters'):
        st.subheader('About Diabetes')
        st.write("""
        Diabetes is a chronic medical condition where the body is unable to properly process food for use as energy. 
        It occurs when the pancreas either does not produce enough insulin or the body does not effectively use the insulin it produces.
        
        **Type 1 Diabetes**: The body's immune system attacks insulin-producing cells in the pancreas.
        **Type 2 Diabetes**: The body becomes resistant to insulin or the pancreas does not produce enough insulin.
        
        **Gestational Diabetes**: Occurs during pregnancy and typically resolves after childbirth, though it increases the risk of developing Type 2 diabetes later in life.
        """)

        st.subheader('Parameters Explained')
        st.write("""
        - **Number of Pregnancies**: The number of times a person has been pregnant. Higher numbers may indicate a higher risk of diabetes.
        - **Glucose Level**: Measures the amount of glucose in the blood. Elevated levels can be a sign of diabetes.
        - **Blood Pressure**: Measures the force of blood against artery walls. High blood pressure can be related to diabetes.
        - **Skin Thickness**: Measures the thickness of skin folds. Increased thickness may indicate higher insulin resistance.
        - **Insulin Level**: The amount of insulin in the blood. Higher levels can indicate insulin resistance or diabetes.
        - **BMI (Body Mass Index)**: A measure of body fat based on weight and height. Higher BMI is associated with a higher risk of diabetes.
        - **Diabetes Pedigree Function**: A score based on family history of diabetes. It helps estimate genetic risk.
        - **Age**: The age of the person. Risk of diabetes increases with age.
        """)

        st.subheader('Learn More About Diabetes')
        st.write("Watch this informative video on diabetes:")
        st.video("https://youtu.be/XfyGv-xwjlI?si=9-a-K_s0tafZN15-")

# Heart Disease Prediction Page
if selected == 'HEART DISEASE PREDICTION':
    st.title('Heart Disease Prediction using Machine Learning')

    # Create columns for better layout
    col1, col2, col3 = st.columns(3)

    # Input fields
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex (1 = Male, 0 = Female)')
    with col3:
        cp = st.text_input('Chest Pain types (0 - Typical angina, 1 - Atypical angina, 2 - Non-anginal pain, 3 - Asymptomatic)')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure (mm Hg)')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar (> 120 mg/dl, 1 = True; 0 = False)')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results (0 - Normal, 1 - ST-T wave abnormality, 2 - Left ventricular hypertrophy)')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina (1 = Yes, 0 = No)')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise relative to rest')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment (0 = Upsloping, 1 = Flat, 2 = Downsloping)')
    with col3:
        ca = st.text_input('Number of major vessels colored by fluoroscopy (0-3)')

    with col1:
        thal = st.text_input('Thal (1 = Normal, 2 = Fixed defect, 3 = Reversible defect)')

    # Initialize variables for results
    heart_diagnosis = ''
    diet_plan = ''
    guidelines = ''

    # Button to get heart disease test result
    if st.button('Heart Disease Test Result'):
        # Validate inputs and convert to float
        try:
            user_input = [
                float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs),
                float(restecg), float(thalach), float(exang), float(oldpeak), float(slope),
                float(ca), float(thal)
            ]

            # Check if any input is missing or invalid
            if all(val >= 0 for val in user_input):
                # Predict using the model
                heart_prediction = heart_disease_model.predict([user_input])

                # Display results based on prediction
                if heart_prediction[0] == 1:
                    heart_diagnosis = 'The person has heart disease.'
                    diet_plan = get_diet_plan(float(age))  # Get a diet plan based on age
                    guidelines = get_heart_disease_guidelines()  # Dos and Don'ts for heart disease patients
                else:
                    heart_diagnosis = 'The person does not have heart disease.'
            else:
                heart_diagnosis = 'Please ensure all input values are non-negative and valid.'
        except ValueError:
            heart_diagnosis = "Please ensure all inputs are numeric."

    # Display results
    st.success(heart_diagnosis)
    
    if heart_diagnosis == 'The person has heart disease.':
        st.subheader('Recommended Diet Plan:')
        st.write(diet_plan)
        st.subheader('Dos and Don’ts for Heart Disease Patients:')
        st.write(guidelines)

    # Button to explain heart disease and parameters
    if st.button('Learn About Heart Disease and Parameters'):
        st.subheader('About Heart Disease')
        st.write("""
        Heart disease refers to a range of conditions that affect the heart, including coronary artery disease, heart attacks, and heart failure. 
        It often involves the narrowing or blockage of coronary arteries which can lead to reduced blood flow to the heart muscle.
        
        **Types of Heart Disease**:
        - **Coronary Artery Disease**: The most common type, caused by the buildup of plaque in the coronary arteries.
        - **Heart Attack**: Occurs when a coronary artery is blocked, leading to damage to the heart muscle.
        - **Heart Failure**: A condition where the heart is unable to pump blood effectively.
        - **Arrhythmias**: Abnormal heart rhythms that can affect the heart's ability to pump blood.
        """)

        st.subheader('Parameters Explained')
        st.write("""
        - **Age**: Age of the person. The risk of heart disease increases with age.
        - **Sex**: Gender of the person. Men are generally at higher risk at a younger age, but the risk for women increases post-menopause.
        - **Chest Pain Types (cp)**: Different types of chest pain can indicate various types of heart disease:
          - 0: Typical angina
          - 1: Atypical angina
          - 2: Non-anginal pain
          - 3: Asymptomatic
        - **Resting Blood Pressure (trestbps)**: High resting blood pressure is a risk factor for heart disease.
        - **Serum Cholestoral (chol)**: High levels of cholesterol can lead to plaque buildup in the arteries.
        - **Fasting Blood Sugar (fbs)**: High fasting blood sugar levels can be a sign of diabetes, which increases heart disease risk.
        - **Resting Electrocardiographic Results (restecg)**: Measures the electrical activity of the heart:
          - 0: Normal
          - 1: ST-T wave abnormality
          - 2: Left ventricular hypertrophy
        - **Maximum Heart Rate Achieved (thalach)**: Lower maximum heart rate during exercise can indicate heart disease.
        - **Exercise Induced Angina (exang)**: Angina caused by exercise can be a sign of heart disease.
        - **ST Depression (oldpeak)**: Depression in the ST segment of an ECG during exercise can indicate heart disease.
        - **Slope of Peak Exercise ST Segment (slope)**: Helps to determine the type of heart problem based on ST segment changes:
          - 0: Upsloping
          - 1: Flat
          - 2: Downsloping
        - **Number of Major Vessels Colored by Fluoroscopy (ca)**: Shows the number of major coronary arteries with significant narrowing.
        - **Thalassemia (thal)**: Blood disorder related to abnormal hemoglobin; can influence heart disease risk:
          - 1: Normal
          - 2: Fixed defect
          - 3: Reversible defect
        """)

        st.subheader('Learn More About Heart Disease')
        st.write("Watch this informative video on heart disease:")
        st.video("https://youtu.be/KPKLq-LQjbc?si=j46fsiOcacbu2-kM")

        
# Define the diet plan function
def get_parkinsons_diet_plan():
    return (
        "### Recommended Diet Plan for Parkinson's Disease Patients:\n"
        "- **Eat Fiber-Rich Foods:** Include whole grains, fruits, and vegetables to aid digestion.\n"
        "- **Stay Hydrated:** Drink plenty of water to help with medication absorption and prevent dehydration.\n"
        "- **Eat Small, Frequent Meals:** Helps with maintaining energy levels.\n"
        "- **Increase Antioxidants:** Include berries, dark leafy greens, and other foods rich in antioxidants to help combat oxidative stress.\n"
        "- **Healthy Fats:** Incorporate omega-3-rich foods like fish, flaxseeds, and walnuts.\n"
        "- **Protein Timing:** Consume protein at dinner rather than earlier in the day to avoid interference with Parkinson's medications.\n"
        "- **Examples:** Grilled salmon with steamed vegetables, oatmeal with flaxseeds and berries, and a side salad with olive oil dressing."
    )

# Define the guidelines function
def get_parkinsons_guidelines():
    return (
        "### Dos and Don'ts for Parkinson's Disease Patients:\n"
        "#### Dos:\n"
        "- **Take Medications as Prescribed:** Consistently take your medications and monitor their effects.\n"
        "- **Stay Active:** Engage in regular physical activities such as walking, yoga, or swimming.\n"
        "- **Eat a Balanced Diet:** Include a mix of vegetables, whole grains, and lean proteins in your meals.\n"
        "- **Keep a Routine:** Establish a consistent daily routine to help manage symptoms.\n"
        "- **Seek Support:** Join a support group or seek counseling if needed.\n\n"
        "#### Don'ts:\n"
        "- **Avoid Skipping Meals:** Ensure regular and balanced eating to prevent fatigue and medication complications.\n"
        "- **Don't Consume Too Much Protein at Once:** Space out protein intake, as it can interfere with certain Parkinson's medications.\n"
        "- **Limit Sugary Foods and Caffeine:** These can cause rapid changes in energy levels and worsen symptoms.\n"
        "- **Avoid Stress:** Stress can exacerbate symptoms, so engage in stress-reduction activities like mindfulness or deep breathing exercises."
    )

# Parkinson's Prediction Page
if selected == "PARKINSONS PREDICTION":
    st.title("Parkinson's Disease Prediction using Machine Learning")

    # Create columns for better layout
    col1, col2, col3, col4, col5 = st.columns(5)

    # Input fields for Parkinson's disease prediction (all valid parameters)
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
    with col3:
        DDP = st.text_input('Jitter:DDP')
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
    with col3:
        MDVP_APQ = st.text_input('MDVP:APQ')
    with col4:
        DDA = st.text_input('Shimmer:DDA')
    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    # Initialize variables for results
    parkinsons_diagnosis = ''
    diet_plan = ''
    guidelines = ''

    # Button to get Parkinson's test result
    if st.button("Parkinson's Test Result"):
        # Ensure that no input field is left empty
        if '' not in [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, MDVP_APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]:
            try:
                # Attempt to convert all inputs to float and store them in a list
                user_input = [
                    float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs),
                    float(RAP), float(PPQ), float(DDP), float(Shimmer), float(Shimmer_dB),
                    float(APQ3), float(APQ5), float(MDVP_APQ), float(DDA), float(NHR),
                    float(HNR), float(RPDE), float(DFA), float(spread1), float(spread2),
                    float(D2), float(PPE)
                ]

                # Perform prediction using the model
                parkinsons_prediction = parkinsons_model.predict([user_input])

                # Check the prediction result and display appropriate message
                if parkinsons_prediction[0] == 1:
                    parkinsons_diagnosis = "The person has Parkinson's disease."
                    diet_plan = get_parkinsons_diet_plan()  # Fetch the diet plan
                    guidelines = get_parkinsons_guidelines()  # Fetch the Dos and Don'ts
                else:
                    parkinsons_diagnosis = "The person does not have Parkinson's disease."
            except ValueError:
                # Handle non-numeric input
                parkinsons_diagnosis = "Please ensure all inputs are numeric."
        else:
            parkinsons_diagnosis = "Please fill out all input fields."

    # Display results
    st.success(parkinsons_diagnosis)
    
    if parkinsons_diagnosis == "The person has Parkinson's disease.":
        st.subheader('Recommended Diet Plan:')
        st.write(diet_plan)
        st.subheader('Dos and Don’ts for Parkinson’s Disease Patients:')
        st.write(guidelines)

    # Button to explain Parkinson's disease and parameters
    if st.button("Learn About Parkinson's Disease and Parameters"):
        st.subheader("About Parkinson's Disease")
        st.write("""
        Parkinson's disease is a progressive neurological disorder that affects movement. It occurs when nerve cells in the brain that produce dopamine, a neurotransmitter that helps control movement, become damaged or die. 

        **Symptoms**: 
        - Tremors or shaking
        - Stiffness or rigidity
        - Slowness of movement
        - Balance and coordination problems

        Parkinson's disease is progressive, meaning that symptoms worsen over time. While there is no cure, treatments are available to manage symptoms and improve quality of life.
        """)

        st.subheader('Parameters Explained')
        st.write("""
        - **MDVP:Fo (Hz)**: Fundamental frequency of the voice signal. It helps to assess vocal characteristics.
        - **MDVP:Fhi (Hz)**: Maximum frequency in the voice signal.
        - **MDVP:Flo (Hz)**: Minimum frequency in the voice signal.
        - **MDVP:Jitter (%)**: Variability in the pitch of the voice. High jitter can be indicative of voice disorders.
        - **MDVP:Jitter (Abs)**: Absolute variability in the pitch of the voice.
        - **MDVP:RAP**: Relative average perturbation in the pitch of the voice.
        - **MDVP:PPQ**: Pitch perturbation quotient, which measures short-term variations in the pitch.
        - **Jitter:DDP**: Difference in pitch perturbation, calculated over a period of time.
        - **MDVP:Shimmer**: Variability in the amplitude of the voice.
        - **MDVP:Shimmer(dB)**: Measure of shimmer in decibels.
        - **Shimmer:APQ3**: Amplitude perturbation quotient (3-point period).
        - **Shimmer:APQ5**: Amplitude perturbation quotient (5-point period).
        - **MDVP:APQ**: Amplitude perturbation quotient based on multiple cycles.
        - **Shimmer:DDA**: Difference in the amplitude of the voice signal over time.
        - **NHR**: Noise-to-harmonic ratio, indicating the amount of noise in the voice.
        - **HNR**: Harmonics-to-noise ratio, measuring the quality of the voice.
        - **RPDE**: Recurrence plot density entropy, a measure of voice signal complexity.
        - **DFA**: Detrended fluctuation analysis, used to assess the predictability of voice signal changes.
        - **spread1**: Spread of the first recurrence plot dimension.
        - **spread2**: Spread of the second recurrence plot dimension.
        - **D2**: Correlation dimension, which measures the complexity of the voice signal.
        - **PPE**: Percentage of perturbation entropy, used to analyze voice signal stability.
        """)

        st.subheader('Learn More About Parkinson’s Disease')
        st.write("Watch this informative video on Parkinson's disease:")
        st.video("https://youtu.be/NAfQoviLFR8?si=JIxkJBd5WeopAW8D")
