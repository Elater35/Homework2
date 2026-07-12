# ДЗ 13.1. Очистити текст від html-тегів


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, 'r', encoding='utf-8') as file:
        html = file.read()


    def clean_html(html_text):
        if html_text.find("<") == -1:
            return html_text
        else:
            text = (html_text[:html_text.find("<")] + html_text[html_text.find(">") + 1:]).replace("  ", " ")
            return clean_html(text)


    with open(result_file, 'w', encoding='utf-8') as file_1:
        file_1.write(clean_html(html))


def delete_empty_str(cleaned_file, result_file_1='cleaned_res.txt'):
    with open(cleaned_file, 'r', encoding='utf-8') as file_1:
        draft_text = file_1.readlines() # для невеликих файлів використовуємо "readlines()"

    draft_text = [item for item in draft_text if item not in ("\n", " \n")]

    with open(result_file_1, 'w', encoding='utf-8') as file_2:
        file_2.write("".join(draft_text))


delete_html_tags("draft.html")
delete_empty_str("cleaned.txt")
