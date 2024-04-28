class MedicalExpertSystem:
    def __init__(self):
        self.disease_symptoms = {
            "Common Cold": ["sore throat", "runny nose", "cough", "sneezing"],
            "Influenza": ["fever", "muscle aches", "fatigue", "headache"],
            "Strep Throat": ["sore throat", "fever", "swollen lymph nodes"],
            "Pneumonia": ["fever", "shortness of breath", "chest pain", "cough"],
            "Urinary Tract Infection": ["frequent urination", "burning sensation", "cloudy urine"],
            "Gastroenteritis": ["nausea", "vomiting", "diarrhea", "abdominal pain"],
            "Bronchitis": ["cough", "mucus production", "chest discomfort"],
            "Asthma": ["wheezing", "shortness of breath", "chest tightness", "cough"],
            "Sinusitis": ["facial pain", "nasal congestion", "postnasal drip", "headache"],
            "Allergic Rhinitis": ["runny nose", "itchy eyes", "sneezing", "nasal congestion"]
        }

    def diagnose(self, symptoms):
        possible_diseases = []
        for disease, disease_symptoms in self.disease_symptoms.items():
            if set(disease_symptoms) == set(symptoms):
                possible_diseases.append(disease)
        return possible_diseases

# Example usage:
if __name__ == "__main__":
    expert_system = MedicalExpertSystem()
    input_symptoms = ["sore throat", "cough"]
    possible_diseases = expert_system.diagnose(input_symptoms)
    if possible_diseases:
        print("Possible diseases:", possible_diseases)
    else:
        print("No matching diseases found.")
