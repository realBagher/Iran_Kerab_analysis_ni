import streamlit as st
import mysql.connector
import pandas as pd


database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sh@0831@Sh',
    database='irabketab_db'
)
mycursor = database.cursor()
st.header("جست و جو پیشرفته")
show_book = st.checkbox('نام کتاب')
if show_book:
    book_name = st.text_input(label='', placeholder='نام کتاب')
else:
    book_name = ''
show_trans = st.checkbox('نام نویسنده')
if show_trans:
    writer_name = st.text_input(label='', placeholder='نام نویسنده')
else:
    writer_name = ''
show_publisher = st.checkbox('نام ناشر')
if show_publisher:
    publisher_name = st.text_input(label='', placeholder='نام ناشر')
else:
    publisher_name = ''
query_for_size = 'SELECT distinct size_name from size\
                  join book on book.size_id = size.id'
mycursor.execute(query_for_size)
available_type_of_size = [result[0] for result in mycursor.fetchall()]
st.markdown("<hr>", unsafe_allow_html=True)
type_of_size = st.checkbox('سایز کتاب')
if type_of_size:
    select_type_of_size = st.selectbox('', available_type_of_size)
else:
    select_type_of_size = ''
st.markdown("<hr>", unsafe_allow_html=True)
query_for_type = 'SELECT distinct type_of_print from type_of_print\
         join book on book.type_of_print_id = type_of_print.id'
mycursor.execute(query_for_type)
available_type_of_jeld = [result[0] for result in mycursor.fetchall()]
type_of_jeld = st.checkbox('نوع جلد')
if type_of_jeld:
    select_type_of_jeld = st.selectbox('', available_type_of_jeld)
else:
    select_type_of_jeld = ''
st.markdown("<hr><h5>موجودی</h5>", unsafe_allow_html=True)
inventory_option = st.radio('', ('موجود', 'ناموجود',), horizontal=True)
range_price = st.checkbox("محدوده قیمت")
if range_price:
    price_range = st.slider("محدوده قیمت", min_value=10000.0, max_value=10000000.0, step=1.0, value=(10000.0, 10000000.0))
else:
    price_range = None
range_count_page = st.checkbox("تعداد صفحه")
if range_count_page:
    page_number_range = st.slider("تعداد صفحه", min_value=10.0, max_value=10000.0, step=5.0, value=(10.0, 10000.0))
else:
    page_number_range = None
rate = st.checkbox("محدوده امتیاز")
if rate:
   rating_range = st.slider("محدوده امتیاز", min_value=0.0, max_value=5.0, step=1.0, value=(0.0, 5.0))
else:
    rating_range = None
if st.button("Search"):
    query = """SELECT distinct product_name, product_name_eng, isbn, release_date_sh, release_date_gc,person.person_name, publisher.publisher_name, rating, print_series,
            CASE WHEN inventory = 0 THEN "ناموجود" ELSE "موجود" END as inventory,
            CASE WHEN original_price = 0 THEN "نامعلوم" ELSE original_price END as original_price,
            CASE WHEN discount_percent = 0 THEN "نامعلوم" ELSE discount_percent END as discount_percent,
            CASE WHEN discount_price = 0 THEN "نامعلوم" ELSE discount_price END as discount_price
            FROM book join book_author on book_author.book_id = book.book_id join person on book_author.person_id = person.id JOIN publisher ON publisher.id = book.publisher_id JOIN type_of_print ON type_of_print.id = book.type_of_print_id JOIN size ON size.id = book.size_id WHERE  """

    conditions = []

    if book_name:
        conditions.append(f"product_name LIKE '%{book_name}%'")
    if writer_name:
        conditions.append(f"person_name LIKE '%{writer_name}%'")
    if publisher_name:
        conditions.append(f"publisher_name LIKE '%{publisher_name}%'")
    if select_type_of_size:
        conditions.append(f"size.size_name like '%{select_type_of_size}%'")
    if select_type_of_jeld:
        conditions.append(f"type_of_print.type_of_print LIKE '%{select_type_of_jeld}%'")
    if inventory_option:
        if inventory_option == 'موجود':
            conditions.append("inventory = 1")
        else:
            conditions.append("inventory = 0")
    if price_range:
        min_price, max_price = price_range
        conditions.append(f"original_price between {min_price} AND {max_price}")
    if page_number_range:
        min_page_number, max_page_number = page_number_range
        conditions.append(f'book_pages between {min_page_number} AND {max_page_number}')
    if rating_range:
        min_rate, max_rate = rating_range
        conditions.append(f'rating between {min_rate} AND {max_rate}')


    query += " AND ".join(conditions) if conditions else " 1=1 "

    query += f' LIMIT 20'

    mycursor.execute(query)

    results = mycursor.fetchall()

    if results:
            dataframe = pd.DataFrame(
                results,
                columns=['نام کتاب', 'نام انگلیسی کتاب', 'شابک', 'تاریخ شمسی', 'تاریخ میلادی','نام نویسنده' , 'نام ناشر', 'امتیاز', 'تعداد چاپ',
                        'موجودی', 'قیمت اصلی', 'درصد تخفیف', 'قیمت بعد تخفیف'])
            st.table(dataframe)
    else:
        st.warning("کتابی یافت نشد")

















