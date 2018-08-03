import jenkins
server=jenkins.Jenkins('http://192.168.40.133:8080',username='jayabalan', password='keyboard92')
print server.get_jobs()
