# Somniac

Somniac is a program used to send 'bots' to specific web URLs

## Usage

1. Open command prompt in the folder somniac.py is inside of
2. Run Somniac.py with the python command adding the required arguments

###### Example
```dos
python Somniac.py -W http://www.site.com/page.php -N t -E t -C t -X t -i 20
```
## Arguments

```
-W or --website
```
The website argument represents the web URL the bots will be sent to 

`(eg. -W https://www.site.com/page.php)`
```
-N or --bname
```
The bname argument represents whether or not the site has a 'Name: ' section, t is for true, and any other character is equivalent to false

`(eg. -N t)`
```
-E or --bemail
```
The bemail argument represents whether or not the site has an 'Email: ' section, t is for true, and any other character is equivalent to false

`(eg. -E t)`
```
-C or --bcomment
```
The bcomment argument represents whether or not the site has a 'Comment: ' section, t is for true, and any other character is equivalent to false

`(eg. -C t)`
```
-X or --bextra
```
The bextra argument represents whether or not the site has an extra section. Normally extra sections are hidden and will have the key 'Submit', and the value 'Send'. You can use this extra argument to represent another section in a form; t is for true, and any other character is equivalent to false

`(eg. -X t)`
```
-i or --iterator
```
The iterator argument represents how many times a new 'bot' should be launched

`(eg. -i 20)`

**Other arguments can be see using `python Somniac.py -h`**
## License
[MIT](https://choosealicense.com/licenses/mit/)
