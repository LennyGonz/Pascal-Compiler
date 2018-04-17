# Pascal Compiler
This is a Pascal compiler built using Python, for Compiler Construction

# Resources used for this project:
* [Pascal Keywords](http://wiki.freepascal.org/Reserved_words)
* [Pascal Operators](http://www.tutorialspoint.com/pascal/pascal_operators.htm)
* [Symbol Tables](http://en.wikipedia.org/wiki/Symbol_table)
* [System Functions](http://www.freepascal.org/docs-html/rtl/system/index-5.html)
* [Data Types](http://wiki.freepascal.org/Variables_and_Data_Types) 

## Compiler Theory
* [Parsers and Compilers](http://parsingintro.sourceforge.net/#contents_item_7)
* [How does an interpreter/compiler work?](http://forums.devshed.com/programming-languages-139/interpreter-compiler-312483.html#post1342279)

## Parsing Methods
* [More notes on Recursive Parsing](http://math.hws.edu/javanotes/c9/s5.html)
* [Top Down Recursive Parsing](https://www.cs.duke.edu/~raw/cps218/Handouts/TDRD.htm)
* [Pascal Grammar](https://www.cs.utexas.edu/users/novak/grammar.html)

# How does an interpreter/compiler work?

A very simple form of a compiler/interpreter:

Source File ==> Scanner ==> Lexer ==> Parser ==> Interpreter/Code Generator

1. **Source File**: This is the program that is read by the interpreter/compiler. This is the text that needs to be compiled or interpreted.

2. **Scanner**: This is the first **module** in a compiler/interpreter/
	* The job of a scanner is to read the source file, one character at a time.
	* It also keeps track of which line number and character is currently being read.
	* A typical scanner can be instructed to move backwards and forwards through the source file.
		* Why do we need to move backwards?
	* For now assume that each time the scanner is called:
		* it returns the next character in the file

3. **Lexer**: This module serves to break up the source file into chunks(called tokens). It calls the scanner to get characters one at a time and organizes them into:
	* tokens
	* token types

<pre>
cx = cy + 324;
print "value of cx is ", cx;
</pre>

**A lexer would break it like this**:

<pre>
cx                 --> Identifier       (variable)
=                  --> Symbol           (assignment operator)
cy                 --> Identifier       (variable)
+                  --> Symbol           (addition operator)
324                --> Numeric Constant (integer)
;                  --> Symbol           (end of statement)
print              --> Identifier       (keyword)
"value of cx is "  --> String Constant  (string)
,                  --> Symbol           (string concatentation operator)
cx                 --> Identifier       (variable)
</pre>

* The lexer calls the **scanner** to pass it **one character at a time**
* Then lexer groups them together(groups characters together) and identifies them up as **tokens** for the language parser (which is the next stage)
* SO basically **TOKENS** are characters grouped together
* The lexer also identifies the type of token: 
	* variable vs keyword
	* assignment operator vs addition operator vs string concatentation operator etc
* Occasionally, the lexer has to tell the scanner to **back up**.
	* Consider a language that has operators that may be more than one character long
		* For example ! vs !=
		* < vs <=
		* '+' vs ++
* If we assume that the lexer needs to determine whether the operator is a < or a <=, the lexer will request the scanner for another character.
* If the next character is a '=', it changes the **token** to "<=" and passes it to the parser
* If **not**, it tells the scanner to back up one character and hold it in the buffer, while it passes the '<' to the parser.

4. **Parser**: This is the part of the **compiler** that really understand the syntax of the language<br>
* It calls the lexer to get **tokens** and prcessess the tokens per the syntax of the language
* For example, taking the example from the lexer above, the hypothetical interaction between the lexer and paraser could go like this:

-----------------------------------------------------------------------------------
Parser: Give me the next token <br>
Lexer : Next token is "cx" which is a variable. <br>
Parser: Ok, I have "cx" as a declared integer variable. Give me next token <br>
Lexer : Next token is "=", the assignment operator. <br>
Parser: Ok, the program wants me to assign something to "cx". Next token <br>
------>	Lexer : The next token is "cy" which is a variable. <br>
------>	Parser: Ok, I know "cy" is an integer variable. Next token please <br>
------>	Lexer : The next token is '+', which is an addition operator. <br>
------>	Parser: Ok, so I need to add something to the value in "cy". Next token please. <br>
-------------->	Lexer: The next token is "324", which is an integer. <br>
-------------->	Parser: Ok, both "cy" and "324" are integers, so I can add them. Next token please: <br>
-------------->	Lexer: The next token is ";" which is end of statement. <br>
------>	Parser: Ok, I will evaluate "cy + 324" and get the answer <br>
Parser: I'll take the answer from "cy + 324" and assign it to "cx" <br>

------------------------------------------------------------------------------------
In the section above, the **indenting** shows a subprocess that the parsers enters
to evaluate "cy+324". This gives an idea about how the parser operates.
* Also note that the parser is checking types and syntax rules (for instance, it checked whether cy and 324 were both integer types before adding them).
* If the parser gets a token that it was not expecting, it will stop processing and complain to the user about an error.
* The scanner holds the current line number and character, so the Parser can inform the user approximately where the error occured.

5. **Interpreter/Code Generator**: This is the part that actually takes the action that is specified by a program statement.
* In some bases, this is actually part of the parser(especially for interpreters)
	* The parser interprets and takes action directly 
* In other cases, the parser converts the statements into byte-code
* In the case of a compiler, it then hands them to the Code Generator to convert into machine code instructions
* If you want a compiler for a different CPU or architecture, all you have to do is put a new code generator unit to translate the byte code into machine code for the new CPU

## Scripts
'scanner.py'
'parser.py'
'simulator.py'
'emulator.py'