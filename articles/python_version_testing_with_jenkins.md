[Jenkins CI's](http://jenkins-ci.org/) [ShiningPanda plugin](https://wiki.jenkins-ci.org/display/JENKINS/ShiningPanda+Plugin) 
makes testing Python extremely easy. It even includes support for testing 
against multiple Python versions within the same Job. Unfortunately 
ShiningPanda, and Jenkins itself, do not automatically install these 
dependent Python versions.

Using [Pythonbrew](https://github.com/utahta/pythonbrew) we can configure 
Jenkins to automatically download and install our dependent versions of Python.


Overview
========
1. Install Shining Panda Plugin.
2. Install pythonbrew (from within Jenkins!)
3. Configure Jenkins' Python 'Tools'.
4. Create Jobs, and test!


Prerequisites
=============
1. A live running Jenkins instance.
2. That's it!


Steps
=====

Phase I: Configure Jenkins
--------------------------
1. From the Jenkins console browse to **Manage Jenkins > Manage Plugins > Available**.
2. Select the **ShiningPanda Plugin** and click **Download now and install after restart**.
3. After Jenkins restarts, from the console, browse to **Manage Jenkins > Script Console**.
4. Paste in the following Groovy script and click **Run**:

        :::Groovy
	    def download = """curl -skLO http://xrl.us/pythonbrewinstall"""
	    def download_proc = download.execute()
	    def install = """bash pythonbrewinstall"""
	    def install_proc = install.execute()
       	
	    download_proc.waitFor()
        
	    println "return code: ${download_proc.exitValue()}"
	    println "stderr: ${download_proc.err.text}"
	    println "stdout: ${download_proc.in.text}"
        
	    install_proc.waitFor()
        
	    println "return code: ${install_proc.exitValue()}"
	    println "stderr: ${install_proc.err.text}"
	    println "stdout: ${install_proc.in.text}"

5. From the Jenkins console, browse to **Manage Jenkins > Configure System**.
6. Under **Python** click **Add Python**. 
7. For each Python version to install, enter a **Name** and click **Install Automatically > Add Installer > Run Command**.

	!['Add Installer' dialog](http://dl.dropbox.com/u/4036736/Screenshots/9b~1.png)

8. Given a Python version of X.Y.Z, for **Command** enter: `$HOME/.pythonbrew/bin/pythonbrew install X.Y.Z`
9. Given a Python version of X.Y.Z, for **Tool Home** enter: `$HOME/.pythonbrew/pythons/Python-X.Y.Z/`
10. Click **Save**

Phase II: Create Job
--------------------
1. From the Jenkins console, browse to **New Job**.
2. Enter a **Job name** and select **Build multi-configuration project**.
3. Under **Configuration Matrix**, click **Add Axis > Python**.

	!['Add axis' dialog](http://dl.dropbox.com/u/4036736/Screenshots/_mvo.png)

5. Select the Python version(s) to run this job against.

	!['Python' dialog](http://dl.dropbox.com/u/4036736/Screenshots/nhzn.png)

7. Under **Build**, **Add build step**s for your project.
8. Test!

Usage
=====
I prefer using the **Virtualenv Builder** for my project, with the following **Command**s:

    :::bash
    $PYTHON_EXE setup.py install
    $PYTHON_EXE setup.py nosetests

!['Virtualenv Builder' dialog](http://dl.dropbox.com/u/4036736/Screenshots/811y.png)

Which leaves me with healthy, all natural, self-installed multiple Python version
job configuration:

!['Configurations' dialog](http://dl.dropbox.com/u/4036736/Screenshots/5tz2.png)
