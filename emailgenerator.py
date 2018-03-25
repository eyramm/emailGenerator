import argparse
import csv
import os
import sys


class EmailGenerator:

    def __init__(self):

        parser = argparse.ArgumentParser()
        parser.add_argument('-d', '--domain', dest='domain', required=True)
        parser.add_argument('-f', '--file', dest='file', required=True)
        parser.add_argument('-t', '--target', dest='target',
                            required=True, help='Target forwarding email')
        parser.add_argument('-m', '--method', dest='method', type=int,
                            default=1, required=False, choices=range(1, 8), help='''
        Email formats
        1-{firstname}.{lastname}@{domain}
        2-{lastname}.{firstname}@{domain}
        3-{firstname}-{lastname}@{domain}
        4-{firstname[0]}{lastname}@{domain}
        5-{lastname}{firstname[0]}@{domain}
        6-{lastname[0]}{firstname}@{domain}
        7-{firstname}{lastname[0]}@{domain}
        ''')
        parser.add_argument('-p', '--password', dest='password',
                            default="hxBU4gHCIeJhIg", required=False)
        parser.add_argument('-o', '--output', dest='output',
                            default="emails.csv", required=False)
        try:
            self.__args = parser.parse_args()
        except Exception:
            print("Error while parsing arguments")

    def generate_email(self, names, domain, email_format):
        name = names.lower().split()
        if email_format == 1:
            return "{0}.{1}@{2}".format(name[0], name[-1], domain)
        elif email_format == 2:
            return "{0}.{1}@{2}".format(name[-1], name[0], domain)
        elif email_format == 3:
            return "{0}-{1}@{2}".format(name[0], name[-1], domain)
        elif email_format == 4:
            return "{0}{1}@{2}".format(name[0][0], name[-1], domain)
        elif email_format == 5:
            return "{0}{1}@{2}".format(name[-1], name[0][0], domain)
        elif email_format == 6:
            return "{0}{1}@{2}".format(name[-1][0], name[0], domain)
        elif email_format == 7:
            return "{0}{1}@{2}".format(name[0], name[-1][0], domain)
        else:
            print("Invalid Option!! Emails not generated")
            sys.exit()

    def _main(self):
        # Get the domain from command line arguments
        domain = self.__args.domain

        # Get the password from command line arguments
        password = self.__args.password

        # Get the target email from command line arguments
        target = self.__args.target

        # Get the email format from command line arguments
        email_format = self.__args.method

        # Read input file and create a list of emails from the lines
        with open(self.__args.file, "r") as names_file:
            emails = []
            for name in names_file.readlines():
                emails.append(self.generate_email(name, domain, email_format))

        # Write Emails to Forwarding file
        with open("forwarding.csv", "a") as emails_file:
            emails_file.write("Source,Target\n")
            emails_file.writelines(
                [e_mail+"," + target + "\n" for e_mail in emails])

        # Open output file as writable
        with open(self.__args.output, "a") as f:
            f.write("Email,Password,Quota\n")
            for email in emails:
                f.write("{0},{1},10\n".format(email, password))


if __name__ == "__main__":
    email_generator = EmailGenerator()
    email_generator._main()
