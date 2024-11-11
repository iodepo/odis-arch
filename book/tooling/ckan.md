# Setting up a CKAN Catalogue

## Background

The following document explains how to set up a full metadata catalogue software 
architecture, with settings enabled to connect the catalogue to ODIS.

The initial steps are for [CKAN](https://ckan.org/), and specifically on Windows.  
This will later be expanded for Docker steps, and other methods.

## Intended Audience

The intended audience of these steps is for a technical person to follow, as
the steps require familiarity with running commands at the commandline, and 
executing various scripts.

## Windows Version

The following steps were created on Windows Server 2022, but should work on 
Windows 11 or 10.  You will be required to have full Administrator access on 
your server.

## Steps

1. Install recommended tools 
   * [Notepad++](https://notepad-plus-plus.org/downloads/) editor
   * [7-Zip](https://www.7-zip.org/) (recommended tool to manage archives)
   * [Firefox](https://www.mozilla.org/firefox/)  browser (and set as default)
2. Install PostgreSQL (<a href=#preparing-content>jump</a> to that below)
3. Install Python (<a href=#creating-a-sitemap>jump</a> to that below)
4. Install Git (<a href=#coming-full-circle-registering-your-sitemap-in-odiscat>jump</a> to that below)
5. Create a working directory (<a href=#frequently-asked-questions-faq>jump</a> to that below)
6. Create virtualenv in Python (<a href=#preparing-content>jump</a> to that below)
7. Upgrade pip (<a href=#creating-a-sitemap>jump</a> to that below)
8. Checkout CKAN source and build CKAN (<a href=#coming-full-circle-registering-your-sitemap-in-odiscat>jump</a> to that below)
9. Add PostgreSQL utils to PATH (<a href=#frequently-asked-questions-faq>jump</a> to that below)
10. Create ckan db (<a href=#frequently-asked-questions-faq>jump</a> to that below)
11. Install PostGIS extension in ckandb (<a href=#preparing-content>jump</a> to that below)
12. Generate config file for CKAN (<a href=#creating-a-sitemap>jump</a> to that below)
13. Install Java JRE (<a href=#coming-full-circle-registering-your-sitemap-in-odiscat>jump</a> to that below)
14. Install strawberry Perl (<a href=#frequently-asked-questions-faq>jump</a> to that below)
15. Install Solr (<a href=#preparing-content>jump</a> to that below)
16. Install Redis (<a href=#creating-a-sitemap>jump</a> to that below)
17. Install Java JRE (<a href=#coming-full-circle-registering-your-sitemap-in-odiscat>jump</a> to that below)
18. Create the CKAN database tables (<a href=#frequently-asked-questions-faq>jump</a> to that below)
19. Add CKAN user (<a href=#preparing-content>jump</a> to that below)
20. Run CKAN (<a href=#creating-a-sitemap>jump</a> to that below)

## Install PostgreSQL

PostgreSQL is a popular Open Source database, that will store tables leveraged by
CKAN.  It also has a very strong spatial engine, PostGIS.  We will now install both 
PostgreSQL and PostGIS, as follows:

- goto https://www.postgresql.org/download/windows/
- near the top, click on "Download the installer certified by EDB"
- click the latest for "Windows x86-64"
- double-click the installer file
- leave default install directory as-is (C:/Program Files/PostgreSQL/17/)
![PG install1](./images/pg-install1.png)
- leave default components as-is
![PG install2](./images/pg-install2.png)
- leave data directory as-is (C:/Program Files/PostgreSQL/17/data/)
- for superuser password, use "postgres"
![PG install3](./images/pg-install3.png)
- leave port as-s (5432)
![PG install4](./images/pg-install4.png)
- leave locale as-is
- install
- make sure "Stack Builder" is selected and then click "Finish"
![PG install5](./images/pg-install5.png)
- in the "Stack Builder" window, select your installation in the dropdown 
  ("PostgreSQL 17 on port 5432") and then click "Next"
- expand "Spatial Extensions" and click the checkbox for "PostGIS x.x Bundle for PostgreSQL"
![PG install6](./images/pg-install6.png)  
- leave download directory as-is, click "Next"
- wait for the PostGIS installer to download
- click "Next" to begin PostGIS install
- click "I Agree" to the PostGIS license
- leave components as-is
- leave destination folder as-is
- click "Finish" to end the installation
![PG install8](./images/pg-install8.png)

## Install Python

CKAN 2.11 (the latest release as of writing this document) supports Python versions 
3.9 to 3.12. This document will explain how to install Python 3.12, as follows:

```{note}
If you have an existing Python installation, you may attempt at using it, but
leveraging a Python virtual environment (venv) is recommended, which is explained
later in this document.
```

- create a new folder "Python" at the root of your C:/ drive, so you have a path of
  `C:/Python`
- download 3.12.7 "Windows installer (64-bit)" from https://www.python.org/downloads/windows/
- double-click the file "python-3.12.7-amd64.exe" to install
- choose "Customize installation" & check the checkbox for "add python.exe to PATH"
![Python install1](./images/python-install1.png)
- leave "Optional Features" as-is
- for "Advanced Options", click on the "Browse" button, to select the install location,
  and choose the `C:/Python` folder
![Python install2](./images/python-install2.png)
- click the "Install" button
- test with a CMD command
  - in the Windows search bar, type "CMD" and press <enter> on your keyboard
  - make sure you right-click on the icon and select "Run as Administrator"
    ![CMD as administrator](./images/cmd-admin1.png)
  - at the command prompt, type: 
    ```bash
      python --version
    ```
    ![Python install3](./images/python-install3.png)

## Install Git

We will use git to "checkout" (which means to get locally) the latest changes in 
software that is required for CKAN (as often the released code contains errors, that 
are fixed in the software's GitHub repository).  We will also be using git through 
the commandline.

```{tip}
After installing, will use the commandline for git, but you will also see a "Git GUI" 
option in the Start Menu, that you may prefer for a more visual experience.  There 
are also other visual tools that you can install instead, such as 
[GitHub Desktop](https://github.com/apps/desktop).
```
- goto https://git-scm.com/downloads/win and select "Click here to download" the 
  64-bit version of Git for Windows
- run the installer
- select "Checkout as-is, commit as-is"
  ![Git install1](./images/git-windows1.png)
- select "Use Windows' default console window"
  ![Git install2](./images/git-windows2.png)
- select "Fast-forward or merge" for 'git pull'
  ![Git install3](./images/git-windows3.png)
- default credential manager (no changes)
  ![Git install4](./images/git-windows4.png)
- select "Enable file system caching"
- test by opening a CMD window and executing: git --version
  ![Git install6](./images/git-windows6.png)

## Create a working directory

Using Windows File Explorer, create a new folder named "working" at the 
`C:/` drive root, so you have the existing path `C:/working`
![File Explorer](./images/working-folder.png)

## Create virtual environment in Python

We will use a `venv` virtual environment in Python, to make sure that 
the installation does not conflict with others on your server.  Open 
a CMD window, and execute the following to create a new `ckan-venv` environment:
```bash
  cd C:\working
  python -m venv ckan-venv
  C:\working\ckan-venv\Scripts\activate
```
You should now see a prompt that looks like the following:
![venv](./images/python-venv.png)

You can also execute `deactivate` to exit that `ckan-venv` virtual environment, 
and then execute `C:\working\ckan-venv\Scripts\activate` to reactivate.

## Upgrade pip

Open a CMD window, and make sure that your `ckan-venv` is activated, and then 
upgrade pip as follows:
```bash
python -m pip install --upgrade pip
```

## Checkout the CKAN source code and build CKAN

We will use git to get the latest source code direct from the CKAN
repository on GitHub, and then build CKAN inside the `ckan-venv` virtual 
environment.  Open a CMD window, and execute:
```bash
  cd C:\working
  C:\working\ckan-venv\Scripts\activate
  git clone https://github.com/ckan/ckan.git ckan-git-master
  cd ckan-git-master
  python -m pip install --upgrade -r requirements.txt
  python -m pip install python-magic-bin
  python -m pip install -e .
```
![CKAN install1](./images/ckan-install1.png)

You can now try to a test, to see the usage, such as:
![CKAN install2](./images/ckan-install2.png)

## Add PostgreSQL utils to PATH

We will need to run various PostgreSQL tools from the commandline, so we need 
to make sure that they are found on the `PATH` environment variable on your
server.  To set the system PATH, execute the following:

- in the Windows search bar, searcg for "env" and choose "Edit the system environment variables"
- click on the bottom "Environment variables" button
  ![PG env1](./images/pg-env1.png)
- select `Path` in the lower "System variables" section and click the "Edit..."
  button
  ![PG env2](./images/pg-env2.png)
- click "New" and then "Browse" to C:/Program Files/PostgreSQL/xx/bin/"
  ![PG env3](./images/pg-env3.png)
- click "OK"
- close your CMD window, and re-open it
- test by executing: `psql --version`
  ![PG env4](./images/pg-env4.png)

## Create the ckan database

We will now create a user profile in `ckanuser` PostgreSQL.  Open a CMD window 
and execute:

```bash
  createuser -U postgres -p 5432 -s -D -r -P ckanuser
    enter password for new role: odis
    enter it again: odis
    password: postgres
```

We will now create a new database `ckandb` in PostgreSQL.  In your CMD window
execute:

```bash
createdb -U postgres -p 5432 -O ckanuser ckandb -E utf-8
  password: postgres
```

## Install the PostGIS extension in ckandb

You likely will need spatial tables inside the `ckandb` database, so it 
is recommended to enable the PostGIS extension, by executing in your 
CMD window as follows:

```bash
psql -U ckanuser -p 5432 -d ckandb
  password for ckanuser: odis
```
You should now be at a prompt like `ckandb=>`

Then execute to list all tables: `\d <enter>`
You see a response as `Did not find any relations`

Next execute:
```bash
  CREATE EXTENSION postgis;  <enter>
  CREATE EXTENSION postgis_topology;  <enter>
  ALTER DATABASE ckandb SET client_min_messages TO WARNING;  <enter>
```
Again execute to list all tables (you should see more tables now) : `\d <enter>`
![PG table install](./images/postgis-table-install.png)

to quit, execute: `\q <enter>`

## Generate config file for CKAN

We will run the built `ckan` tool to generate a config file for CKAN.  Open a 
CMD window and execute:

```bash
  cd C:\working
  C:\working\ckan-venv\Scripts\activate
  mkdir ckan-site
  cd ckan-site
  ckan generate config ckan.ini
```

Now open in Notepad++: C:\working\ckan-site\ckan.ini
and set the following:

```
  line# 73:
    sqlalchemy.url = postgresql://ckanuser:odis@localhost/ckandb

  line# 78:
    ckan.site_url = http://localhost:5000

  line# 139:
    ckan.site_id = default
    
  line# 195
    extra_template_paths = C:\working\ckan-git-master\ckan\templates
    
  line# 202:
    ckan.storage_path = C:\working\ckan-site\data  
```
Using Windows File Explorer, then create a new `data` folder inside 
`C:\working\ckan-site`

##Install Java JRE

Several tools for CKAN require that we install Java, as follows:

- download "Open JDK 21.x" from https://learn.microsoft.com/en-ca/java/openjdk/download
```{tip}
   JDK 21 is recommended for latest Solr through GitHub
```
- use MSI installer for x64 platform
- run installer (use all defaults)
- test: open a new CMD window and execute: java --version
- check your system Environment Variables list to make sure JAVA_HOME is set
    - set it to: 
        `C:\Program Files\Microsoft\jdk-17.0.13.11-hotspot`

## Install strawberry Perl

- download: https://strawberryperl.com/
- use MSI installer
- leave defaults as-is
- test with new CMD window, executing: `perl --version`

## Install Solr

CKAN leverages Solr for its fast indexing/searches.  To install Solr
execute the following in a CMD window:

```bash
  cd C:\working
  C:\working\ckan-venv\Scripts\activate  
  git clone https://github.com/apache/solr.git solr-git-main
  cd solr-git-main
  gradlew dev
  cd C:\working\solr-git-main\solr\packaging\build\dev
```
- Test Solr by executing: `bin\solr.cmd --help`
    
- Now we must start Solr in "standalone mode"
```bash
  bin\solr.cmd start --user-managed -p 8983
```
  In your web browser goto: http://localhost:8983/solr
  
- Now check Solr status with `bin\solr.cmd status`

```
        Solr process 2360 running on port 8983
        {
          "solr_home":"C:\\working\\solr-git-main\\solr\\packaging\\build\\dev\\server\\solr",
          "version":"10.0.0-SNAPSHOT bc0c226c8fe9c475e5e723355f729fd39ceaf30f [snapshot build, details omitted]",
          "startTime":"Sat Nov 09 16:01:17 AST 2024",
          "uptime":"0 days, 0 hours, 13 minutes, 19 seconds",
          "memory":"115.4 MB (%22.5) of 512 MB"}
```
- now create a new `ckan` Solr core
```
  bin\solr.cmd create -c ckan
     "Created new core 'ckan'"
```
     
- now stop Solr
```
bin\solr.cmd stop -p 8983
```
- copy schema.xml from `C:\working\ckan-git-master\ckan\config\solr`
  to `C:\working\solr-git-main\solr\packaging\build\dev\server\solr\ckan\conf`               
- delete the file `managed-schema.xml` in `C:\working\solr-git-main\solr\packaging\build\dev\server\solr\ckan\conf`

- now start Solr
```
  bin\solr.cmd start --user-managed -p 8983
```
- in your web browser, check the `ckan` core
  - http://localhost:8983/solr/#/ckan/core-overview

- get status of one core ("ckan")
```
curl -X GET http://localhost:8983/api/cores/ckan

        {
          "responseHeader":{
            "status":0,
            "QTime":4
          },
          "initFailures":{ },
          "status":{
            "ckan":{
              "name":"ckan",
              "instanceDir":"C:\\working\\solr-git-main\\solr\\packaging\\build\\dev\\server\\solr\\ckan",
              "dataDir":"C:\\working\\solr-git-main\\solr\\packaging\\build\\dev\\server\\solr\\ckan\\data\\",
              "config":"solrconfig.xml",
              "schema":"managed-schema.xml",
              "startTime":"2024-11-09T20:33:09.309Z",
              "uptime":253492,
              "index":{
                "numDocs":0,
                "maxDoc":0,
                "deletedDocs":0,
                "version":2,
                "segmentCount":0,
                "current":true,
                "hasDeletions":false,
                "directory":"org.apache.lucene.store.NRTCachingDirectory:NRTCachingDirectory(MMapDirectory@C:\\working\\solr-git-main\\solr\\packaging\\build\\dev\\server\\solr\\ckan\\data\\index lockFactory=org.apache.lucene.store.NativeFSLockFactory@17a1916f; maxCacheMB=48.0 maxMergeSizeMB=4.0)",
                "segmentsFile":"segments_1",
                "segmentsFileSizeInBytes":69,
                "userData":{ },
                "sizeInBytes":69,
                "size":"69 bytes"
              }
            }
          }
        }
```

## install Redis

To install Redis (required for CKAN), we must install the WSL (Windows Subsystem for Linux),
as follows:
  - follow https://learn.microsoft.com/en-us/windows/wsl/install
  - open CMD window and execute:
    - see list of all Linux distribution names
      ```
        wsl --list --online
      ```
    - now install Ubuntu
      ```
        wsl --install --enable-wsl1 --distribution "Ubuntu-24.04 LTS"
      ```
  - reboot machine
  - you should see a progress bar for installing Ubuntu
  - when asked to create a new user, enter:
    ```
      username: odis
      password: odis
    ```
  - to run: goto Start menu, choose "WSL"
    - CMD window should open with an odis@ prompt
  - to check the Ubuntu version, run:
    ```
      lsb_release -a
      
         Distributor ID: Ubuntu
         Description:    Ubuntu 24.04 LTS
         Release:        24.04
         Codename:       noble
    ```   
   - install the redis package
     - (follow steps at https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-windows/
       ```
         curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
         echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
         sudo apt-get update
         sudo apt-get upgrade
         sudo apt-get install redis
      ```
     - if error "Failed to take /etc/passwd lock: Invalid argument", execute:
       ```
         sudo mv /var/lib/dpkg/info /var/lib/dpkg/info_silent
         sudo mkdir /var/lib/dpkg/info
         sudo apt-get update
         sudo apt-get -f install
         sudo mv /var/lib/dpkg/info/* /var/lib/dpkg/info_silent
         sudo rm -rf /var/lib/dpkg/info
         sudo mv /var/lib/dpkg/info_silent /var/lib/dpkg/info
         sudo apt-get update
         sudo apt-get upgrade
         sudo apt-get install redis
      ```
    - start the redis server
      ```
        sudo service redis-server start
      ```
   - test it by running: `redis-cli`
     ```
       127.0.0.1:6379>
       127.0.0.1:6379>ping
         PONG
     ```         
  
## Create the CKAN database tables

- open new CMD window, and execute:
```
  C:\working\ckan-venv\Scripts\activate
  cd C:\working\ckan-site
  ckan -c ckan.ini db init
```
- you should see a green message: "Upgrading DB: SUCCESS"
- test with psql command:
  ```
    psql -U ckanuser -p 5432 -d ckandb -c "\d"
      password: odis
  ```
  you should see 32 rows of tables


