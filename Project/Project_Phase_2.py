import streamlit as st
from PIL import Image
import pickle
import pandas as pd
import math
from sklearn.cluster import KMeans
import random
st.write("""
<style>
.big-font {
    font-size:100px !important;
}
</style>
""", unsafe_allow_html=True)

def run():
    df=pd.read_excel("Clustered.xlsx")
    df['Wr']=df['Wr'].replace([30,20,10,3,2,1],[0.3,0.2,0.1,0.03,0.02,0.01])
    st.title("Movie recommendation system")
    x = df[['Wd','Wa','Wg','Wy','Wr']]
    kmeans = KMeans(3,random_state=42)
    kmeans.fit(x)
    identified_clusters = kmeans.fit_predict(x)
    IC=list(identified_clusters)
    cluster1,cluster2,cluster3=[],[],[]
    for i in range(0,len(IC)):
        IC[i] = int(IC[i])
        if IC[i] == 0:
            cluster1.append(i)
        if IC[i] == 1:
            cluster2.append(i) 
        if IC[i] == 2:
            cluster3.append(i)
    Cluster1=df.iloc[cluster1]
    Cluster2=df.iloc[cluster2]
    Cluster3=df.iloc[cluster3]
    name1 = st.text_input('enter the name of movie')
    if(len(name1)==0):
        st.warning('Please enter the movie name')
        st.stop()
    name1=name1.split(',')
    l=[]
    flag=0
    for i in name1:
        for index,rows in df.iterrows():
            if i.lower() == rows['original_title'].lower():
                l.append(rows)
                flag=1
    if flag ==0:
        st.write("No Movies are Available to recommend you")
        return 0
    df1=pd.DataFrame(l)
    print(df1)
    p1=df1['Cluster'].value_counts()
    p1=p1.to_frame()
    p1.reset_index(inplace = True)
    if len(p1)==1:
        Clusternumber=p1.loc[0,'index']
    if len(p1)==2:
        l1=[int(p1.loc[0,'index']),int(p1.loc[1,'index'])]
        Clusternumber=l1.index(max(l1))
    if len(p1)==3:
        l1=[int(p1.loc[0,'index']),int(p1.loc[1,'index']),int(p1.loc[2,'index'])]
        Clusternumber=l1.index(max(l1))
    Movies=df1[['Wd','Wa','Wg','Wy','Wr']]
    if Clusternumber==0:
        t=Cluster1
        Total=Cluster1[['Wd','Wa','Wg','Wy','Wr']]
    if Clusternumber==1:
        t=Cluster2
        Total=Cluster2[['Wd','Wa','Wg','Wy','Wr']]
    if Clusternumber==2:
        t=Cluster3
        Total=Cluster3[['Wd','Wa','Wg','Wy','Wr']]
    recommend=[]
    for index,rows in Movies.iterrows():
        for index1,rows1 in Total.iterrows():
            a=rows1['Wd']*rows['Wd'] + rows1['Wa']*rows['Wa'] + rows1['Wg']*rows['Wg'] + rows1['Wr']*rows['Wa']
            ar=math.sqrt(rows['Wd']*rows['Wd']+rows['Wa']*rows['Wa'] + rows['Wg']*rows['Wg'] + rows['Wr']*rows['Wr'])
            br=math.sqrt(rows1['Wd']*rows1['Wd']+rows1['Wa']*rows1['Wa'] + rows1['Wg']*rows1['Wg'] + rows1['Wr']*rows1['Wr'])
            sim =a/(ar*br)
            if sim > 0.57:
                recommend.append(index1)
    st.write("the recommended movies for you are:")
    Recommended_Movies=df['original_title'].iloc[list(set(recommend))]
    
    Recommended_Movies=Recommended_Movies.to_frame()


    Recommended_Movies.reset_index(inplace = True)
    a=[]
    if len(Recommended_Movies) >= 5:
        for i in range(0,5):
            a1=random.randint(0,len(Recommended_Movies))
            a.append(a1)
        a2=t.iloc[a]
        st.write(a2['original_title'])
    else:
        st.write(Recommended_Movies['original_title'])   
run()