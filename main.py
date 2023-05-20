from googletrans import Translator
import streamlit as st

st.title('Да, они действительно настолько похожи! :pencil:')

st.markdown("Ты должен был слышать, **насколько** похожи *романские* языки.")
st.markdown("Напомню, что *романские языки* — это группа языков и диалектов, входящих в италийскую ветвь "
            "индоевропейской языковой семьи и генетически восходящих к общему предку — вульгарной латыни."
            "Сюда входят **:red[французский, итальянский, испанский, португальский, "
            "румынский, молдавский, каталанский, провансальский,]** "
            "сардинский, рето-романский, македоно-румынский и мертвые латинский, "
            "оскский, умбрский и другие (так называемые италийские).")
st.markdown('Чтобы уж точно это показать, наш дорогой робот Чаппи  покажет тебе '
            'перевод любой фразы с русского на несколько романских языков сразу. :star:')

# source language
src = "ru"
# target languages
dst = ["es", "it", "fr", "pt", "ca", "la"]

form = st.form(key='my_form')
source = form.text_input(label="Напиши что-нибудь на русском:")
# reruns the code
submit_button = form.form_submit_button(label='Submit')

translator = Translator()

if submit_button:
    for lang in dst:
        result = translator.translate(source, dest=lang)
        st.write(result.dest, " > ", result.text)
