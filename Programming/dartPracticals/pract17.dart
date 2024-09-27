import 'dart:io';

void main() {
  // String text = '@myport.ac.uk';
  // print(isValidEmail(text));

  // print(removeMilk({'milkshake', 'yoghurt', 'burger', 'banana milk', 'milk'}));

  // Map<String, double> prices = {
  //   'Tesco Finest Yogurt': 0.90,
  //   'Robinson\'s orange squash': 2.00,
  //   'Tesco Finest Macaroni Cheese': 4.25,
  //   'Doritos Cool Original': 1.20,
  //   'Milk': 1.20,
  // };
  // priceRise(prices);
  // print('After price rises: $prices');

  //print(capitalize('hello'));

  // print(extractHashtags(['Learning #Dart and #Flutter is fun!']));

  print(capitalize2(
      'Update your capitalize function so that it can also capitalize a sentence'));
}

bool isValidEmail(String? text) {
  try {
    String email = text!;
    if (email.contains('@myport.ac.uk')) {
      return true;
    } else {
      return false;
    }
  } catch (e) {
    return false;
  }
}

bool checkExpenses(List<double> expenses, double limit) {
  for (double expense in expenses) {
    if (expense > limit) {
      return false;
    } else {
      return true;
    }
  }
  return false;
}

double weatherDifference(List<double> temperatures) {
  double difference = temperatures[0] - temperatures[-1];
  if (difference < 0) {
    difference = difference * -1;
  }
  return difference;
}

Set removeMilk(Set<String> foods) {
  foods.remove('milk');
  return foods;
}

Map capMarks(String module, Map<String, List<int>> marks) {
  try {
    List<int> moduleMarks = marks[module]!;
    for (int i = 0; i < moduleMarks.length; i++) {
      if (moduleMarks[i] > 40) {
        moduleMarks[i] = 40;
      }
    }
    marks[module] = moduleMarks;
    return marks;
  } catch (e) {
    print('Module not found');
    return marks;
  }
}

void priceRise(Map<String, double> productPrices) {
  for (String product in productPrices.keys) {
    if (product.contains('Tesco Finest')) {
      double newPrice = productPrices[product]!;
      print('Price of $product is £$newPrice');
      productPrices[product] = newPrice * 1.1;
    }
  }
}

String capitalize(String text) {
  String firstLetter = text[0].toUpperCase();
  String restOfText = text.substring(1);
  return firstLetter + restOfText;
}

Set extractHashtags(List<String> posts) {
  Set<String> hashtags = {};
  for (String post in posts) {
    for (String word in post.split(' ')) {
      if (word.startsWith('#')) {
        hashtags.add(word);
      }
    }
  }
  return hashtags;
}

String capitalize2(String text) {
  String capitalizedText = '';
  for (String word in text.split(' ')) {
    String firstLetter = word[0].toUpperCase();
    String restOfText = word.substring(1);
    capitalizedText += firstLetter + restOfText + ' ';
  }
  return capitalizedText;
}

String snakeToCamel(String text) {
  String camelText = '';
  for (String word in text.split('_')) {
    String firstLetter = word[0].toUpperCase();
    String restOfText = word.substring(1);
    camelText += firstLetter + restOfText;
  }
  return camelText;
}

void compress(int n, String text) {}

// void main() {
//   print('Uncomment the code in this file to run it');

// iterateString('Hello, World!');
// iterateString('👨‍👩‍👧‍👦');
// iterateString('Café');

// substringDemo();

// String line = 'Stella! Hey Stella!';
// print(line.toUpperCase());
// print(line.toLowerCase());

// stringChecker('Hello, World!', 'World');
// stringChecker('Hello, World!', 'World!');
// stringChecker('Hello, World!', 'Hello, World!');
// stringChecker('Hello, World!', 'o');
// stringChecker('Hello, World!', 'Moon');

// String littleWomen = 'Jo and Beth and Amy and Meg';
// for (String name in littleWomen.split(' and ')) {
//   print(name);
// }

// stringSplitDemo();

// listDemo();

// List<List<double>> matrix = [
//   [9.7, 8.4, 7.6],
//   [0.9, 0.8, 0.7],
//   [6.5, 5.3, 4.2],
//   [3.1, 2.6, 1.7],
// ];

// print('First row: ${matrix[0]}');
// print('Second element of the third row: ${matrix[2][1]}');

// for (int row = 0; row < matrix.length; row++) {
//   for (int col = 0; col < matrix[row].length; col++) {
//     stdout.write('${matrix[row][col]} ');
//   }
//   print(''); // New line
// }

// setDemo();

// setIteration();

// Map<int, String> orders = createOrders();
// for (int orderNumber in orders.keys) {
//   print('Order $orderNumber: ${orders[orderNumber]}');
// }

// Map<String, double> prices = {
//   'Tesco Finest Yogurt': 0.90,
//   'Robinson\'s orange squash': 2.00,
//   'Tesco Finest Macaroni Cheese': 4.25,
//   'Doritos Cool Original': 1.20,
//   'Milk': 1.20,
// };
// priceRise(prices);
// print('After price rises: $prices');

// listOfMapsDemo();
// }

void substringDemo() {
  String postcode = 'PO13HF';
  int startIndex = 3, endIndex = 5;
  print('The substring of "$postcode" from $startIndex to $endIndex is ' +
      postcode.substring(startIndex, endIndex));
  print('The substring of "$postcode" from $startIndex to the end is ' +
      postcode.substring(startIndex));
  print('The last 3 characters of "$postcode" are ' +
      postcode.substring(postcode.length - 3));
}

void iterateString(String text) {
  for (int i = 0; i < text.length; i++) {
    var char = text[i];
    print(char);
  }
}

void stringChecker(String text, String substring) {
  String output =
      'The index of "$substring" in "$text" is ${text.indexOf(substring)} and ';

  if (text.startsWith(substring))
    output += 'the text starts with the substring';
  else if (text.endsWith(substring))
    output += 'the text ends with the substring';
  else if (text.contains(substring))
    output += 'the text contains the substring';
  else
    output += 'the text does not contain the substring';

  print(output);
}

void stringSplitDemo() {
  String letters = 'abcdefg';
  List<String> splitted = letters.split('');
  print(splitted[2]);

  String joined = splitted.join(' ');
  print(joined);
}

// List<bool> getAvailability() {
//   List<bool> availability = List.filled(7, true);
//   for (int i = 0; i < 7; i++) {
//     print('Do you have any classes on day ${i + 1}? (yes/no)');
//     String? response = stdin.readLineSync();
//     if (response == 'yes') {
//       availability[i] = false;
//     }
//   }
//   return availability;
// }

// The same function but with a for-in loop
List<bool> getAvailability() {
  List<bool> availability = List.filled(7, true);
  List<String> days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'];
  for (String day in days) {
    print('Do you have any classes on $day? (yes/no)');
    String? response = stdin.readLineSync();
    if (response == 'yes') {
      int index = days.indexOf(day);
      availability[index] = false;
    }
  }
  return availability;
}

void addAndRemoveElements() {
  List<String> fruits = ['Apple', 'Banana', 'Cherry'];
  print('Initial list: $fruits');

  fruits.add('Pear');
  print('Added Pear: $fruits');

  fruits.insert(1, 'Blueberry');
  print('Inserted Blueberry at index 1: $fruits');

  fruits.remove('Banana');
  print('Removed Banana: $fruits');
}

void listDemo() {
  List<int> marks = [100, 60, 40, 87, 54];
  print('In the first in-class test, I got %${marks.first}');
  print('In the second in-class test, I got %${marks[1]}');
  print('But in the last coursework, my mark was ${marks.last}');
  int numberOfMarks = marks.length;
  int lastIndex = numberOfMarks - 1;
  marks[lastIndex] = 90;
  print('After the remark, my last mark is ${marks.last} 😂');
}

void setDemo() {
  Set<int> numbers = {1, 2, 3, 4};
  print('Initial set: $numbers');
  print('Length of the set: ${numbers.length}');
  print('Is 3 in the set? ${numbers.contains(3)}');

  numbers.add(5);
  print('After adding 5: $numbers');

  numbers.add(2);
  print('After adding 2: $numbers');

  numbers.remove(3);
  print('After removing 3: $numbers');
}

void setIteration() {
  Set<String> fruits = {'apple', 'banana', 'orange'};
  print('Fruits:');
  for (String fruit in fruits) {
    print(fruit);
    fruit = fruit.toUpperCase(); // This doesn't change the set
  }

  // Checking if the set is still the same
  print(fruits);
}

Map<int, String> createOrders() {
  Map<int, String> orders = {
    1: 'Milkshake',
    2: 'Burger',
    3: 'Chicken wrap',
  };
  print('Initial orders: $orders');

  orders[4] = 'Salad';
  print('Added Salad: $orders');

  orders.remove(2);
  print('Removed Burger: $orders');

  return orders;
}

// void priceRise(Map<String, double> productPrices) {
//   if (productPrices.containsKey('Milk')) {
//     print('Price of milk is £${productPrices['Milk']}');
//   }
//   productPrices['Milk'] = productPrices['Milk']! + 0.20;
// }

void listOfMapsDemo() {
  List<Map<String, Object>> games = [
    {
      'title': 'Call of Duty',
      'price': 49.99,
      'platforms': ['PlayStation', 'Xbox', 'PC']
    },
    {
      'title': 'Warhammer',
      'price': 29.99,
      'platforms': ['PC', 'macOS']
    },
    {
      'title': 'Fortnite',
      'price': 0.00,
      'platforms': ['PlayStation', 'Xbox', 'PC'],
    },
  ];
  for (Map<String, Object> game in games) {
    print('${game['title']} costs £${game['price']}'
        ' and is available on ${game['platforms']}');
  }

  for (Map<String, Object> game in games) {
    List<String> platforms = game['platforms'] as List<String>;
    if (platforms.contains('PlayStation')) {
      print('${game['title']} costs £${game['price']}'
          ' and is available on PlayStation');
    }
  }
}
