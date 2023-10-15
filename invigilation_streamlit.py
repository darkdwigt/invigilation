import streamlit as st
import pandas as pd
import numpy as np

def invigilation_allocation(teachers_data, exams_data):
    subjects = exams_data['Subject'].unique()
    tally = {teacher: 0 for teacher in teachers_data['name']}
    allocations = {}
    schedule_df = exams_data.copy()

    for _, exam in exams_data.iterrows():
        subject = exam['Subject']
        subject_teachers = teachers_data[teachers_data['subjects'].str.contains(subject)]['name'].tolist()
        
        if not subject_teachers:
            allocations[exam['Subject']] = 'No teachers available'
            continue

        min_tally = min([tally[teacher] for teacher in subject_teachers])
        available_teachers = [teacher for teacher in subject_teachers if tally[teacher] == min_tally]

        allocated_teacher = np.random.choice(available_teachers)
        allocations[exam['Subject']] = allocated_teacher
        tally[allocated_teacher] += 1

        schedule_df.loc[schedule_df['Subject'] == subject, 'Invigilator'] = allocated_teacher

    return allocations, tally, schedule_df


def main():
    st.title('Invigilation Allocation')
    
    uploaded_teachers = st.file_uploader("Upload teachers data", type=['csv'])
    uploaded_exams = st.file_uploader("Upload exams data", type=['csv'])

    if uploaded_teachers and uploaded_exams:
        teachers_data = pd.read_csv(uploaded_teachers)
        exams_data = pd.read_csv(uploaded_exams)
        
        if st.button("Generate Allocation"):
            allocations, tally, schedule_df = invigilation_allocation(teachers_data, exams_data)
            st.write("Allocations:")
            st.write(allocations)
            st.write("Tally:")
            st.write(tally)
            st.write("Invigilation Schedule:")
            st.table(schedule_df)

if __name__ == '__main__':
    main()
