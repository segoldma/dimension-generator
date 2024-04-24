from loadJSON import load_json
from extractCatalogInfo import extract_catalog_info
from extractManifestInfo import extract_manifest_info
from mergeDictionaries import merge_dictionaries
from convertModelToLookML import convert_model_to_lookml
import lkml
import json


manifest_path = 'manifest.json'
catalog_path = 'catalog.json'

manifest_data = load_json(manifest_path)
catalog_data = load_json(catalog_path)

manifest_dict = extract_manifest_info(manifest_data)
catalog_dict = extract_catalog_info(catalog_data)

combined_dict = merge_dictionaries(manifest_dict, catalog_dict)

# Add a filename here and run
model_name = ''

lookml_data = convert_model_to_lookml(combined_dict, model_name)

for lookml_entry in lookml_data:
    print(lkml.dump(lookml_entry))

