def merge_dictionaries(manifest_dict, catalog_dict):
    """
    Merge both dictionaries to include description, name, and type for each column that exists in both the manifest and catalog.
    Case-insensitive comparison is used to merge dictionaries based on node and column names.
    Only includes nodes and columns that exist in both dictionaries.
    """
    merged_dict = {}

    # Iterate through each node and column in the manifest
    for node_key, columns in manifest_dict.items():
        # Check if node exists in the catalog
        if node_key in catalog_dict:
            # Create a node entry in the merged dictionary if not exists
            if node_key not in merged_dict:
                merged_dict[node_key] = {}

            # Check each column in the manifest node if it exists in the catalog node
            for column_key in columns:
                if column_key in catalog_dict[node_key]:
                    # Merge description, name, and type for columns that exist in both
                    merged_dict[node_key][column_key] = {**manifest_dict[node_key][column_key], **catalog_dict[node_key][column_key]}

    return merged_dict
