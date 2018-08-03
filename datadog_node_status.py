from datadog import initialize, api

options = {
    "api_key": "",
    "app_key": ""
}

initialize(**options)

x=api.Hosts.search()
#print(x)

def nodestatus():
    dict = {}
    temp1 = {}
    hostlist=x['host_list']

    for i in hostlist:
        for j in i['meta']['agent_checks']:
            temp1[j[0]]=j[3]
        dict[i['name']]=temp1
    return dict

def errornodes():
    nodestat=nodestatus()
    dash=False
    for key,value in nodestat.items():
        for i,j in value.items():
            if j!='OK':
                print(key,"\n",i," : ",j)
                dash=True
            if dash:
                print("=============================================================")
                dash=False

print(errornodes())
