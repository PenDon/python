// https://www.baibianip.com/home/free.html
function ddip(e0) {
  var Base64 = {
    _keyStr: "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",
    encode: function(e) {
      var t = "";
      var n, r, i, s, o, u, a;
      var f = 0;
      e = Base64._utf8_encode(e);
      while (f < e.length) {
        n = e.charCodeAt(f++);
        r = e.charCodeAt(f++);
        i = e.charCodeAt(f++);
        s = n >> 2;
        o = (n & 3) << 4 | r >> 4;
        u = (r & 15) << 2 | i >> 6;
        a = i & 63;
        if (isNaN(r)) {
          u = a = 64
        } else if (isNaN(i)) {
          a = 64
        }
        t = t + this._keyStr.charAt(s) + this._keyStr.charAt(o) + this._keyStr.charAt(u) + this._keyStr.charAt(a)
      }
      return t
    },
    decode: function(e) {
      var t = "";
      var n, r, i;
      var s, o, u, a;
      var f = 0;
      e = e.replace(/[^A-Za-z0-9+/=]/g, "");
      while (f < e.length) {
        s = this._keyStr.indexOf(e.charAt(f++));
        o = this._keyStr.indexOf(e.charAt(f++));
        u = this._keyStr.indexOf(e.charAt(f++));
        a = this._keyStr.indexOf(e.charAt(f++));
        n = s << 2 | o >> 4;
        r = (o & 15) << 4 | u >> 2;
        i = (u & 3) << 6 | a;
        t = t + String.fromCharCode(n);
        if (u != 64) {
          t = t + String.fromCharCode(r)
        }
        if (a != 64) {
          t = t + String.fromCharCode(i)
        }
      }
      t = Base64._utf8_decode(t);
      return t
    },
    _utf8_encode: function(e) {
      e = e.replace(/rn/g, "n");
      var t = "";
      for (var n = 0; n < e.length; n++) {
        var r = e.charCodeAt(n);
        if (r < 128) {
          t += String.fromCharCode(r)
        } else if (r > 127 && r < 2048) {
          t += String.fromCharCode(r >> 6 | 192);
          t += String.fromCharCode(r & 63 | 128)
        } else {
          t += String.fromCharCode(r >> 12 | 224);
          t += String.fromCharCode(r >> 6 & 63 | 128);
          t += String.fromCharCode(r & 63 | 128)
        }
      }
      return t
    },
    _utf8_decode: function(e) {
      var t = "";
      var n = 0;
      var r = c1 = c2 = 0;
      while (n < e.length) {
        r = e.charCodeAt(n);
        if (r < 128) {
          t += String.fromCharCode(r);
          n++
        } else if (r > 191 && r < 224) {
          c2 = e.charCodeAt(n + 1);
          t += String.fromCharCode((r & 31) << 6 | c2 & 63);
          n += 2
        } else {
          c2 = e.charCodeAt(n + 1);
          c3 = e.charCodeAt(n + 2);
          t += String.fromCharCode((r & 15) << 12 | (c2 & 63) << 6 | c3 & 63);
          n += 3
        }
      }
      return t
    }
  }

  e1 = r13(e0.toString());
  e2 = Base64.decode(e1);
  e3 = e2.toString().substr(10);
  l3 = e3.length;
  e4 = e3.substr(0, l3 - 10);
  return e4;
}

function r3(str) {
  var newarr = [];
  for (var i = 0; i < str.length; i++) {
    if (str.charCodeAt(i) < 65 || str.charCodeAt(i) > 90) {
      newarr.push(str.charAt(i));
    } else if (str.charCodeAt(i) > 77) {
      newarr.push(String.fromCharCode(str.charCodeAt(i) - 13));
    } else {
      newarr.push(String.fromCharCode(str.charCodeAt(i) + 13));
    }
  }
  return newarr.join('');
}

function rot(t, u, v) {
  return String.fromCharCode(((t - u + v) % (v * 2)) + u);
}

function r13(s) {
  var b = [], c, i = s.length, a = 'a'.charCodeAt(),
    z = a + 26, A = 'A'.charCodeAt(), Z = A + 26;
  while (i--) {
    c = s.charCodeAt(i);
    if (c >= a && c < z) {
      b[i] = rot(c, a, 13);
    } else if (c >= A && c < Z) {
      b[i] = rot(c, A, 13);
    } else {
      b[i] = s.charAt(i);
    }
  }
  return b.join('');
}

function rot5(s) {
  var b = [], c, i = s.length, a = '0'.charCodeAt(),
    z = a + 10;
  while (i--) {
    c = s.charCodeAt(i);
    if (c >= a && c < z) {
      b[i] = rot(c, a, 5);
    } else {
      b[i] = s.charAt(i);
    }
  }
  return b.join('');
}

function rot135(s) {
  return rot13(rot5(s));
}

document.write(ddip('ZGLlZQLjZmN0ZmR2AF4lZwHhZmLhAwxkAwZkZQL0BGp4'))
