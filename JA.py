import jenkins
jenkins_url = 'http://globegatepmx/Citrix/Web/'
# Create server
server = Jenkins(jenkins_url, username='yuktal', password='Amdocs@2023')
# Check job and print description
#for job_name, job_instance in server.get_jobs():
 #   if job_name == "testjob":
  #      print('Job Name:%s' % job_instance.name)
   #     print('Job Description:%s' % (job_instance.get_description()))

# Trigger job
#params = {'a':1, 'b':2, 'c': True}
#server.build_job("testjob", params)
# HOW do I get the result of this job???jenkins_url = 'http://myjenkins_host:8080'   
# Create server
server = Jenkins(jenkins_url, username='user', password='123456789abcdef')
# Check job and print description
for job_name, job_instance in server.get_jobs():
    if job_name == "testjob":
        print('Job Name:%s' % job_instance.name)
        print('Job Description:%s' % (job_instance.get_description()))

# Trigger job
params = {'a':1, 'b':2, 'c': True}
server.build_job("testjob", params)
# HOW do I get the result of this job???
