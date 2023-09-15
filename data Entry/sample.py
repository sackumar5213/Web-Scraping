def text_to_number(text_with_commas):
    # Remove commas from the text
    text_without_commas = text_with_commas.replace(',', '')
    
    try:
        # Convert the text to a numeric value (float)
        numeric_value = float(text_without_commas)
        return numeric_value
    except ValueError:
        # Handle the case where the text cannot be converted to a number
        return None  # Or raise an exception or return an error message

# Example usage:
text = "45,12,58,62"
result = text_to_number(text)
if result is not None:
    print("Numeric Value:", result)
else:
    print("Invalid input, cannot convert to a number.")
