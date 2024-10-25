import mysql.connector
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class Show_Data:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='db-robopark.crtxsdecqcur.us-east-1.rds.amazonaws.com',
            user='admin',
            password='Boss1all23',
            database='mydb'
        )
        # self.conn = sql.connect("face_data.db")
        self.cursor = self.conn.cursor()
    def show_age_bar(self):
        plt.clf()
        query = "SELECT usia FROM person"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        data_list = [item[0] for item in data]
        data_df = pd.DataFrame(data_list, columns=['age'])

        data_counts = data_df.value_counts().reset_index()
        data_counts.columns = ['age', 'count']

        sns.barplot(x="age", y="count", data=data_counts)
        plt.xticks(rotation=90)
        plt.title("Age Bar Chart")
        plt.xlabel("Age")
        plt.ylabel("Count")
        return plt
    def show_age_pie(self):
        plt.clf()
        query = "Select usia from person "
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        data_list = [item[0] for item in data]
        data_df = pd.DataFrame(data_list, columns=['age'])

        data_counts = data_df.value_counts().reset_index()
        data_counts.columns = ['age', 'count']
        plt.title("Age Pie Chart")
        plt.pie(data_counts["count"], labels = data_counts["age"])
        return plt
    def show_emotion_bar(self):
        plt.clf()
        query = "Select emotion from person"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        data_list = [item[0] for item in data]
        data_df = pd.DataFrame(data_list, columns=['emotion'])

        data_counts = data_df.value_counts().reset_index()
        data_counts.columns = ['emotion', 'count']

        sns.barplot(x="emotion", y="count", data=data_counts)
        plt.title("Emotion Distribution")
        plt.xlabel("Emotion")
        plt.ylabel("Count")
        return plt
    def show_emotion_pie(self):
        plt.clf()
        query = "Select emotion from person"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        data_list = [item[0] for item in data]
        data_df = pd.DataFrame(data_list, columns=['emotion'])

        data_counts = data_df.value_counts().reset_index()
        data_counts.columns = ['emotion', 'count']

        sns.barplot(x="emotion", y="count", data=data_counts)
        plt.title("Emotion Distribution")
        plt.xlabel("Emotion")
        plt.ylabel("Count")
        return plt

    def show_gender_bar(self):
        plt.clf()
        query = "Select gender from person"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        data_list = [item[0] for item in data]
        data_df = pd.DataFrame(data_list, columns=['gender'])

        data_counts = data_df.value_counts().reset_index()
        data_counts.columns = ['gender', 'count']

        sns.barplot(x="gender", y="count", data=data_counts)
        plt.title("Gender Distribution")
        plt.xlabel("Gender")
        plt.ylabel("Count")
        return plt

    def show_gender_pie(self):
        plt.clf()
        query = "Select gender from person"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        data_list = [item[0] for item in data]
        data_df = pd.DataFrame(data_list, columns=['gender'])

        data_counts = data_df.value_counts().reset_index()
        data_counts.columns = ['gender', 'count']
        plt.title("Gender Pie Chart")
        plt.pie(data_counts["count"], labels=data_counts["gender"])
        return plt

    def show_age_emotion_bar(self):
        plt.clf()
        query = "Select usia, emotion from person"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        data_df = pd.DataFrame(data, columns=['age', 'emotion'])

        data_counts = data_df.groupby(['age', 'emotion']).size().reset_index(name='count')
        data_counts.columns = ['age', 'emotion', 'count']

        sns.barplot(x="emotion", y="count", hue="age", data=data_counts)
        plt.xticks(rotation=90)
        plt.title("Emotion & Age Distribution")
        plt.xlabel("Age & Emotion")
        plt.ylabel("Count")
        return plt
    def show_age_gender_bar(self):
        plt.clf()
        query = "Select usia, gender from person"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        data_df = pd.DataFrame(data, columns=['age', 'gender'])

        data_counts = data_df.groupby(['age', 'gender']).size().reset_index(name='count')
        data_counts.columns = ['age', 'gender', 'count']

        sns.barplot(x="age", y="count", hue="gender", data=data_counts)
        plt.xticks(rotation=90)
        plt.title("Age & Gender Distribution")
        plt.xlabel("Age & Gender")
        plt.ylabel("Count")
        return plt
    def show_emotion_gender_bar(self):
        plt.clf()
        query = "Select emotion, gender from person"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        data_df = pd.DataFrame(data, columns=['emotion', 'gender'])

        data_counts = data_df.groupby(['emotion', 'gender']).size().reset_index(name='count')
        data_counts.columns = ['emotion', 'gender', 'count']

        sns.barplot(x="emotion", y="count", hue="gender",data=data_counts)
        plt.title("Emotion & Gender Distribution")
        plt.xlabel("Gender & Emotion")
        plt.ylabel("Count")
        return plt

    def show_all_data(self):
        query = "select * from person"
        data_all = self.cursor.execute(query).fetchall()
        return data_all

