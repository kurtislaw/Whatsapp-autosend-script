# Whatsapp-autosend-script

A python script to automatically send whatsapp messages.

Any contributions from you guys are welcome. Just fork this repository, make changes in the code and create a pull request, I will merge the changes if it seems interesting. :)

Do star the repo if you think it worth it.

# Requirements (on your system)
1. Chrome/Chromium Browser (https://www.google.com/chrome/browser)
2. Chrome WebDriver (https://chromedriver.storage.googleapis.com/index.html?path=2.33/)
3. Python3 (https://www.python.org/downloads/)
4. Virtualenv (<code>$ pip3 install virtualenv</code>)
5. Selenium (<code>$ pip3 install selenium</code>)

# Steps to run in your local machine (MacOS)
1. Open Terminal and clone the repository<br>
<code>$ git clone https://github.com/kurtislaw/Whatsapp-autosend-script.git</code> 
2. Goto the base directory of the project <br>
<code>$ cd Whatsapp-autosend-script</code>  
3. Create a virtual environment and activate it.<br> 
<code> $ python3 -m venv venv </code><br>
<code> $ . venv/bin/activate </code>
4. Install the requirements for the project<br> 
<code> $ pip3 install -r requirements.txt </code>
6. Download the ChromeWebdriver appropriate to your current browser and extract into the directory.
7. In the file `autosend.py`, edit the variables under the "TO BE CHANGED" section accordingly.
8. Add your texts to `texts.txt`. Each new line represents a new text message.
9. Run the script<br>
<code> $ python3 autosend.py</code>
