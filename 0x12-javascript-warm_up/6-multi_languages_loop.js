#!/usr/bin/node
/*
    Auth: codenvibes
    Desc: JS script - Prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop.
        - The first line: “C is fun”
        - The second line: “Python is cool”
        - The third line: “JavaScript is amazing”
        - You can use only one console.log
        - You must use a loop (while, for, etc.)
*/
languages = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
for (let index = 0; index < languages.length; index++) {
  console.log(languages[index]);
}
