#!/usr/bin/node
/*
    Auth: codenvibes
    Desc: A JS script that prints two arguments passed to it, in the following format: “ is ”
        - You must use console.log(...) to print all output
        - You are not allowed to use var
*/
const cmdArgs = process.argv;
if (cmdArgs[2] && cmdArgs[3]) {
  console.log(cmdArgs[2] + ' is ' + cmdArgs[3]);
} else if (cmdArgs[2] && !cmdArgs[3]) {
  console.log(cmdArgs[2] + ' is undefined');
} else {
  console.log('undefined is undefined');
}
