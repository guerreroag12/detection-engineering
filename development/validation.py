import tomllib
import sys
import os
    
#file = "alert_example.toml"
#with open(file,"rb") as toml:
#alert = tomllib.load(toml)

for root, dirs, files in os.walk("C:\\Users\\alexs\\Documents\\Code\\Detection Engineering\\converted_detections"):
    for file in files:
        if file.endswith(".toml"):
            full_path = os.path.join(root, file)
            with open(full_path,"rb") as toml:
                alert = tomllib.load(toml)
    
                present_fields = []
                missing_fields = []

                if alert['rule']['type'] == "query": # query based alert
                    required_fields = ['description', 'name', 'rule_id', 'risk_score', 'severity', 'type', 'query']
                elif alert['rule']['type'] == "eql": # event correlation alert
                    required_fields = ['description', 'name', 'rule_id', 'risk_score', 'severity', 'type', 'query', 'language']
                elif alert['rule']['type'] == "threshold": # threshold based alert
                    required_fields = ['description', 'name', 'rule_id', 'risk_score', 'severity', 'type', 'query', 'threshold']
                else:
                    print(f"Unsupported rule type found in {full_path}")
                    break

                for table in alert:    
                    for field in alert[table]:
                        present_fields.append(field)

                for field in required_fields:
                    if field not in present_fields:
                        missing_fields.append(field)
                        
                if missing_fields:
                    print(f'The following fields do not exist in {file}: {missing_fields}')
                else: 
                    print(f"Validation passed for: {file}!")