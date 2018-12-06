// Madlib

// function madlib(name,subject){
//     console.log(name+"\'s favorite subject in school is "+subject)
//  }
//  madlib('Anushaka','art');

// function tipAmount(amount,service){

//     if(service=="good"){ 
//         tipamount=(amount*20)/100;
//         console.log(tipamount);
        
//     }
//     else if(service =="fair"){
//         tipamount=(amount*15)/100;
//         console.log(tipamount);
//     }
//         else if(service=="bad"){
//             tipamount=(amount*10)/100;
//             console.log(tipamount);

//         } 

// }
// // tipAmount(100,'good')
// tipAmount(40,'fair')


// Tip Calculator 2 

// f

// Print Numbers

// function printNumbers(start,end){
//     for (start; start<=end;start++){
//         console.log(start)
//     }
// }
// printNumbers(1,10);


// using while loop:
// function printNumbers(start,end){

//     while(start<=end){
//         console.log(start)
//         start+=1
//     }

// }

// printNumbers(1,10)

// Print a Square
// Write a function printSquare which is given a size and prints a square of that size using asterisks

    // function printSquare(size){
    //       var stringArr=[] 
    //       var str="*"
    //     for(var i=1;i<=size;i++){
    //          stringArr.push(str)
    //     }
    //     // console.log(stringArr)
    //     var final=stringArr.join("")
    //     // console.log(final)

    //     for(var i=1;i<=size;i++){
    //        console.log(final)
    //     }    
    // }
    //    printSquare(3)
    //       printSquare(5);


    
    
    // Print a box
    // Write function printBox which is given a width and height and prints a hollow box of those given dimensions
    function printSquare(width,height){
        var stringArr=[]
        var fArray=[] 
        var str="*"
        var empstr=" " 
      for(var i=1;i<=height;i++){
            if(i == 1||height) {
                for(i=1;i<=width;i++){
                  stringArr.push(str)
                }
                console.log(stringArr)
                var ele=stringArr.join("")
                console.log(ele)
                fArray.push(ele)
            }
            else {
                for(i=1;1<=width;i++){
                    if(i == 1||width){
                      stringArr.push(str)
                    }
                    else{
                        stringArr.push(empstr)
                    }
                     var emele= stringArr.join("")
                     console.log(emele);
                     fArray.push(emele);
                    }
                 
              }
        
         console.log(stringArr)
         for(var i=1;i<=height;i++){
          console.log(stringArr[i])
      }    
  }
     printSquare(6,4)

    // function lvl1exercise1() {
    //     // Declare a variable without instantiating it and return it!
    //      var i;
    //      return i;
    // }
    //  var num=lvl1exercise1();
    //  console.log(num)
    
    // function lvl1exercise2() {
    //     // Declare and instantiate a number and return it
       
    //     var j=4;
    //     return j;
         
    
    // }
    //  var num= lvl1exercise2()
    //  console.log(num)
    
    // function lvl1exercise3() {
    //     // Declare and instantiate a floating point number that isn't a whole number and return it
    //      var i=3.4;
    //      return i;
    // }
    // var flt=lvl1exercise3();
    // console.log(flt)

    
    // function lvl1exercise5() {
    //     // Declare and instantiate an array containing the string "Hello World!" and the number 4 and return it
    //      var arr=["Hello World",4]
    //      return arr;
    // }
    // var arr1=lvl1exercise5() 
    // console.log(arr1)
    // function lvl1exercise6() {
    //     // Declare and instantiate an object containing the key-value pairs key1 -> "Hello World!" and key2 -> 4, and return it
    //      var obj1={
    //          key1:"Hello World",
    //          key2:4
    //      }
    //      return obj1;
    // }
    // var objval=lvl1exercise6()
    // console.log(objval)

    // function lvl2exercise1(num1, num2) {
    //     // Return the sum of num1 and num2
    //     return num1+num2;
    
    // }
    // var sum=lvl2exercise1(100,1000)
    // console.log(sum)
    
    // function lvl2exercise2(num1, num2) {
    //     // Return the difference of num1 and num2
    //        return num1-num2;
    // }
    // var diff=lvl2exercise2(10,100);
    // console.log(diff)
    
    // function lvl2exercise3(num1, num2) {
    //     // Return the multiplication of num1 and num 2
    //       return num1*num2
    // }
    // var mul =lvl2exercise3(2.5,2.3)
    // console.log(mul)
    
    // function lvl2exercise4(num1, num2) {
    //     // Return the division of num1 and num2
    //     return num1/num2;
    
    // }
    //  var div=lvl2exercise4(20,5)
    //  console.log(div)
    // function lvl2exercise5(num1) {
    //     // Add 2 to num1 using += and return it
    //      return num1+=2
    // }
    // var plus2=lvl2exercise5(1000.5)
    // console.log(plus2)
    
    // function lvl3exercise1() {
    //     // Create a "hello" and a "world", return the concatenation of the two
    //     str1="hello"
    //     str2="world"
    //     var str=str1.concat(str2)
    //     return str 
           
    // }
    //   var strcon=lvl3exercise1()
    //   console.log(strcon)

    
    // function lvl3exercise2() {
    //     // Create a "hello" and a 12, return the concatenation of the two
    //     var str="hello"
    //     var num=12
    //     var strnum=str.concat(num)
    //     return strnum;
    // }
    //  var strnum1=lvl3exercise2()
    //  console.log(strnum1)

    
    // function lvl3exercise3() {
    //     // Create a variable that equals 12 and convert it to a string with concatenation. Return it.
    //     var num1=12;
    //     var numstr = (num1.toString()).concat(num1);
    //     return numstr;

    // }
    // var out=lvl3exercise3()
    // console.log(out)
    
    // function lvl3exercise4() {
    //     // Create a "hello world!" string. Return the length of the string
    //    var str2="hello world!";
    //    var len =str2.length
    //    return len;
    // }

    // var out =lvl3exercise4()
    // console.log(out)
    
    
    // function lvl3exercise5() {
    //     // Create a "hello world!" string. Return the index of the word "world".
    //     var str5="hello world!"
    //     var serstr5=str5.indexOf("world")
    //     return serstr5;
        
    // }
    // var inxserstr5=lvl3exercise5()
    // console.log(inxserstr5)

    
    // function lvl4exercise1() {
    //     // Return the boolean value "true"
    //     return true;

        
    // }
    // var out=lvl4exercise1();
    // console.log(out)
    
    // function lvl4exercise2() {
    //     // Return the boolean value "false"
    //     return false;
    
    // }
    // var out2=lvl4exercise2();
    // console.log(out2)

    // function lvl4exercise3(bool) {
    //     // Return the opposite of the input boolean value
    //       return !bool
    // }
    // var out3=lvl4exercise3(true)
    // console.log(out3) 
    
    // function lvl4exercise4(bool1, bool2) {
    //     // Return the logical "and" of the input boolean values
    //     return bool1 && bool2
    
    // }
    // var out4=lvl4exercise4(true, false)
    // console.log(out4)
    
    // function lvl4exercise5(bool1, bool2) {
    //     // Return the logical "or" of the input boolean values
    //     return bool1|| bool2
        
    // }


    // var out4=lvl4exercise5(true, true)
    // console.log(out4)
    
    // function lvl4exercise6(bool1, bool2) {
    //     // Return the logical "equivalence" of the input boolean values
    //     return bool1==bool2;
    // }
    // var out4=lvl4exercise6(false, false)
    // console.log(out4)

    // function lvl5exercise1() {
    //     // Push the string "hello" into the array and return it.
    //     var array = [1, "adam"];
    //     var str="hello";
    //     array.push(str);
    //     return array;
        
    // }
    //   var out=lvl5exercise1()
    //   console.log(out)
    
//     function lvl5exercise2() {
//         // Remove the last element from the array and return it
//         var array = [1, "adam"];
//         array.pop();
//         return array;
//     }
// var out =lvl5exercise2()
// console.log (out)
    
    // function lvl5exercise3() {
    //     // Return the length of the array
    //     var array = [1, "adam"];
    //      return array.length;
    
    // }
    // var out=lvl5exercise3()
    // console.log(out)
    
    // function lvl5exercise4() {
    //     // Return the index of "adam" in the array
    //     var array = [1, "adam"];
    //     return array.indexOf("adam")
    
    // }
    // var out =lvl5exercise4()
    // console.log(out)
    // function lvl6exercise1(num) {
    //     // Return 'hello' if num is 1, 'world' if num is 2, otherwise return'bye'
    //     if(num==1){
    //         return "hello"
    //     }
    //     else if(num==2){
    //           return "world"
    //     }
    //     else{
    //         return "bye"

    //     }
    // }
    //  var out=lvl6exercise1(4)
    //  console.log(out)
    
    // function lvl6exercise2() {
    //     // Push 10 "hello" strings into the array using a for loop, then return it
    //     var array = [];
    //     for(var i=0;i<=10;i++){   
    //     array.push("hello")
    //     }
    //     return array
    
    // }
    // var out =lvl6exercise2()
    // console.log(out)


    
    // function lvl6exercise3() {
    //     // Empty this array using a while loop and return it
    //     var array = ["hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello"];
    //      for(var i=0;i<10;i++){
    //          array.pop()
    //      }
    //      return array
    // }
    // var out =lvl6exercise3()
    // console.log(out)

    // Write a function that takes a number as an input. 
// Have it create an empty array and then push a string into the array as many 
// times as the input number
//
// Name the function "finalFunction"

// function finalFunction(num){
//     var array=[];
//     for (var i=1;i<=num;i++){
//         array.push("hello")
//     }
// return array

// }
// var out=finalFunction(5)
// console.log(out)