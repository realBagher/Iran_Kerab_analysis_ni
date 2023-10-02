import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sh@0831@Sh',
    database='irabketab_db'
)
mycursor = database.cursor()


sql1 = "Select count(book_id) as count, category_name from book_category inner join category on book_category.category_id=category.id group by category_id"
df_book1 = pd.read_sql_query(sql1, database)

if mycursor:
    df = pd.DataFrame(df_book1, columns=["count", "category_name"])
    st.bar_chart(df.set_index('category_name'), use_container_width=True)
##2
sql2 = "SELECT COUNT(book.book_id) AS numbook_pub, publisher.publisher_name FROM book INNER JOIN publisher ON book.publisher_id = publisher.id GROUP BY publisher.id ORDER BY numbook_pub DESC LIMIT 10"
df_book2 = pd.read_sql_query(sql2, database)

if mycursor:
    df = pd.DataFrame(df_book2, columns=["numbook_pub", "publisher_name"])
    st.bar_chart(df.set_index('publisher_name'), use_container_width=True)

##3
sql3 = "SELECT COUNT(book_id) AS numbook_year, release_date_sh FROM book GROUP BY release_date_sh ORDER BY release_date_sh DESC"
df_book3 = pd.read_sql_query(sql3, database)

if mycursor:
    df = pd.DataFrame(df_book3, columns=["numbook_year", "release_date_sh"])
    st.line_chart(df.set_index('release_date_sh'), use_container_width=True)

##4
sql4 = "SELECT COUNT(book_id) AS numbook_author, person.person_name FROM book_author INNER JOIN person ON book_author.person_id = person.id GROUP BY person.id ORDER BY numbook_author DESC LIMIT 10 OFFSET 1"
df_book4 = pd.read_sql_query(sql4, database)
if mycursor:
    df = pd.DataFrame(df_book4, columns=["numbook_author", "person_name"])
    
    st.bar_chart(df.set_index('person_name'), use_container_width=True)


sql5 = "SELECT COUNT(book_id) AS numbook_translator, person.person_name FROM book_translator INNER JOIN person ON book_translator.person_id = person.id GROUP BY person.id ORDER BY numbook_translator DESC LIMIT 10 OFFSET 2"
df_book5 = pd.read_sql_query(sql5, database)
if mycursor:
    df = pd.DataFrame(df_book5, columns=["numbook_translator", "person_name"])
    st.bar_chart(df.set_index('person_name'), use_container_width=True)

##6
sql6 = "SELECT book_id, book_pages, release_date_sh FROM book"
df_book6 = pd.read_sql_query(sql6, database)

if mycursor:
    df = pd.DataFrame(df_book6, columns=["book_pages", "release_date_sh"])
    
    fig, ax = plt.subplots(figsize=(20, 5))
    ax.scatter(df["release_date_sh"], df["book_pages"])
    ax.set_xlabel("Date of Publish")
    ax.set_ylabel("Book Pages")
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

##7
sql7 = "SELECT book_id, original_price, release_date_sh FROM book"
df_book7 = pd.read_sql_query(sql7, database)
if mycursor:
    df = pd.DataFrame(df_book7, columns=["original_price", "release_date_sh"])
    fig, ax = plt.subplots(figsize=(20, 5))
    ax.scatter(df["release_date_sh"], df["original_price"])
    ax.set_xlabel("Date of Publish")
    ax.set_ylabel("Book Original Price")
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)
##8
sql8 = "Select book_id, original_price, rating from book "

df_book8 = pd.read_sql_query(sql8, database)
if mycursor:
    df = pd.DataFrame(df_book8, columns=["original_price" , "rating"])
    fig ,ax = plt.subplots(figsize=(20,5))
    ax.scatter(df["rating"], df["original_price"])
    st.pyplot(fig)

##9
sql9 = "SELECT COUNT(book_id) AS numbook_print_type, size.size_name FROM size INNER JOIN book ON size.id = book.size_id GROUP BY size_id"
df_book9 = pd.read_sql_query(sql9, database)
if mycursor:
    df = pd.DataFrame(df_book9, columns=["numbook_print_type", "size_name"])
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(df["numbook_print_type"], labels=df["size_name"], autopct='%1.1f%%', startangle=140)
    ax.set_title("Distribution of Book Sizes")

    st.pyplot(fig)
