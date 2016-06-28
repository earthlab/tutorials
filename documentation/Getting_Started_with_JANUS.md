# Getting Started with Janus

### Background

What is a supercomputer and why is it necessary? A supercomputer is defined as a computer with a high-level computational capacity much greater in comparison to a general-purpose computer, hence the ‘super’ prefix. General-purpose computers can typically compute anywhere between 1-10 billion floating-point operations per second (FLOPS) whereas supercomputers can compute trillions or even quadrillions of FLOPS. In layman’s terms, this means that programs can run much quicker on a supercomputer due to the greater amount of FLOPS it can compute, this is especially useful for computation-heavy programs which may take hours or even days to run.

Fortunately, EarthLab has access to CU Boulder’s Research Computing supercomputer, JANUS. The JANUS supercomputer is comprised of 1,368 compute nodes, each containing 12 cores, for a total of 16,416 available cores and can achieve 184 trillion FLOPS. As a member of EarthLab, you have access to JANUS and are able to utilize, run jobs, and store files on this supercomputer. This document will walk you through the prerequisites necessary for using JANUS, logging into JANUS, and running jobs on JANUS.

### Authentication

It’s obviously important that JANUS is not open to the general public who may tamper with or use JANUS outside of programs such as EarthLab. Therefore, some form of authentication is necessary prior to logging into JANUS.

##### Getting an RC Account

1) Open up a web browser and head to the [RC Account Creation Page](https://portals.rc.colorado.edu/account/request/)

2) At the bottom of the screen, ensure 'University of Colorado - Boulder' is selected fom the dropdown box under 'Select your organization' and press 'Continue'

3) Provide your CU Boulder identikey username and password

4) Provide your proper University affiliation, enter 'EarthLab' for Organization/Department you represent, and ensure 'bash' is selected for 'Preferred login shell'

5) Click 'Submit Request'

##### Getting a Duo Account

1) Open up a web browser and head to the [Duo Signup Page](https://signup.duo.com/)

2) Provide your first name, last name, CU Boulder email address, mobile phone number, enter 'EarthLab' as Company/Account Name, and selecter 'Just me' from the final dropdown box

3) Check the Terms/Privacy Policy box and click 'Create My Account'

4) Download the Duo Mobile application on your smartphone

5) Ensure that notifications are enabled for the Duo Mobile application

5) Come into the ARC Building on East Campus to see Joel (6th floor, Room 679) with your CU Boulder photo ID card

6) Joel will then issue an email/text message/phone call to verify and finalize the two-step authentication setup process

### Logging into JANUS

Now that you properly have two-step authentication set up, you're ready to log into JANUS and begin using it.

##### Windows Users

1) Open up a web browser and head to the [Putty Download Page](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) and click 'putty.exe' under 'For Windows on x86 Intel'

2) Download, install, and open Putty

3) Click 'Session' from the list on the left side of the screen

4) Under 'Host Name (or IP address)' type 'login.rc.colorado.edu'

5) Click 'Data' under 'Connection; from the list on the left side of the screen

6) Under 'Login details' type your identikey username for 'Auto-login username'

7) Click 'Session' from the list again

8) Under 'Saved Sessions' type 'JANUS' and press 'Save'

9) Click 'JANUS' and press 'Open' on the bottom-right of the screen

10) A new window should pop up with the title 'login.rc.colorado.edu - PuTTY' with a prompt to enter your password

11) Enter 'duo:password' where password is your identikey password (do not include the single quotation marks) and press 'Enter'

12) You should receive a notification on your smartphone from Duo

13) Open the notifcation/app and press the green 'Approve' button on the bottom of the screen

##### Mac/Linux Users

1) Open up the command line on your system

2) Type 'ssh login.colorado.edu' and press 'Enter'

3) You should now be connected to JANUS and be prompted to enter your password

4) Enter 'duo:password' where password is your identikey password (do not include the single quotation marks) and press 'Enter'

5) You should receive a notification on your smartphone from Duo

6) Open the notification/app and press the green 'Approve' button on the bottom of the screen

### Using JANUS

You should now be logged into JANUS and now be able to utilize it. Since there is no graphical user interface (GUI) all of your interactions with JANUS will be via the command line. Please note, the default command line used to communicate with JANUS is **bash**, this can be changed if need be. A tutorial on bash can be found [here](http://cli.learncodethehardway.org/bash_cheat_sheet.pdf)

##### Workspaces

When you login to JANUS you will automatically be in the login workspace/directory, this is denoted by the [identikey_username@login ~]$ text on the command line. It is very important to note that this is **not** the place to store large amounts of files. Each user on JANUS has a login/home directory which is limited to 2GB, solely to prevent the use of the home directory as a target for job output. Every time you login to JANUS, a small file is created in order to ensure your login; therefore, if you fully use up this 2GB with data this file will not be created and you won't be able to login!

Therefore it's important to direct any job output or store files in your personal projects directory. Each user has access to 256GB in this directory, **much** more room than the login directory. You're able to switch into your projects directory with the following command:

```sh
$ cd /projects/username
# 'username' is your identikey username
```

As previously stated, this is the location where you should direct any job output or store files.

##### Modules

While using JANUS, we're going to need to load specific modules in order to accomodate and assist in running any programs that we wish to run on JANUS. Below are a list of commands that you can enter in order to view, import, or get rid of modules while using JANUS.

```sh
$ ml                        #View modules you currently have loaded in your session
$ ml avail                  #View all available modules currently on JANUS
$ ml intel                  #Load the intel compiler, use 'ml gcc' for the gcc compiler
$ ml python                 #Load the python module
$ ml EARTHLAB_PYTHON_PKGS   #Load all of the python packages necessary for EarthLab
$ ml unload module_name     #Unload the module called 'module_name'
$ ml purge                  #Unload all currently loaded modules
```

While you are certainly able to load any of the modules listed after the 'ml avail' command, you will for the most part just be using the following commands for any work that you need to do on JANUS:

```sh
$ ml intel
$ ml python
$ ml EARTHLAB_PYTHON_PKGS
```

##### Submitting/Running Jobs on JANUS

JANUS uses a queueing system called 'Slurm' to manage available resources and to schedule jobs that use these resources. You should always use Slurm commands to submit both batch and interactive jobs and to monitor their progress during execution. Firstly, you'll need to load the slurm module.

```sh
$ ml slurm
```

___Batch Jobs___

Slurm is primarily a resource manager for batch jobs: a user writes a job script that slurm shcedules to run non-interactively when resources are available. Submissions of computational jobs to the slurm queue are done via the *sbatch* command. 

```sh
$ sbatch job_script.sh
```

You can provide additional requirements to JANUS such as the amount of nodes/memory/tasks/time to be used for your specific job. These can be included as command line arugments such as below or within the file you wish to run.

```sh
$ sbatch --ntasks 16 job_script.sh
```

Please note that you should only be using these additional command line arguments if you have a good idea as to the amount of resources necessary to run your job. Overestimating the amount of time or resources allocated to your job will be taking away time and resources from other jobs that are scheduled.

___Monitoring Job Progress___

The *squeue* command can be used to inspect the current slurm job queue and a job's progress through it.

```sh
$ squeue --user=$USER               #List all of your current jobs on the queue
$ squeue --user=$USER --start       #Provide an estimate on when your jobs will start/what resources are expected
$ sconrol show job $SLURM_JOB_ID    #More detailed information about a specific job on the queue
```

Additional information regarding submitting jobs to JANUS such as job arrays, accounts, job mail, and memory limits can be found [here](https://www.rc.colorado.edu/support/user-guide/batch-queueing.html)

##### Running a Test Job

1) *cd* into your projects directory and make a new sub-directory called 'test_job'

```sh
$ cd /projects/username
$ mkdir test_job
$ cd test_job
```

2) Write the test_job script

```sh
$ cat - >test_job.sh << EOF
#!/bin/bash
#SBATCH --job-name test_job
#SBATCH --time 05:00
#SBATCH --nodes 1
#SBATCH --output test_job.out

echo "The job has begun"
echo "Wait one minute..."
sleep 60
echo "Wait a second minute..."
sleep 60
echo "Wait a third minute..."
sleep 60
echo "Enough waiting: job completed."
EOF
```

3) Load slurm and submit the job

```sh
$ ml slurm
$ sbatch --qos janus-debug test_job.sh
```
    
4) Monitor the job execution

```sh
$ squeue --user $USER
# Information regarding your job will be printed
$ squeue --user $USER --start
# Print the estimated start time for the job
$ tail -F test_job.out
# Print out the output of the job that we submitted
```

Congrats! You just submitted your first job on the JANUS supercomputer. Please adhere to the guidelines listed in this document for further usage of JANUS.
