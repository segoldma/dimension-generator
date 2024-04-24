def convert_model_to_lookml(data, model_name):
    """
    Converts a single model's columns into LookML format.

    Parameters:
        data (dict): A dictionary where the key is the model name and the value is a dictionary of columns.
        model_name (str): The name of the model to convert to LookML format.

    Returns:
        list: A list of LookML-formatted dictionaries for the specified model's columns.
    """
    lookml_columns = []

    # Define type mappings
    type_mapping = {
        "TEXT": "string",
        "TIMESTAMP_TZ": "time",
        "BOOLEAN": "yesno",
        "FLOAT": "number",
        "DATE": "date",
        "TIMESTAMP_NTZ": "time",
        "NUMBER": "number"
    }

    # Check if the model exists in the data
    if model_name in data:
        columns = data[model_name]
        for column_name, column_attrs in columns.items():
            column_type = column_attrs["type"]
            lookml_type = type_mapping.get(column_type, column_type.lower())
            description = column_attrs["description"]

            # Determine dimension type based on timestamp presence
            dimension_type = "dimension_group" if "TIMESTAMP" in column_type else "dimension"

            # Correct SQL formatting
            sql_formatted = f"${{TABLE}}." + f'"{column_name.upper()}"'

            # Create LookML column dictionary
            lookml_column = {
                dimension_type: {
                    "name": column_name,
                    "description": description,
                    "type": lookml_type,
                    "sql": sql_formatted
                }
            }

            # Append formatted column to list
            lookml_columns.append(lookml_column)
    else:
        raise ValueError(f"Model '{model_name}' not found in the provided data.")

    return lookml_columns
