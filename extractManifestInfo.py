def extract_manifest_info(manifest_json):
    """
    Extract descriptions from manifest.json and convert column names to lowercase.
    """
    result_dict = {}
    nodes = manifest_json.get('nodes', {})
    for node_key, node_value in nodes.items():
        alias = node_value.get('alias').lower()  # Convert alias to lowercase for consistency
        columns = node_value.get('columns', {})
        column_info = {column_key.lower(): {"description": column_details.get('description'), "name": column_details.get('name')}
                       for column_key, column_details in columns.items()}  # Convert column keys to lowercase
        result_dict[alias] = column_info
    return result_dict
