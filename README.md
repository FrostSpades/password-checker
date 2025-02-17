# Password Checker
University of Utah

Class: DS2500  
Created by: Ethan Andrews  
Version: 2025.2.17

## Description

Checks a password's strength and returns any potential weaknesses. Usage includes inputting a password, and a list of weaknesses is printed.

## Usage
Requires python3 to be installed, but has no external dependencies.  

Clone the repository  

`git clone https://github.com/FrostSpades/password-checker.git`

Go into the newly created directory  

`cd password-checker`

Can be used as a standalone file:

`python3 password_checker.py`

Or the internal method can be called as a module:

`from password_checker import check_password`

## Limitations

This tool is for educational use only. The password checker is very rudimentary. This should not be used as the primary password checker for a serious commercial or personal project.

## Ethical Considerations

This tool, to the best of my knowledge, is secure and is not vulnerable to any security flaws. However, this tool may provide a false sense of security. It performs a few basic password checks, but is by no means an exhaustive password checker. For serious projects, a more serious password checker should be used. 

This module should not be used for projects involving real user data or for projects in which security is a real concern.
