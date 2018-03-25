# emailGenerator

This is a simple tool create email and forwarding csv lists from a list of names provided in a text file. 

**Usage**

Example: python3 emailGenerator.py -f names.txt -d domain.com -t hello@domain.com -p samplePassword

**Options**

**-d**: Domain - The name of the domain you want the emails created for.

**-f**: File - The path to, or name of the file you want to read the names from. 

**-m**: Method - The format of the email you want to generate. The default email format is *firstname.lastname@domain.com*.

**-p**: Password - The password to the emails you're creating. The default password is *hxBU4gHCIeJhIg*.

**-t**: Target - This is the target email for email forwarding. 

**-o**: Output - This specifies the name of the file containing the email list. The default file is *emails.csv*