
var pwLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
var pwNumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
var pwSymbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



function generatePassword() {
    var letterGroup = ""
    for (var i = 0; i < 6; i++) {
    var randLetter = pwLetters[Math.floor(Math.random() * pwLetters.length)]
    letterGroup += randLetter
  }
    var numberGroup = ""
    for (var i = 0; i < 2; i++) {
    var randNumber = pwNumbers[Math.floor(Math.random() * pwNumbers.length)]
    numberGroup += randNumber
}
    var symbolGroup = ""
    for (var i = 0; i < 2; i++) {
    var randSymbol = pwSymbols[Math.floor(Math.random() * pwSymbols.length)]
    symbolGroup += randSymbol
    }
     var completePassword = symbolGroup + numberGroup + letterGroup;
     var shufflePassword = completePassword.split('').sort(function(){return 0.5-Math.random()}).join('');
     // var completeArray = completePassword.split('')
     // var hardPassword = ""
     // for (var i = 0; i < completeArray.length; i++) {
     // var randHard = completeArray[Math.floor(Math.random() * completeArray.length)]
     // hardPassword += randHard    
     // }
console.log(shufflePassword)
  }

generatePassword()
  
  

  
  
  
  /*function getKindaComplex() {
  var passRand = Math.floor(Math.random() * kindaComplex.length);
       $(document).on("click", "#kindaComplex", function() {
      document.getElementById("target1").innerHTML = kindaComplex[passRand];
       });
  }
  getKindaComplex();*/
