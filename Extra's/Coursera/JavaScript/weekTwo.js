/*function letterFinder(word,match){
    for(var i = 0;i<word.length;i++){
        if (word[i] == match){
            console.log('Found the', match, 'at', i);
        }
        else{
            console.log('---No match found at', i);
        }
    }
}
letterFinder("test","t");*/

//Exercise error prevention
/*task 1
function addTwoNums(a,b) {
    console.log(a + b) //display the result
}*/
/*task 2
function addTwoNums(a,b) {
    console.log(a + b)
}
addTwoNums(5, "5") // "55"*/
/*task 3
function addTwoNums(a,b) {
    try {
        console.log(a + b)
    } catch(err) {
        console.log(err)
    }
}
//task 4
function addTwoNums(a,b) {
    try {
        if (typeof(a) != "number"){
            throw new ReferenceError('the first argument is not a number');
        }
        else if (typeof(b) != "number"){
            throw new ReferenceError('the second argument is not a number');
        }
        else{
            console.log(a+b)
        } 
    } catch(err) {
           console.log(err) 
    }
}
//task 5
function addTwoNums(a,b) {
    try {
        if (typeof(a) != "number"){
            throw new ReferenceError('the first argument is not a number');
        }
        else if (typeof(b) != "number"){
            throw new ReferenceError('the second argument is not a number');
        }
        else{
            console.log(a+b)
        } 
    } catch(err) {
           console.log("Error!", err)
    }
}*/
//task 6
/*function addTwoNums(a,b) {
    try {
        if (typeof(a) != "number"){
            throw new ReferenceError('the first argument is not a number');
        }
        else if (typeof(b) != "number"){
            throw new ReferenceError('the second argument is not a number');
        }
        else{
            console.log(a+b)
        } 
    } catch(err) {
           console.log("Error!", err)
    }
}
addTwoNums(5,"5")
console.log("It stills works")*/
/*Exercise defensive programming
function letterFinder(word, match) {
    var condition1 = typeof(word) == 'string' && word.length >= 2;
    var condition2 = typeof(match) == "string" && match.length == 1;
    if (condition1 && condition2){
        for(var i = 0; i < word.length; i++) {
            if(word[i] == match) {
                //if the current character at position i in the word is equal to the match
                console.log('Found the', match, 'at', i)
            } else {
                console.log('---No match found at', i)
            }
        }        
    }
    else{
        console.log("Please pass correct arguments to the function.")
    }
}
letterFinder("cat", "c")
*/


// try {
//     Number(5).toPrecision(300)
//     } catch(e) {
//     console.log("There was an error")
//     }

var h1  = document.querySelector("h1");
var arr = [
        'Example Domain',
        'First Click',
        'Second Click',
        'Third Click'
    ]

function handleClicks() {
    switch (h1.innerText){
        case arr[0]:
            h1.innerText = arr[1];
            break;
        case arr[1]:
            h1.innerText = arr[2];
            break;
        case arr[2]:
            h1.innerText = arr[3];
            break;
        default:
            h1.innerText = arr[0];
    }
}

h1.addEventListener('click', handleClicks);