"""

Copyright 2020 ZenTheDev

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom
the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING 
BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

import os
import sys
import traceback
import argparse
import requests

os.system('COLOR 07')

parser = argparse.ArgumentParser(description='Launch bots onto webpages using Somniac. Example command: python Somniac.py -W http://www.website.com/page.php -N t -E t -C t -X t')
parser.add_argument('-W', '--website', type=str, metavar='', required=True, help='\033[93mThe website contact/login/signup page URL (eg. http://www.website.com/contact.php)\033[0m')
parser.add_argument('-N', '--bname', type=str, metavar='', required=True, help='\033[93mIf the website contact/login/signup page has a name section (eg. t(true) or anything else for false)\033[0m')
parser.add_argument('-E', '--bemail', type=str, metavar='', required=True, help='\033[93mIf the website contact/login/signup page has an email section (eg. t(true) or anything else for false)\033[0m')
parser.add_argument('-C', '--bcomment', type=str, metavar='', required=True, help='\033[93mIf the website contact/login/signup page has a comment section (eg. t(true) or anything else for false)\033[0m')
parser.add_argument('-X', '--bextra', type=str, metavar='', required=True, help='\033[93mIf the website contact/login/signup page has an extra section (eg. t(true) or anything else for false)\033[0m')

parser.add_argument('-1', '--sname', type=str, metavar='', required=False, default='name', help='The name of the name section, if the website has a name section (eg. name)')
parser.add_argument('-2', '--semail', type=str, metavar='', required=False, default='email', help='The name of the email section, if the website has an email section(eg. email)')
parser.add_argument('-3', '--scomment', type=str, metavar='', required=False, default='comment', help='The name of the comment section, if the website has a comment section (eg. comment)')
parser.add_argument('-4', '--sextra', type=str, metavar='', required=False, default='Submit', help='The name of the extra section, if the website has an extra section (eg. Submit)')

parser.add_argument('-n', '--name', type=str, metavar='', required=False, default='John Doe', help='The name (eg. John Doe)')
parser.add_argument('-e', '--email', type=str, metavar='', required=False, default='examplegmail', help='The name part of the email (eg. myemail391, the @gmail.com will automatically be appended)')
parser.add_argument('-c', '--comment', type=str, metavar='', required=False, default='Hello, World!', help='The comment (eg. Hello, World!)')
parser.add_argument('-x', '--extra', type=str, metavar='', required=False, default='Send', help='The extra data (eg. Send)')

parser.add_argument('-i', '--iter', type=int, metavar='', required=True, help='\033[93mThe amount of bots to send to the URL (eg. 20)\033[0m')
args = parser.parse_args()

bot_name = bot_email = bot_comment = bot_extra = 'Undefined'

try:
	print(f'\033[93mUser args: URL = {args.website}, Name Section = {args.bname}, Email Section = {args.bemail}, Comment Section = {args.bcomment}, Extra Section = {args.bextra}\033[0m')

	base = ['name', 'email', 'comment', 'extra']
	reqdict = {}

	for sec in base:
		if getattr(args, 'b' + sec) == 't':
			reqdict[getattr(args, 's' + sec)] = getattr(args, sec)
			exec('bot_' + sec + ' = args.' + sec, globals())

	for i in range(args.iter):
		requests.post(args.website, allow_redirects=False, data=reqdict)

		if i >= 1:
			sys.stdout.write("\033[F")
			sys.stdout.write("\033[K")

		print(f'\033[93mSending \033[91mbot #{i + 1}\033[93m with args: Name = {bot_name}, Email = {bot_email}, Comment = {bot_comment}, Extra = {bot_extra}\033[0m')
except:
	traceback.print_exc()
	input('\033[94mPress any key to continue...\033[0m')
