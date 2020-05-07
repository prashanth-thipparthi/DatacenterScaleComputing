# Steps:
1. Clone the repository given in the moodle writeup.

# Part 1:

1. I utilised google cloud python compute apis, create_instance.py (https://github.com/GoogleCloudPlatform/python-docs-samples) as a base code to complete my part 1.
2. I created a shell script file to pull the git repo, install dependencies and flask and finally execute it.
3. In part1, I first wrote a api to create a firewall rule to open port 5000 for the flask application.
4. In the next step, I created the instance by forming the body to the create_instance api call and also passed the shell script file in the metadata part of the api call to execute the shell script as a start up script.
5. In the next step I waited for the operation to be dome and extracted the external ip of the instance and printed the url of the flask application.


# Part2:
1. At first, I listed the instance which created in the step 1.
2. Created a snapshot of the instance disk.
3. Started the timer before creating each instance and recorded at the end of the instance creation.
4. Finally wrote all the timings to a file.


# Part3:
1. I have two stages like stage 1 and stage2.
2. Associated with stage1 , there is a shell script startup-script1.sh, in which we will pull the code from the git repo and start the stage2.
3. Stage2 is same as the part1 where we create the machine deploy the flsk application in the machine.

