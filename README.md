# wordle-solver

this code is a simple script which is also called Wordle solver.

the usage may be a little complicated but it's worth to try.


## Usage
in the begining make a few guesses by your own to find out some simple characters which helps script find answer more acurate.<br/> Let's assume you are facing with following situation:<br/><br/>
![WORDLE IMAGE](https://i.inews.co.uk/content/uploads/2022/01/Screenshot-2022-01-05-at-17.10.58-640x360.png)<br/>
as you can see we have green, yellow, gray charactes, the way we pass these characters to script is:<br/>
__For green characters: (CHARACTER+INDEX, CHARACTER+INDEX) for example 's2,t4' means there is a character 'T' in index '4' and 'S' in index '2'__<br/>
__Yellow characters: (CHARACTER, CHARACTER) for example 'i' (without passing it's index) means the character 'i' is in the word but we don't know what is it's index__<br/>
__Gray characters are also like yellow characters: (CHARACTER, CHARACTER)__<br/><br/>
SO this is how you should Run the script:<br/>
```
python main.py
green characters with it's indexes seperated with comma (like: m1, n3): t1, i2, e4
orange characters (like: p,o,l): r
removed characters (like: g,r,t): w, a, y, s
```
