import streamlit as st
import pickle
import numpy as np
import datetime


st.title("Flight fare")

pickle_in = open("flightact.pkl","rb")
model=pickle.load(pickle_in)

def prediction():
    source=st.selectbox("Choose source",["Bangalore","Kolkata","Chennai","Delhi","Mumbai"])
    dest=st.selectbox("Choose destination",["Delhi","Bangalore","Cochin","Kolkata","Hyderabad"])
    if source==dest:
        st.warning("Destination cannot be equal to source")
    else:
        
        Source_Chennai=0
        Source_Delhi=0
        Source_Kolkata=0
        Source_Mumbai=0
        
        if source=="Chennai":
            Source_Chennai+=1
        if source=="Delhi":
            Source_Delhi+=1
        if source=="Chennai":
            Source_Chennai+=1
        if source=="Mumbai":
            Source_Mumbai+=1
        else:
            Source_Mumbai+=0
        
        Destination_Cochin=0
        Destination_Delhi=0
        Destination_Hyderabad=0
        Destination_Kolkata=0
        
        if dest=="Cochin":
            Destination_Cochin+=1
        if dest=="Delhi":
            Destination_Delhi+=1
        if dest=="Hyderabad":
            Destination_Hyderabad+=1
        if dest=="Kolkata":
            Destination_Kolkata+=1
        else:
            Destination_Kolkata+=0
            
    
  
        airline=st.selectbox("Choose the Airline:",["Air India","Indi Go","Jet Airways","Spice Jet","Multiple Carriers","Multiple Carriers Premium Economy","GoAir","Vistara","Vistara Premium Economy","Air Asia","Trujet"])
        Airline_Air_India=0
        Airline_GoAir=0
 
        Airline_IndiGo=0
        Airline_Jet_Airways=0
        Airline_Multiple_carriers=0
        Airline_Multiple_carriers_Premium=0
        Airline_SpiceJet=0
        Airline_Trujet=0
        Airline_Vistara=0
        Airline_Vistara_Premium=0
        
        if airline=="Air India":
             Airline_Air_India+=1
             
        if airline=="GoAir":
            Airline_GoAir+=1
        
        if airline=="Indi Go":
            Airline_IndiGo+=1
            
        if airline=="Jet Airways":
            Airline_Jet_Airways+=1
            
        if airline=="Multiple Carriers":
            Airline_Multiple_carriers+=1
            
        if airline=="Multiple Carriers Premium Economy":
            Airline_Multiple_carriers_Premium+=1
            
        if airline=="Spice Jet":
            Airline_SpiceJet+=1
            
        if airline=="Trujet":
            Airline_Trujet+=1
            
        if airline=="Vistara":
            Airline_Vistara+=1
            
        if airline=="Vistara Premium Economy":
            Airline_Vistara_Premium+=1
            
        else:
            Airline_Vistara_Premium+=0
            
    
    
        
        today = datetime.date.today()
        now=datetime.datetime.now()
    
        start_date = st.date_input('Start date', today)
        
    
        start_time=st.time_input("Start time",now)
       
        
        
        stops=st.selectbox("Direct flight or with stops",("Direct","1 Stop","2 Stops","3 Stops","4 Stops"))
        Total_Stops=0
        if stops=="Direct":
            Total_Stops+=0
        if stops=="1 Stop":
            Total_Stops+=1
        if stops=="2 Stops":
            Total_Stops+=2
        if stops=="3 Stops":
            Total_Stops+=3
        if stops=="4":
            Total_Stops+=4
            

        obj1=""
        if st.button("Predict"):
            dd1=str(start_date)
            startdate1 = datetime.datetime.strptime(dd1,"%Y-%m-%d")
            month_of_journey=startdate1.month
            day_of_journey=startdate1.day
         
            
            dat1=str(start_time)
            dat = datetime.datetime.strptime(dat1,"%H:%M:%S")
            dep_hour=dat.hour
            dep_min=dat.minute
            
     
            result=model.predict([[Total_Stops,day_of_journey,month_of_journey,dep_hour,dep_min,Airline_Air_India,Airline_GoAir,Airline_IndiGo,Airline_Jet_Airways,Airline_Multiple_carriers,Airline_Multiple_carriers_Premium,Airline_SpiceJet,Airline_Trujet,Airline_Vistara,Airline_Vistara_Premium,Source_Chennai,Source_Delhi,Source_Kolkata,Source_Mumbai,Destination_Cochin,Destination_Delhi,Destination_Hyderabad,Destination_Kolkata]])
            obj=float(result)
            obj1=round(obj,2)
            st.success('The price is {}'.format(obj1))
    
 

    
    
    
 
if __name__=='__main__':
    prediction()