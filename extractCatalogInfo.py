def extract_catalog_info(catalog_json):
    """
    Extract types from catalog.json and convert column names to lowercase.
    """
    result_dict = {}
    nodes = catalog_json.get('nodes', {})
    for node_key, node_value in nodes.items():
        node_name = node_value.get('metadata', {}).get('name').lower()  # Convert node names to lowercase for consistency
        columns = node_value.get('columns', {})
        column_type_info = {column_key.lower(): {"type": column_details.get('type')}
                            for column_key, column_details in columns.items()}  # Convert column keys to lowercase
        result_dict[node_name] = column_type_info
    return result_dict
