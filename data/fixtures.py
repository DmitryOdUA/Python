def get_issue_json(summary: str):
    return {
        "fields": {
            "project": {
                "id": "10903"
            },
            "summary": summary,
            "description": "Some description",
            "issuetype": {
                "name": "Bug"
            }
        }
    }
