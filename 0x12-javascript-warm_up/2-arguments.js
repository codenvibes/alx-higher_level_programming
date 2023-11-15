#!/usr/bin/node
/*
    Auth: codenvibes
    Desc: A JS script that prints a message depending of the number of arguments passed:
        - If no arguments are passed to the script, print “No argument”
        - If only one argument is passed to the script, print “Argument found”
        - Otherwise, print “Arguments found”
*/
const cmdArgs = process.argv.length;
if (cmdArgs === 2) {
    console.log('No argument');
} else if (cmdArgs === 3) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
