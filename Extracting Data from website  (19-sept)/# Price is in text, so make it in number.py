# Price is in text, so make it in number
def text_to_number(text_with_commas):
    # Remove commas from the text
    text_without_commas = text_with_commas.replace(',', '')
    numeric_value = float(text_without_commas)
    return numeric_value