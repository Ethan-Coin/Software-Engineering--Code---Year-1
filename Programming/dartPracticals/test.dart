void main() {
  String email = 'up1234567@myport.ac.uk';
  print(isValidEmail(email));
}

bool isValidEmail(String email) {
  int last = email.length;
  int start = last - 12;
  if (email.contains('@myport.ac.uk')) {
    if (email.substring(start, last) == 'myport.ac.uk') {
      return true;
    } else {
      return false;
    }
  } else {
    return false;
  }
}
