//1 . Positive Numbers
// Write a function which takes an array of numbers as input and returns a new array containing only the positive numbers in the given array.

// function positive(arr){
// var newarr = arr.filter(function(value){
//     if (value>0) 
//       return value 
// });
//    return newarr
// }
// console.log(positive([1,2,4,7,9,-1,-2,-3]))

// 2.Even Numbers
// Write a function which takes an array of numbers as input and returns a new array containing only the even numbers in the given array.

// function even(arr){

//     var newarr=arr.filter(function(value){
//         if(value%2==0)
//         return value;

//     })
    
    
//     return newarr;
// }

// console.log(even([1,2,3,4,5,6,7,8]))


// 3.Square the Numbers
// Write a function which takes an array of numbers as input and returns a 
// new array containing result of squaring each of the numbers in the given array by two. 
// Example: squareTheNumbers([1, 2, 3]) should give [1, 4, 9]
//  function square(arr){
//       var newarr=arr.map(function(value){
//           return value**2;
//      })
//     return newarr   
//  }
//  console.log(square([2,3,4,5]))
     
// Cities 1
// Write a function which takes an array of city objects like such:
   
// var cities = [ 
//     { name: 'Los Angeles', temperature: 60.0}, 
//     { name: 'Atlanta', temperature: 52.0 }, 
//     { name: 'Detroit', temperature: 48.0 }, 
//     { name: 'New York', temperature: 80.0 } ];
    
//     function cities1(arr){
//         var newcities=cities.filter(function(value,index,arr){
//             if(value.temperature < 70.0) 
//             return value
//         })
//         var citynames=newcities.map(function(value){
//             return value.name

//         })
//         return citynames;
//     }
//     console.log(cities1(cities))

// Good Job!
// Given an array of people's names:
// var people = [ 'Dom', 'Lyn', 'Kirk', 'Autumn', 'Trista', 'Jesslyn', 'Kevin', 'John', 'Eli', 'Juan', 'Robert', 'Keyur', 'Jason', 'Che', 'Ben' ];

// function good(arr){
//     arr.forEach(function(value){
//      console.log("Good Job "+value+"!")
//     });
// }

// good(people)



// Given an array of people's names:
// var people = [ 'Dom', 'Lyn', 'Kirk', 'Autumn', 'Trista', 'Jesslyn', 'Kevin', 'John', 'Eli', 'Juan', 'Robert', 'Keyur', 'Jason', 'Che', 'Ben' ];

// people.sort();
// console.log(people)

// Sort an array, 2
// Sort the same array, but not by alphabetically order, but by how long each name is, shortest name first.    

// var people = [ 'Dom', 'Lyn', 'Kirk', 'Autumn', 'Trista', 'Jesslyn', 'Kevin', 'John', 'Eli', 'Juan', 'Robert', 'Keyur', 'Jason', 'Che', 'Ben' ];
// people.sort(function(a,b){
//     return a.length-b.length
// })
// console.log(people)


// Given an array of array of numbers like:
// var arr = [ 
//     [1, 3, 4], 
//     [2, 4, 6, 8], 
//     [3, 6] ];
//     console.log(arr.sort(function(a,b){
//         return a.reduce(function(accumulator,currentValue){
//              return accumulator+currentValue
//         })-b.reduce(function(accumulator,currentValue){
//             return accumulator+currentValue
//        })
//     }))
    
    //  var sumarr=arr.map(function(value,index,arr){  
    //            return value.sort(function(a,b){
    //                return a-b;
    //            })              
    //     })        
    
    
    // console.log(sumarr)

    

// var arr = [ 
// [1, 3, 4], 
// [2, 4, 6, 8], 
// [3, 6] ];

//  var sumarr=arr.map(function(value,index,arr){  
//            return value.reduce(function(accumulator,currentValue,index,arr){ 
//              return  accumulator+currentValue ;              
//     })        
// })
// console.log(sumarr)
// console.log(sumarr.sort(function(a,b){
//     return a-b;
// }))


// 3 times
// Given this function:
//  var fun=function(){
//      console.log( "Hello World")
//  }
// var fun=function(){
//     console.log( "Hello World")
// }
// function call3Times(fun){ 
//      fun(); 
//      fun(); 
//      fun(); 
//     }   
// call3Times(fun)

// n times
// You will write a function callNTimes that takes two arguments: 
// times as a number, and fun as a function. 
// It will call that function for that many times. Example:

// var fun=function(){
//     console.log("Hello World! ")
// }
// function callNTimes(num,fun){
//     for(i=0;i<num;i++){
//         fun();
//     }
// }

// callNTimes(3,fun);
// callNTimes(5,fun);
// callNTimes(2,fun);

// Sum an array
// Write a function sum that takes an array of numbers as argument and 
// returns the sum of those numbers. Use the reduce method to do this.

// function sum(arr){
//     var sumarr= arr.reduce(function(accumulator,currentVaule){
//         return accumulator+currentVaule;
//     })
//         return sumarr;
    
// }
// console.log(sum([1,2,3]))

// Bonus: forEach
// Implement your own custom forEach function which 
// takes two arguments: an array arr and a function fun. It will call fun passing 
// each item in arr to fun as the first argument. Example:

// var arr = [ 
// { name: 'Bob' }, 
// { name:'Alice' }, 
// { name:'Joe' } ]; 
// var fun=function(person){
//     console.log("Hello,"+person+"!")
// }

// function foreach(arr,fun){
//     arr.forEach(function(element){
//        return fun(element.name);
//     })
 
// }
// foreach(arr,fun);
   

// var arr = [ 
//     { name: 'Bob' }, 
//     { name:'Alice' }, 
//     { name:'Joe' } ]; 

//     arr.forEach(function(element){
//          console.log("Hello "+element.name+"!")
//     })


// Bonus: map
// Implement your own custom map function which takes two arguments: 
// an array arr and a function fun. It will return a new array, 
// with each of its results being the result of calling fun with each array element.

// var arr = [ 1,2,3,4
//          ]; 

//   function map(arr,fun){      
//     var newarr=[] 
//     arr.forEach(function(element){
        
//     })    


        





