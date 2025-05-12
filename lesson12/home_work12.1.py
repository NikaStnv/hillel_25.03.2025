import re


def edit_file(file_path):
    """ Очищення тексту від html-тегів та порожні рядки"""
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        edit1_content = re.sub(r'<[^>]+>', '', content)
        edit2_content = [line for line in edit1_content.splitlines() if line.strip() != ""]

    cleaned_file = "cleaned.txt"
    with open(cleaned_file, "w", encoding="utf-8") as file:
        file.write("\n".join(edit2_content))
    return True


path = r"C:\Users\Admin\PycharmProjects\Hillel_Basic\hillel_25.03.2025\lesson12\draft.html"
edit_file(path)



import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
      with codecs.open(html_file, 'r', 'utf-8') as file:
           html = file.read()
