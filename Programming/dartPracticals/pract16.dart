import 'dart:io';
import 'dart:math';

void main() {
  // int num1 = 4;
  // int num2 = 3;
  // print(maxNumbers2(num1, num2));

  // print(daysInMonth(2));

  // print(euroToPounds(2));

  // print(isPrime(4));

  // print(gcd(27, 3));
}

double maxNumbers(double num1, double num2) {
  if (num1 > num2) {
    return num1;
  } else {
    return num2;
  }
}

double maxNumbers2(double num1, double num2) {
  return max(num1, num2);
}

int daysInMonth(int month) {
  if (month == 2) {
    return 28;
  } else if (month == 4 || month == 6 || month == 9 || month == 11) {
    return 30;
  } else {
    return 31;
  }
}

double euroToPounds(double euro) => euro * 0.86;

double fahrenheitToCelsius(double fahrenheit) => (fahrenheit - 32) * 5 / 9;

double circumferenceOfCircle2(double radius) => 2 * pi * radius;

String heartMonitor(int age, int bpm) {
  int maxHeartRate;
  if (age <= 20) {
    maxHeartRate = 170;
  } else if (age <= 40) {
    maxHeartRate = 155;
  } else if (age <= 60) {
    maxHeartRate = 140;
  } else if (age <= 80) {
    maxHeartRate = 130;
  } else {
    maxHeartRate = 100;
  }

  if (bpm > maxHeartRate) {
    return "High heart rate for $age";
  } else {
    return "Normal heart rate for $age";
  }
}

double basicCalculator(double num1, double num2, String operator) {
  if (operator == 'add') {
    return num1 + num2;
  } else if (operator == 'subtract') {
    return num1 - num2;
  } else if (operator == 'multiply') {
    return num1 * num2;
  } else if (operator == 'divide') {
    return num1 / num2;
  } else {
    return 0;
  }
}

String isPrime(int num) {
  if (num < 2) {
    return "Not prime";
  }
  for (int i = 2; i <= sqrt(num); i++) {
    if (num % i == 0) {
      return "Not prime";
    }
  }
  return "Prime";
}

int gcd(int num1, int num2) {
  if (num1 == num2) {
    return num1;
  } else if (num1 > num2) {
    return gcd(num1 - num2, num2);
  } else {
    return gcd(num1, num2 - num1);
  }
}

void customisedGreeting() {
  print('Enter time (between 0 and 2359):');
  String? timeInput = stdin.readLineSync();
  int? time = null;
  while (true) {
    time = int.tryParse(timeInput!);
    if (time == null) {
      print("Your input was not a number.");
      continue;
    } else if (time < 0 || time > 2359) {
      print("Your number must be between 0 and 2359.");
      continue;
    } else {
      print("You have selected $time.");
      break;
    }
  }

  String greeting;
  if (time >= 600 && time < 1200) {
    greeting = 'Have a great morning!';
  } else if (time >= 1200 && time < 1800) {
    greeting = 'Have a wonderful afternoon!';
  } else if (time >= 1800 && time < 2200) {
    greeting = 'Have a pleasant evening!';
  } else {
    greeting = 'Have a peaceful night!';
  }
  print(greeting);
}

void exceptionHandlingDemo() {
  try {
    var numbers = [1, 2, 3];
    print('The fourth number is ${numbers[3]}');
  } on RangeError {
    print('Caught a RangeError!');
  } catch (e) {
    print('An unknown error occurred: $e');
  } finally {
    print('This line will always be executed');
  }
}

int factorial(int n) {
  int result = 1;
  for (int i = 1; i <= n; i++) {
    result = result * i;
  }
  return result;
}

int getSize() {
  int size = 0;
  while (size != 5 && size != 7 && size != 9) {
    print("Enter a size (5, 7 or 9):");
    String? input = stdin.readLineSync();
    size = int.parse(input!);
  }
  return size;
}

int getSize2() {
  int? size = null;
  while (true) {
    print("Enter a size (5, 7 or 9):");
    String? input = stdin.readLineSync();
    if (input == null) {
      print("That was not a valid input.");
      continue;
    }
    size = int.tryParse(input);
    if (size == null) {
      print("Your input was not a number.");
      continue;
    } else if (size != 5 && size != 7 && size != 9) {
      print("Your number must be 5, 7 or 9.");
      continue;
    } else {
      print("You have selected $size.");
      break;
    }
  }
  return size;
}
