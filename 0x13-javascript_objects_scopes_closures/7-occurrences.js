#!/usr/bin/node
/*
    Auth: codenvibes
    Desc: JS script - a function that returns the number of occurrences in a list
*/
exports.nbOccurences = function (list, searchElement) {
  let occur = 0;

  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      occur++;
    }
  }
  return occur;
};
