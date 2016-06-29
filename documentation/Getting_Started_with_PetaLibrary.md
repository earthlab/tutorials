# PetaLibrary Earth Lab Tutorial
## About
The [PetaLibrary](https://www.rc.colorado.edu/resources/storage/petalibrary) is a rescource managed by Research Computing, and subsidized by the National Science Foundation, that allows users a place to store large amounts of data to be used for their research needs. This tutorial will provide useful information to aid Earth Lab members in accessing, and using the PetaLibrary.

## Authentication
This tutorial will go through accessing the PetaLibrary using duo dual authentication. G

## Accessing the Library
There are several different methods for accessing the PetaLibrary. The Globus and gridftp are by far the most efficient and should be used for any large data transfers, but depending on your needs some of the other methods may be easier or more convenient.

### RC Environment
Assuming you have an account with research computing and have access to the PetaLibrary you sould have PetaLibrary directories available in your research computing environment. Information on how to access an RC environment through Janus login nodes can be found [here](link to Janus guide). The PetaLibrary directories will be `/work/` for active storage, `/repl/` for active storage with replication, and `/archive/` for archive storage. Active storage, and archive storage will have read and write capabilities directly from the RC environment, while the active with replication storage directory will be read only.

### Login
Some information on accessing the PetaLibrary can be found [here](https://www.rc.colorado.edu/resources/storage/petalibrary/accessinstructions). The PetaLibrary can be accessed directly from Janus login nodes. Information on how to access Janus can be found [here](link to Janus guide). 

### Globus
Globus is an effective tool for high performance data transfer. GolobusOnline provides an easy-to-use web app for accessing Globus tools. To get started with [GlobusOnline](https://www.globus.org/) select the login option at the top of the homepage. Select The University of Colorado at Boulder as your organization from the dropdown menu. When you click continue you will be taken to a page where you should be able to sign in with your CU Identikey username and password. Once you have logged in you can associate your Indentikey with your Globus account, you will only need to do this the first time you login. Once you are logged in, you will want to use the Transfer Files to select an endpoint. From here, go to the My Endpoints tab and select 'add Globus Connect Personal'. From here you should be able to select your personal computer as one endpoint.