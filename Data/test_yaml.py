import yaml

with open("../Data/search.yaml",'r') as f:
    data = yaml.load(f)
    print(type(data))
    print(data)


with open('../Data/write1.yaml','w') as f:
    data = {'Search_Data':{
                    'search_test_002':{'expect':{'value':'你好'},'value':'你好'},
                    'search_test_001':{'expect':[4,5,6],'value':456}}}
    #yaml.dump(data,f,encoding='utf-8',allow_unicode=True)
    yaml.dump(data,f)