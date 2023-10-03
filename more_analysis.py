import streamlit as st
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sh@0831@Sh',
    database='irabketab_db'
)
mycursor = database.cursor()


text1 = """به صورت کلی اگر هزینه‌های مربوط به دستمزد نویسنده یا مترجم، هزینه‌های اداری، و مجوز را کنار بگذاریم، اصلی‌ترین هزینه چاپ یک کتاب مربوط به چاپ آن است. در نتیجه اگر قیمت با تخفیف یک کتاب را بر تعداد صفحه آن تقسیم کنیم، میانگین درآمد ناشر بر روی هر صفحه آن کتاب بدست می‌آید. هزینه چاپ هر صفحه به قطع آن کتاب بستگی دارد و همچنین به نوع جلد و کیفیت کاغذ بستگی دارد. در اینجا دو مورد اول را در اختیار داریم. در این بخش به صورت کلی به دنبال آن هستیم از یک سو با داشتن میزان محبوبیت کتاب که اساسی‌ترین معیار آن امتیاز دریافتی است و از سوی دیگر قیمت فروش بر هر صفحه، بهترین ژانر و نوع کتاب را با توجه به شرایط و ویژگی‌های یک ناشر مشخص کنیم. در واقع تصویری به ناشر ارائه دهیم که تغییرات قیمت کتاب نسبت به امتیاز و دیگر معیارهای محبوبیت کتاب بسته به تغییر دسته‌بندی محتوایی کتاب، نوع جلد، قطع، خارجی‌بودن یا نبودن، ناشر و تعداد تجدید چاپ؛ چگونه تغییر می‌کند.  """
st.markdown(text1)
text2 = """در اولین گام در این مسیر، سه تحلیل زیر را بر پایه داده‌های استخراج‌شده از سایت ایران کتاب ارائه می‌دهیم. تحلیل اول و دوم به دنبال بررسی ناهمگنی تغییر رفتارهای قیمتی نسبت به امتیاز در انواع قطع، جلد و دسته‌بندی است. در تحلیل سوم با الگوگیری از معیار تمرکز صنایع و سهم هر ناشر در هر یک از دسته‌بندی‌های موضوعی کتاب، میزان رقابتی‌بودن هر موضوع را بدست آورده و اثر آن بر میانگین قیمت هر صفحه کتاب در آن موضوع را مشاهده کنیم. 
"""
st.markdown(text2)
st.header('تحلیل اول ')
text3 = """متغیر قیمت تقسیم بر تعداد صفحه با تغییر مقدار امتیاز """
st.markdown(text3)

sen_sql1 = "Select discount_price, book_pages ,product_name , rating  from book inner join size on book.size_id=size.id inner join type_of_print on book.type_of_print_id=type_of_print.id LIMIT 100"
sen_df1 = pd.read_sql_query(sen_sql1, database)
sen_df1['priceofonepage'] = sen_df1['discount_price']/sen_df1['book_pages']
plt.figure(figsize=(10, 6))
plt.bar(sen_df1['rating'], sen_df1['priceofonepage'])
plt.xlabel('Book Title')
plt.ylabel('Price per Page')
plt.title('Price per Page for Books')
plt.xticks(rotation=90) 
st.pyplot(plt)




