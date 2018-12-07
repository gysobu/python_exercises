// function lvl6exercise3() {
//         // Empty this array using a while loop and return it
//         var array = ["hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello"];
//          for(var i=array.len;i > 0; i--){
//              array.pop()
//          }
//          return array
//         }
//         console.log(lvl6exercise3())

// function lvl6exercise3() {
//             // Empty this array using a while loop and return it
//       var array = ["hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello", "hello"];
//         while(array.length>0){
//             array.pop()
//         }
//            console.log(lvl6exercise3())

//     }



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
                 
                    }                 
                var emele= stringArr.join("")
                console.log(emele);
                fArray.push(emele);
          
            }

    
     
  } 
     console.log(fArray)
     for(var i=1;i<fArray.length;i++){
      console.log(fArray[i])
  
}
 printSquare(6,4)
