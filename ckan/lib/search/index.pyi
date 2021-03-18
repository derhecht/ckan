
import string
import re
import six
from ckan.model import PackageRelationship


TYPE_FIELD = "entity_type"
PACKAGE_TYPE = "package"
KEY_CHARS = string.digits + string.ascii_letters + "_-"
SOLR_FIELDS = [TYPE_FIELD, "res_url", "text", "urls", "indexed_ts", "site_id"]
RESERVED_FIELDS = SOLR_FIELDS + [
    "tags",
    "groups",
    "res_name",
    "res_description",
    "res_format",
    "res_url",
    "res_type",
]
RELATIONSHIP_TYPES = PackageRelationship.types

def escape_xml_illegal_chars(val, replacement=...):
    ...

def clear_index(): ...

class SearchIndex(object):

    def __init__(self) -> None: ...
    def insert_dict(self, data):
        ...
    def update_dict(self, data):
        ...
    def remove_dict(self, data):
        ...
    def clear(self):
        ...
    def get_all_entity_ids(self):
        ...

class NoopSearchIndex(SearchIndex): ...

class PackageSearchIndex(SearchIndex):
    def remove_dict(self, pkg_dict): ...
    def update_dict(self, pkg_dict, defer_commit=...): ...
    def index_package(self, pkg_dict, defer_commit=...): ...
    def commit(self): ...
    def delete_package(self, pkg_dict): ...
