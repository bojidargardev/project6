import streamlit as st

st.title("Библиотека")
if "books" not in st.session_state:
    st.session_state.books = []
st.header("Добави книга")
title = st.text_input("Заглавие")
author = st.text_input("Автор")
price = st.number_input("Цена", min_value=0.0)
if st.button("Добави книга"):
    book = {
        "title": title,
        "author": author,
        "price": price
    }
    st.session_state.books.append(book)
    st.success("Книгата е добавена!")
if st.button("Покажи всички книги"):
    if len(st.session_state.books) == 0:
        st.write("Няма добавени книги.")
    else:
        for book in st.session_state.books:
            st.write("Заглавие:", book["title"])
            st.write("Автор:", book["author"])
            st.write("Цена:", book["price"])
            st.write("--------------------")
st.header("Търсене по автор")
search_author = st.text_input("Въведи името на автор")
if st.button("Търси по автор"):
    found = False
    for book in st.session_state.books:
        if book["author"] == search_author:
            st.write(book)
            found = True

    if not found:
        st.write("Няма намерени книги на този автор.")
st.header("Търсене по заглавие")
search_title = st.text_input("Въведете заглавие:")

if st.button("Търси по заглавие"):
    found = False
    for book in st.session_state.books:
        if book["title"] == search_title:
            st.write(book)
            found = True

    if not found:
        st.write("Няма намерена такава книга.")
if st.button("Покажи най-евтината книга"):
    if len(st.session_state.books) == 0:
        st.write("Няма книги.")
    else:
        cheapest = st.session_state.books[0]
        for book in st.session_state.books:
            if book["price"] < cheapest["price"]:
                cheapest = book
        st.write("Най-евтината книга е:")
        st.write(cheapest)
