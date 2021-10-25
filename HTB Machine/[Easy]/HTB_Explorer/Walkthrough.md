# Explore Walkthrough
![image](https://user-images.githubusercontent.com/50168261/138621406-538ee1f4-cd1d-4ae9-a012-78f117f31f58.png)
<div align="right"><i>Box Author: <a href="https://www.hackthebox.eu/home/users/profile/27897">bertolis</a></i></div>

# Open Source Intelligence & Analyze

Port scanning by IP-address with high level of verbality.
<div align="center"><img src="https://user-images.githubusercontent.com/50168261/138760351-d0bdc521-3674-40a2-8c02-e238692178d5.png" width="650" 
  height="90"></a>
  </div>
<div align="center"><img src="https://user-images.githubusercontent.com/50168261/138760653-15254c35-4812-4600-8116-b403f6902f9f.png" width="650" 
  height="190"></a>
  </div>
As a result of the scan we get a list of available ports.

* 2222: SimpleSSH
* 5555: ADB
* 59777: File Explorer

Often, because of human stupidity, File Explorer can contain files with username/password: most often these are graphic images, text files. Therefore you should check port 59777 for such files. 
<div align="center"><img src="https://github.com/RdrStels/Practice-CTF/blob/main/HTB%20Machine/%5BEasy%5D/HTB_Explorer/Screenshot_2021-10-15_15-57-18.png?raw=true" width="1280" 
  height="450"></a>
  </div>
 

Using the exploit, we get a list of files to download (the most interesting ones are signed)
<div align="center"><img src="https://github.com/RdrStels/Practice-CTF/blob/main/HTB%20Machine/%5BEasy%5D/HTB_Explorer/Screenshot_2021-10-15_16-01-12.png?raw=true" width="680"
  height="450"></a>
  </div>
  
![image](https://github.com/RdrStels/Practice-CTF/blob/main/HTB%20Machine/%5BEasy%5D/HTB_Explorer/Screenshot_2021-10-15_16-08-57.png?raw=true)

