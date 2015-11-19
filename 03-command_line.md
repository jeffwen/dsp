# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

1. `less`/`more` = allows the user to page through long files. Less allows the user to move forward and backwards in the file while more only allows for forward movement.
2. `|` = pipe command that allows for mny uses. It allows for chained utlities to take the output of one utility and use it as input for the next utility.
3. `sort` = will sort the contents of a file, can be used in combination with uniq, which will find the unique, consecutive items from the input and return only one occurence.
4. `grep` = searching within files. Especially with the -i option, which allows for case insensitive searching
5. `rm -rf` = remove utility but with the recursive and force options can be used for removing entire directories
6. `sed` = stream editor, which allows for search and replacing within the command line
7. `pushd`/ `popd` = store the current working directory in a stack and go to another directory temporarily; popd returns the previous saved working directory
8. `xargs` = allows for long input argument lists to be passed to utlities that only take one argument.
9. `find` = search for file names or other depending on the options placed
10. `wc` = count the number of lines, words, and characters

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

>> `ls` lists the files and directories in the present working directory.

>> The -a option will list all of the hidden files and directories as well as the visible ones. -l lists the contents in a long format that provides more information about each file and directory. -ls will list contents in long format, but the -h will change the size suffix to be the size of the file so B for bytes, M for megabytes, etc. Whereas without the -h the size would just be a numerical representation that might be really long. (79275 will be represented as 77K).

---


---

What does `xargs` do? Give an example of how to use it.

>> The `xargs` command takes in a standard input and will split up the standard input so that it can be passed to utlities that may otherwise not be able to take such long inputs. Additionally, some utilities do not accept standard inputs and instead the input is required to be spelled out (for example: rm, touch, cp, etc.). xargs, when used with these utilities will take an input and split the input into individual arguments that can then be passed into these utilities.

>> The below example searches in the current directory (and other subdirectories) for files ending in .txt and removes these files.

```bash
$ find . -name "*.txt" -print0 | xargs -0 rm -rf
```


---

