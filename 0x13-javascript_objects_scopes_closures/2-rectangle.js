#!/usr/bin/node
/*
    Auth: codenvibes
    Desc: JS script - a class Rectangle that defines a rectangle:
*/
module.exports = class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
