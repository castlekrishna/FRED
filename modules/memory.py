import json

project_memory = "data/project_memory.json"


#loads project data from memory
def load_project_memory():
    try:
        with open(project_memory,"r") as f:
            records = json.load(f)
            return records
    except:
        print("File not found")

# saves project memory
def save_project_memory(data):
    with open(project_memory,"w") as f:
            json.dump(data,f,indent=4)

#update current feature in memory
def update_current_feature(project, feature):
     data = load_project_memory()
     current = data["projects"][project]["features"]["current"]
     data["projects"][project]["features"]["completed"].append(current)
     data["projects"][project]["features"]["current"] = feature

     save_project_memory(data)

# format the records to print in a good way
def format_records(project,records):
     features = records['projects'][project]["features"]
     output = f"""
Project = {project}
Status = {records['projects'][project]['status']}

Current Feature : 
- {features['current']}

Completed Feature :
{"\n".join(features['completed'])}

Upcoming Features :
{chr(10).join(features['upcoming'])}
"""
     return output