#!/usr/bin/python
# -*- coding: utf-8 -*-
import io
from zipfile import ZipFile
import os
from django.shortcuts import render
from django.http import HttpResponse

def warn(*args, **kwargs):
    pass

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

#from .models import *

def upload_csvmodel(request):
    import requests
    import pandas as pd

    #logger = logging.getLogger("log_hritik")
    #logger.info("Whatever to log")
    #img_path = "media/dog.jpeg"
    result=""
    render_html='upload_csvmodel.html'
    #file upload html
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs=FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
        #testing = ''
        ##datamiminig
        result = "media/"+uploaded_file.name#path save
        #print(result)

        #prashnat code
        data = pd.read_csv(result)
        
        #data_filtered
        list=[]
        for i in data['Accepted Compound ID']:
            i=str(i)
            if ("plasmalogen" in i) or ("LPC" in i) or ("PC" in i):
                list.append(i)
        data_filtered = data.loc[data['Accepted Compound ID'].isin(list)]
        
        #data_filtered_PC
        list_PC=[]
        for i in list:
            i=str(i)
            if (" PC" in i):
                list_PC.append(i)

        data_filtered_PC = data_filtered[data_filtered['Accepted Compound ID'].isin(list_PC)]
        data_filtered_PC.to_csv('dfPC.csv',index=False)
        
        #list_plasmalogen
        list_plasmalogen=[]
        for i in list:
            i=str(i)
            if ("plasmalogen" in i):
                list_plasmalogen.append(i)
        data_filtered_plasmalogen = data_filtered[data_filtered['Accepted Compound ID'].isin(list_plasmalogen)]
        data_filtered_plasmalogen.to_csv('dfPLAS.csv',index=False)

        #DATA_FILTERED_LPC
        list_LPC=[]
        for i in list:
            i=str(i)
            if ("LPC" in i):
                list_LPC.append(i)

        data_filtered_LPC = data_filtered[data_filtered['Accepted Compound ID'].isin(list_LPC)]
        data_filtered_LPC.to_csv('dfLPC.csv',index=False)

        #render bank file
        zip_file_list = ['dfLPC.csv','dfPC.csv','dfPLAS.csv']
        download_file = io.BytesIO()
        with ZipFile(download_file,'w') as zip_file:
            for csv_file in zip_file_list:
                zip_file.write(csv_file)
                os.remove(csv_file) 
        response = HttpResponse(download_file.getvalue(),content_type='application/octet-stream')		
        response['Content-Disposition'] = 'attachment; filename="Q1_output.zip"'
                
        return response

        

    return render(request,render_html)
    #return render(request,'upload_csvmodel.html',{'f5':'/static/img.png')



def question(request):
    import requests
    import pandas as pd

    #logger = logging.getLogger("log_hritik")
    #logger.info("Whatever to log")
    #img_path = "media/dog.jpeg"
    result=""
    render_html='question.html'
    #file upload html
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs=FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
        #code
        result = "media/"+uploaded_file.name
        df = pd.read_csv(result)
        df.shape

        df.head()

        x = df["Accepted Compound ID"]

        a = len(x)

        df1 = df["Retention time (min)"]

        for i in range(a):
            df1.iloc[i] = round(df1.iloc[i])

        df1 = df1.to_frame(name = "Retention time RoundOff (min)")
        

        df = df.join(df1)

        df.head()

        DF = df[df["Retention time RoundOff (min)"].duplicated()]
        
        DF.to_csv('q2.csv',index=False)

        #render bank file
        zip_file_list = ['q2.csv']
        download_file = io.BytesIO()
        with ZipFile(download_file,'w') as zip_file:
            for csv_file in zip_file_list:
                zip_file.write(csv_file)
                os.remove(csv_file) 
        response = HttpResponse(download_file.getvalue(),content_type='application/octet-stream')		
        response['Content-Disposition'] = 'attachment; filename="Q2_output.zip"'
                
        return response

    return render(request,render_html)

def questionth(request):
    import requests
    import pandas as pd
    import csv
    from csv import writer
    #logger = logging.getLogger("log_hritik")
    #logger.info("Whatever to log")
    #img_path = "media/dog.jpeg"
    result=""
    render_html='questionth.html'
    #file upload html
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs=FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
        #code  
        result = "media/"+uploaded_file.name
        df = pd.read_csv(result) 

        df.shape

        df.head()

        x = df["Accepted Compound ID"]

        a = len(x)

        df1 = df["Retention time (min)"]

        for i in range(a):
            df1.iloc[i] = round(df1.iloc[i])

        df1 = df1.to_frame(name = "Retention time RoundOff (min)")

        df = df.join(df1)

        data_top = df.head()

        DF = df[df["Retention time RoundOff (min)"].duplicated()]
    
        means = DF.groupby("Retention time RoundOff (min)")[data_top].mean()
        means.to_csv('q3.csv',index=False)    
        zip_file_list = ['q3.csv']
        download_file = io.BytesIO()
        with ZipFile(download_file,'w') as zip_file:
            for csv_file in zip_file_list:
                zip_file.write(csv_file)
                os.remove(csv_file) 
        response = HttpResponse(download_file.getvalue(),content_type='application/octet-stream')		
        response['Content-Disposition'] = 'attachment; filename="Q3_output.zip"'
                
        return response

    return render(request,render_html)