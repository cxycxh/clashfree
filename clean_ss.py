import yaml

with open('clash.yml', 'r',encoding="utf-8") as f:
    clash_profile = yaml.safe_load(f)
    
proxies = clash_profile['proxies']

if not proxies:
    print("None!")