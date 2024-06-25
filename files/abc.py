entity = {
    "content": {
        "id": "1381025",
        "type": "page",
        "status": "current",
        "title": "Page 936",
        "space": {
            "id": 1572876,
            "key": "SPACE111",
            "name": "Space 111",
            "type": "global",
            "_links": {
                "webui": "/display/SPACE111",
                "self": "http://103.108.207.59:9685/rest/api/space/SPACE111",
            },
            "_expandable": {
                "metadata": "",
                "icon": "",
                "description": "",
                "retentionPolicy": "",
                "homepage": "/rest/api/content/1380088",
            },
        },
        "history": {
            "latest": True,
            "createdBy": {
                "type": "known",
                "username": "admin",
                "userKey": "8ab28a638dd55254018dd5537bb60000",
                "profilePicture": {
                    "path": "/images/icons/profilepics/default.svg",
                    "width": 48,
                    "height": 48,
                    "isDefault": True,
                },
                "displayName": "Confluence Admin",
                "_links": {
                    "self": "http://103.108.207.59:9685/rest/api/user?key=8ab28a638dd55254018dd5537bb60000"
                },
                "_expandable": {"status": ""},
            },
            "createdDate": "2024-02-27T15:19:06.032+05:30",
            "_links": {
                "self": "http://103.108.207.59:9685/rest/api/content/1381025/history"
            },
            "_expandable": {
                "lastUpdated": "",
                "previousVersion": "",
                "contributors": "",
                "nextVersion": "",
            },
        },
        "container": {
            "id": 1572876,
            "key": "SPACE111",
            "name": "Space 111",
            "type": "global",
            "_links": {
                "webui": "/display/SPACE111",
                "self": "http://103.108.207.59:9685/rest/api/space/SPACE111",
            },
            "_expandable": {
                "metadata": "",
                "icon": "",
                "description": "",
                "retentionPolicy": "",
                "homepage": "/rest/api/content/1380088",
            },
        },
        "body": {
            "storage": {
                "value": "<p>This is a sample page.</p>",
                "representation": "storage",
                "_expandable": {"content": "/rest/api/content/1381025"},
            },
            "_expandable": {
                "editor": "",
                "view": "",
                "export_view": "",
                "styled_view": "",
                "anonymous_export_view": "",
            },
        },
        "extensions": {"position": "none"},
        "_links": {
            "webui": "/display/SPACE111/Page+936",
            "edit": "/pages/resumedraft.action?draftId=1381025",
            "tinyui": "/x/oRIV",
            "self": "http://103.108.207.59:9685/rest/api/content/1381025",
        },
        "_expandable": {
            "metadata": "",
            "operations": "",
            "children": "/rest/api/content/1381025/child",
            "restrictions": "/rest/api/content/1381025/restriction/byOperation",
            "ancestors": "",
            "version": "",
            "descendants": "/rest/api/content/1381025/descendant",
        },
    },
    "title": "Page 936",
    "excerpt": "This is a sample page.",
    "url": "/display/SPACE111/Page+936",
    "resultGlobalContainer": {
        "title": "Space 111",
        "displayUrl": "/display/SPACE111",
    },
    "entityType": "content",
    "iconCssClass": "aui-icon content-type-page",
    "lastModified": "2024-02-27T15:19:06.032+05:30",
    "friendlyLastModified": "Feb 27, 2024",
    "timestamp": 1709027346032,
}
def nested_get_from_dict(dictionary, keys, default=None):
    def nested_get(dictionary_, keys_, default_=None):
        if dictionary_ is None:
            return default_

        if not keys_:
            return dictionary_

        if not isinstance(dictionary_, dict):
            return default_
        return (dictionary_.get(keys_[0]), keys_[1:], default_)
    return nested_get(dictionary, keys, default)

a = nested_get_from_dict(entity, ['content','history'])
print(a)