function printSquare(width,height){  
    var fArray=[] 
    var str="*"
    var empstr=" "  
  for(var i=1;i<=height;i++){
    var stringArr=[]
    var ele=""
        if(i == 1||i==height) {
            for(var k=1;k<=width;k++){
              stringArr.push(str)
            }
            
             ele=ele.concat(stringArr.join("")) 
            console.log(ele)
            
        }
        
        else {
            for(var j=1;j<=width;j++){
                if(j == 1||j==width){
                  stringArr.push(str)
                               }
                else{
                    stringArr.push(empstr)
                     }
                 
                    }                
                var emele= stringArr.join("")
                console.log(emele);
                
          
            } 
  }      
  
}
 printSquare(6,4)

