# PetaLibrary Earth Lab Tutorial

## About

The [PetaLibrary](https://www.rc.colorado.edu/resources/storage/petalibrary) is a rescource managed by Research Computing, and subsidized by the National Science Foundation, that allows researchers affiliated with CU a place to store large amounts of data to be used for their research needs. This tutorial will provide useful information to aid Earth Lab members in accessing, and using the PetaLibrary.

## Authentication

The PetaLibrary is only available to certain CU researchers who pay the required fees. Fortunately, Earth Lab provides access to the PetaLibrary, but there must be a method for authenticating users to ensure this valuable rescource is not abused. In this case, Earth Lab members will use an RC account with Duo dual authentication.

### Getting an RC Account

1) Open up a web browser and head to the [RC Account Creation Page](https://portals.rc.colorado.edu/account/request/)
2) At the bottom of the screen, ensure 'University of Colorado - Boulder' is selected fom the dropdown box under 'Select your organization' and press 'Continue'
3) Provide your CU Boulder identikey username and password
4) Provide your proper University affiliation, enter 'EarthLab' for Organization/Department you represent, and ensure 'bash' is selected for 'Preferred login shell'
5) Click 'Submit Request'

### Getting a Duo Account

1) Open up a web browser and head to the [Duo Signup Page](https://signup.duo.com/)
2) Provide your first name, last name, CU Boulder email address, mobile phone number, enter 'EarthLab' as Company/Account Name, and selecter 'Just me' from the final dropdown box
3) Check the Terms/Privacy Policy box and click 'Create My Account'
4) Download the Duo Mobile application on your smartphone
5) Ensure that notifications are enabled for the Duo Mobile application
5) Come into the ARC Building on East Campus to see Joel (6th floor, Room 679) with your CU Boulder photo ID card
6) Joel will then issue an email/text message/phone call to verify and finalize the two-step authentication setup process


## Accessing the Library
There are several different methods for accessing the PetaLibrary that will be outlined below.

### RC Environment
Assuming you have an account with research computing and have access to the PetaLibrary, you sould have PetaLibrary directories available in your research computing environment. Information on how to access an RC environment through Janus login nodes can be found [here](https://github.com/earthlab/tutorials/blob/2acec457c3af7001bea474a5f0c6a03fc9b88b2c/documentation/Getting_Started_with_JANUS.md). The PetaLibrary directories will be `/work/` for active storage, `/repl/` for active storage with replication, and `/archive/` for archive storage. 

Now that you have established a connection with an RC environment you will need to know what each of these directories does, and how they can be most effectively used.

#### Active Storage
Active storage (`/work/`) will be accessible for read and write directly through any RC environment. This of course includes both the login and compute nodes. This is the directory you will want to be using to read and write data while you are working on a project.

#### Active Storage with Replication
Active storage with replication (`/repl/`) will be available for read only purposes from the login nodes. This directory contains copies of your data, and is used as a tool to backup files that may be inadvertently deleted.

#### Archive Storage
Archive storage (`/archive/`) will be available for read and write purposes from login nodes only. This is meant to be used to transfer data from other storage spaces, and should not be used extensively during a project.

### External Access

#### Globus

Globus is an effective tool for high performance data transfer. GolobusOnline provides an easy-to-use web app for accessing Globus tools. To get started with [GlobusOnline](https://www.globus.org/), select the login option at the top of the homepage. Next, select The University of Colorado at Boulder as your organization from the dropdown menu. When you click continue you will be taken to a page where you should be able to sign in with your CU Identikey username and password. Once you have logged in you can associate your Indentikey with your Globus account. You will only need to do this the first time you login. After this is done, you will want to use the Transfer Files tool and click 'Start by selecting an endpoint'. From here, go to the My Endpoints tab and select 'add Globus Connect Personal'. This should allow you to select the computer you are working on as one endpoint. For the second enpoint you will want to use 'colorado#gridftp'. This will require you to sign in with your RC account credentials. Use `<identikey>`@duo as the username and enter your password. This should send a Duo authentication notice to your phone, assuming you have properly set up your duo account. Once this is done your RC computing environment should be set as your second endpoint. Now you can easily transfer files to and from your computer and the PetaLibrary, as well as any other RC storage space, using the simple interface.

Globus also has a command-line interface that allows you to manage data transfer without using the web app. Information on how to configure and use the Globus command-line interface can be found [here](https://docs.globus.org/cli/using-the-cli/).

#### SSH

SSH methods are much less efficient than Globus, but you may find them to be more convenient for moving only a few files.

##### Windows Users

Windows users will want to go to the [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) site, and download pscp.exe. This is a command line interface, and it does not install itself, so you will need to place the file in a desired directory. Next, add that directory to your path variable. More information on setting your path in windows look [here](http://www.computerhope.com/issues/ch000549.htm). Once the path has been properly set you will be able to use the pscp command to tranfer files. Specifics on using this command will be given in the next section, just be sure to replace `scp` with `pscp`.This is the only difference, otherwise the command works exactly the same as OS X and Linux users.

##### Mac/Linux Users

In the command line, navigate to the directory containing the files you would like to transfer. Once in the directory you should be able to use the command 
`scp file_name <identikey>@login.rc.colorado.edu:/path/to/directory`
You will then be asked for a password. Enter 'duo:password' and a Duo authentication notification will be sent to your phone. Accept the notification, and the file(s) should be transfered to your RC environment. Of course, you will want to use one of your PetaLibrary directories in the path argument if you would like to send files to the PetaLibrary. One useful tool is to replace the `file_name` argument with `*.type` where type is some file extension for a specific type of file you would like to transfer. This will transfer all files of that type in the current directory, instead of transfering files one at a time. 
