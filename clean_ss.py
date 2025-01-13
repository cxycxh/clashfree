import yaml

with open('tmp.yaml', 'w', encoding='utf-8') as tmp:
    with open('clash.yaml', 'r',encoding="utf-8") as f:
        for line in f:
            if '<' in line:
                continue
            else:
                tmp.write(line)

clash_profile = None
with open('tmp.yaml', 'r',encoding="utf-8") as f:
    clash_profile = yaml.safe_load(f)
    if clash_profile:
        proxies = clash_profile['proxies']
        proxy_groups = clash_profile['proxy-groups']
        
        ss_names = []
        if proxies:
            new_proxies = []
            for proxy in proxies:
                if proxy.get('cipher','')=='ss':
                    ss_names.append(proxy['name'])
                else:
                    new_proxies.append(proxy)
            clash_profile['proxies'] = new_proxies
        
        for group in proxy_groups:
            if group['proxies']:
                new_proxies = []
                for proxy in group['proxies']:
                    if proxy in ss_names:
                        continue
                    else:
                        new_proxies.append(proxy)
                group['proxies'] = new_proxies

with open('clash.yml', 'w',encoding="utf-8") as fw:
    yaml.dump(clash_profile, fw)



            
