import 'dart:io';
import 'dart:math';

void main() {
  print(hypotenuseOfTriangle(3, 4));
}

void sayName() {
  print('Ethan');
}

void studentDetails() {
  print('''My name is Ethan Schultz
My student number is 2200330
My email address is: up2200330@myport.ac.uk''');
}

double euroToPounds(double euro) {
  double pound = euro * 0.86;
  return pound;
}

double fahrenheitToCelsius(double fahrenheit) {
  double celsius = (fahrenheit - 32) * 5 / 9;
  return celsius;
}

void circumferenceOfCircle() {
  print('Enter the radius of a circle:');
  String? radiusInput = stdin.readLineSync();
  double radius = double.parse(radiusInput!);
  double circumference = 2 * pi * radius;
  print('Circumference: ${circumference.toStringAsFixed(2)}');
}

void areaOfCircle() {
  print('Enter the radius of a circle');
  String? radiusInput = stdin.readLineSync();
  double radius = double.parse(radiusInput!);
  double area = pi * pow(radius, 2);
  print('Area: ${area.toStringAsFixed(2)}');
}

double circumferenceOfCircle2(double radius) {
  double circumference = 2 * pi * radius;
  return circumference;
}

double areaOfCircle2(double radius) {
  double area = pi * pow(radius, 2);
  return area;
}

void circleInfo() {
  print('Enter radius of the circle:');
  String? radiusInput = stdin.readLineSync();
  double radius = double.parse(radiusInput!);
  double circumference = circumferenceOfCircle2(radius);
  double area = areaOfCircle2(radius);
  print(
      'Circumference: ${circumference.toStringAsFixed(2)}\nArea: ${area.toStringAsFixed(2)}');
}

void displayBurgerOrder(int burgers, double price) {
  double total = price * burgers;
  print('Your order: ${'🍔' * burgers}\nTotal: ${total.toStringAsFixed(2)}');
}

int howManyBurgers(double price, double bal) {
  int burgers = bal ~/ price;
  return burgers;
}

double hypotenuseOfTriangle(double sideA, double sideB) {
  double hyptoenuse = sqrt(pow(sideA, 2) + pow(sideB, 2));
  return hyptoenuse;
}
// web app module completion